from app.configs.database import db
from sqlalchemy import Column, Integer

tasks_categories = db.Table('tasks_categories',
    Column('id',Integer, primary_key=True),
    Column('task_id', Integer, db.ForeignKey('tasks.id')),
    Column('category_id', Integer, db.ForeignKey('categories.id'))
)
