from typing import Any, Callable, Dict, List, Sequence, Tuple

from fastapi.security.base import SecurityBase
from pydantic import BaseConfig, Schema
from pydantic.error_wrappers import ErrorWrapper
from pydantic.errors import MissingError
from pydantic.fields import Field, Required
from pydantic.schema import get_annotation_from_schema
from starlette.concurrency import run_in_threadpool
from starlette.requests import Request

param_supported_types = (str, int, float, bool)


class SecurityRequirement:
    def __init__(self, security_scheme: SecurityBase, scopes: Sequence[str] = None):
        self.security_scheme = security_scheme
        self.scopes = scopes


class Dependant:
    def __init__(
        self,
        *,
        path_params: List[Field] = None,
        query_params: List[Field] = None,
        header_params: List[Field] = None,
        cookie_params: List[Field] = None,
        body_params: List[Field] = None,
        dependencies: List["Dependant"] = None,
        security_schemes: List[SecurityRequirement] = None,
        name: str = None,
        call: Callable = None,
        request_param_name: str = None,
    ) -> None:
        self.path_params = path_params or []
        self.query_params = query_params or []
        self.header_params = header_params or []
        self.cookie_params = cookie_params or []
        self.body_params = body_params or []
        self.dependencies = dependencies or []
        self.security_requirements = security_schemes or []
        self.request_param_name = request_param_name
        self.name = name
        self.call = call
