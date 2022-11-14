from api import dashboard as dashboard_api
from modules import api


api.add_url_rule("/polygons", view_func=dashboard_api.PolygonView.as_view("polygon_list"))
api.add_url_rule("/polygon/create", view_func=dashboard_api.PolygonView.as_view("polygon_create"))
api.add_url_rule("/polygon/data", view_func=dashboard_api.PolygonDataView.as_view("polygon_data"))
