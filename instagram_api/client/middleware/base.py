from abc import ABCMeta, abstractmethod

from requests import Response, PreparedRequest
from requests.adapters import HTTPAdapter, DEFAULT_POOLBLOCK

from typing import Optional, Tuple

from urllib3.response import HTTPResponse
from urllib3.poolmanager import PoolManager

"""
@author: Joshua Carp
@source: https://github.com/jmcarp/requests-middleware/

Модуль взят оттуда и адаптирован к библиотеке Typing
для удобства дальнейшей работы и дабы не тянуть зависимости
из-за по сути одного файла 

"""


class BaseMiddleware(metaclass=ABCMeta):

    @abstractmethod
    def before_init_poolmanager(self, connections, maxsize: int, block: bool = False) -> Optional[dict]:
        raise NotImplementedError

    @abstractmethod
    def before_send(self, request, *args, **kwargs) -> Optional[Response]:
        raise NotImplementedError

    @abstractmethod
    def before_build_response(
            self,
            req: PreparedRequest,
            resp: HTTPResponse,
    ) -> Tuple[PreparedRequest, HTTPResponse]:
        raise NotImplementedError

    @abstractmethod
    def after_build_response(self, req: PreparedRequest, resp: HTTPResponse, response: Response) -> Response:
        raise NotImplementedError


class MiddlewareHTTPAdapter(HTTPAdapter):
    poolmanager: PoolManager

    def __init__(self, middlewares: list = None, *args, **kwargs):
        self.middlewares = middlewares or []
        super(MiddlewareHTTPAdapter, self).__init__(*args, **kwargs)

    def register(self, middleware: BaseMiddleware):

        self.middlewares.append(middleware)

    def init_poolmanager(self, connections, maxsize, block=DEFAULT_POOLBLOCK, **pool_kwargs):

        kwargs = {}
        middleware: BaseMiddleware
        for middleware in self.middlewares[::-1]:
            value = middleware.before_init_poolmanager(
                connections=connections,
                maxsize=maxsize,
                block=block
            )
            kwargs.update(value or {})

        self._pool_connections = connections
        self._pool_maxsize = maxsize
        self._pool_block = block

        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            **kwargs,
        )

    def send(self, request: PreparedRequest, *args, **kwargs):

        middleware: BaseMiddleware
        for middleware in self.middlewares:
            value = middleware.before_send(request, **kwargs)

            if isinstance(value, Response):
                return value
            if isinstance(value, HTTPResponse):
                return self.build_response(request, value)
            if value:
                raise ValueError('Middleware `before_send` methods must return `Response`, `HTTPResponse` or `None`')

        return super(MiddlewareHTTPAdapter, self).send(request, *args, **kwargs)

    def build_response(self, req, resp):

        middleware: BaseMiddleware
        for middleware in self.middlewares[::-1]:
            req, resp = middleware.before_build_response(req, resp)

        response = super(MiddlewareHTTPAdapter, self).build_response(req, resp)

        for middleware in self.middlewares[::-1]:
            response = middleware.after_build_response(req, resp, response)

        return response



