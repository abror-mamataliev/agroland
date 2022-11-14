from dataclasses import dataclass
from flask import (
    make_response,
    render_template,
    request,
    url_for
)
from flask.views import MethodView
from flask.wrappers import Response


@dataclass(init=False)
class BaseView(MethodView):

    __appname__: str
    _template: str
    _forms: dict

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[f'_{key}'] = value
    
    def get(self):
        if '_template' not in self.__dict__:
            raise AttributeError("'template' atribute is required")
        response: Response = make_response(render_template(
            f"{self.__appname__}/{self._template}",
            **{ k: v for k, v in self._forms.items() } if '_forms' in self.__dict__ else {},
            **{ k: v for k, v in self.__dict__.items() if k not in ['_template', '_forms'] }
        ))
        return response
