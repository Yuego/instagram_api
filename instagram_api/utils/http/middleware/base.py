from abc import ABCMeta, abstractmethod

from requests import Response, PreparedRequest

from typing import Optional, Tuple

from urllib3.response import HTTPResponse

"""
@author: Joshua Carp
@source: https://github.com/jmcarp/requests-middleware/

Модуль взят оттуда и адаптирован к библиотеке Typing
для удобства дальнейшей работы и дабы не тянуть зависимости
из-за по сути одного файла 

"""
__all__ = ['BaseMiddleware']


class BaseMiddleware(metaclass=ABCMeta):
    ordering = 128

    def before_init_poolmanager(self, connections, maxsize: int, block: bool = False) -> Optional[dict]:
        return {}

    def before_send(self, request: PreparedRequest, *args, **kwargs) -> Optional[Response]:
        return None

    def before_build_response(
            self,
            req: PreparedRequest,
            resp: HTTPResponse,
    ) -> Tuple[PreparedRequest, HTTPResponse]:
        return req, resp

    def after_build_response(self, req: PreparedRequest, resp: HTTPResponse, response: Response) -> Response:
        return response
