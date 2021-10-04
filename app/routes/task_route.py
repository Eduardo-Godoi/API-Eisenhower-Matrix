from flask import Blueprint
from app.controllers.task_controler import create, update, delete

bp = Blueprint('bp_task', __name__, url_prefix='/task')


bp.post('')(create)
bp.patch('/<int:id>')(update)
bp.delete('/<int:id>')(delete)
