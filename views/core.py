from .base import BaseView


class CoreView(BaseView):

    __appname__: str = "core"


class IndexView(CoreView):

    def __init__(self, **kwargs):
        self._template: str = "index.html"
        super().__init__(**kwargs)
