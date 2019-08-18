from requests import Response, PreparedRequest
from requests.adapters import HTTPAdapter, DEFAULT_POOLBLOCK

from urllib3.response import HTTPResponse
from urllib3.poolmanager import PoolManager

from .base import BaseMiddleware

__all__ = ['MiddlewareHTTPAdapter']


class MiddlewareHTTPAdapter(HTTPAdapter):
    poolmanager: PoolManager
    middlewares: list

    def __init__(self, middlewares: list = None, reorder: bool = False, *args, **kwargs):
        self.middlewares = middlewares or []

        if reorder:
            self.middlewares.sort(key=lambda m: m.ordering)

        super(MiddlewareHTTPAdapter, self).__init__(*args, **kwargs)

    def register(self, middleware: BaseMiddleware, reorder: bool = False):

        self.middlewares.append(middleware)

        if reorder:
            self.middlewares.sort(key=lambda m: m.ordering)

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

    def restart(self):
        self.close()
        self.init_poolmanager(self._pool_connections, self._pool_maxsize, self._pool_block)

    def send(self, request: PreparedRequest, *args, **kwargs):

        middleware: BaseMiddleware
        for middleware in self.middlewares:
            value = middleware.before_send(request, **kwargs)

            if isinstance(value, Response):
                return value
            if isinstance(value, HTTPResponse):
                return self.build_response(request, value)
            if value:
                raise ValueError('Middleware `before_send` methods must return `ApiResponse`, `HTTPResponse` or `None`')

        return super(MiddlewareHTTPAdapter, self).send(request, *args, **kwargs)

    def build_response(self, req, resp):

        middleware: BaseMiddleware
        for middleware in self.middlewares[::-1]:
            req, resp = middleware.before_build_response(req, resp)

        response = super(MiddlewareHTTPAdapter, self).build_response(req, resp)

        for middleware in self.middlewares[::-1]:
            response = middleware.after_build_response(req, resp, response)

        return response
