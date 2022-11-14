from flask.views import MethodView
from flask_login import login_required


class APIView(MethodView):

    decorators: list = [
        login_required
    ]
