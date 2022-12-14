from flask import Flask

from app import create_app


if __name__ == "__main__":
    app: Flask = create_app()
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT']
    )
