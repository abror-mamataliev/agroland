from modules import dashboard
from views import dashboard as dashboard_views


dashboard.add_url_rule("/", view_func=dashboard_views.IndexView.as_view("index"))
dashboard.add_url_rule("/polygons", view_func=dashboard_views.PolygonsView.as_view("polygons"))
