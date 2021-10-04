from dataclasses import dataclass

from app.configs.database import db
from app.models.tasks_categories_model import tasks_categories
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class Categorie(db.Model):
    __tablename__ = 'categories'

    name: str

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String)

    tasks = relationship("Task",secondary=tasks_categories,back_populates="category")
