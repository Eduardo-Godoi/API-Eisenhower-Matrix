from dataclasses import dataclass

from app.configs.database import db
from app.models.tasks_categories_model import tasks_categories
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class Task(db.Model):
    __tablename__ = 'tasks'

    id: int
    name: str
    description: str
    eisenhower_classification: str
    category = str

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(Integer, db.ForeignKey('eisenhowers.id'), nullable=False)

    eisenhower_classification = relationship('Eisenhower', backref='task', uselist=False)

    category = relationship("Categorie",secondary=tasks_categories,back_populates="tasks")
