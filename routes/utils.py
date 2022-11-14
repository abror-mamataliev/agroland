from flask import Flask


def register_default_route(app: Flask) -> None:
    """
    Implementation of root route
    """
    from flask import (
        redirect,
        url_for
    )

    @app.route("/")
    def index():
        return redirect(url_for("base.index"))
    
    @app.route("/uploads/<path:filename>", methods=["GET"])
    def uploads(filename: str):
        from flask import send_from_directory

        return send_from_directory("uploads", filename)
