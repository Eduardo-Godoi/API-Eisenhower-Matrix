from flask import Flask

from app.routes.task_route import bp as task_bp
from app.routes.category_route import bp as category_bp
from app.routes.get_all_route import bp as get_all_bp


def init_app(app: Flask):
    app.register_blueprint(category_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(get_all_bp)
