from flask import Blueprint
from app.controllers.castegory_and_tasks_controller import get_all

bp = Blueprint('bp_get_category_tasks', __name__, url_prefix='/')


bp.get('')(get_all)
