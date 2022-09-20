from app.blueprints.home_blueprint import home
from app.blueprints.predict_blueprint import predict


def init_app(app):
    app.register_blueprint(home)
    app.register_blueprint(predict)
