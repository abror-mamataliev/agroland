from flask import Flask


def register_modules(app: Flask) -> None:
    from . import (
        api,
        auth,
        core,
        dashboard
    )
    
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(core)
    app.register_blueprint(dashboard, url_prefix="/my")
