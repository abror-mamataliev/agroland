from flask_login import login_required

from .base import BaseView


class DashboardView(BaseView):

    __appname__: str = "dashboard"

    decorators: list = [
        login_required
    ]


class IndexView(DashboardView):

    def __init__(self, **kwargs):
        self._template = "index.html"
        super().__init__(**kwargs)


class PolygonsView(DashboardView):

    def __init__(self, **kwargs):
        self._template = "polygons.html"
        super().__init__(**kwargs)


class TilesView(DashboardView):

    def __init__(self, **kwargs):
        self._template = "tiles.html"
        super().__init__(**kwargs)
