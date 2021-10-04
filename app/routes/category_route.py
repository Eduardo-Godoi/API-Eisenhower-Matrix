from flask import Blueprint
from app.controllers.category_controller import create, update, delete

bp = Blueprint('bp_category', __name__, url_prefix='/category')


bp.post('')(create)
bp.patch('/<int:id>')(update)
bp.delete('/<int:id>')(delete)
