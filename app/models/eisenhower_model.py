from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String


@dataclass
class Eisenhower(db.Model):
    __tablename__ = 'eisenhowers'

    type: str

    id = Column(Integer, primary_key=True)
    type = Column(String)
