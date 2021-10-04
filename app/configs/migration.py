from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):
    Migrate(app, app.db)

    from app.models.categorie_model import Categorie
    from app.models.task_model import Task
    from app.models.eisenhower_model import Eisenhower
    from app.models.tasks_categories_model import tasks_categories