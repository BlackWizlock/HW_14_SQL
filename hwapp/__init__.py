from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")
    app.config["JSON_AS_ASCII"] = False

    from hwapp import hwapp

    app.register_blueprint(hwapp.bp)

    return app
