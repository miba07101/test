from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hard to guess"

    # a simple page that says hello
    @app.route("/")
    def hello():
        return "Ahoj, World!"

    return app
