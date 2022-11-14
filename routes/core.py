from modules import core
from views import core as core_views


core.add_url_rule("/", view_func=core_views.IndexView.as_view("index"))
