from enum import Enum
from flask_sqlalchemy import SQLAlchemy
from database.db import db

class TaskNature(Enum):
    BINARY_CLASSIFICATION = 'classification binaire'
    MULTI_CLASS_CLASSIFICATION = 'classification multi-class'
    REGRESSION = 'regression'

class Model(db.Model):
    __tablename__ = 'models'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255))
    project_name = db.Column(db.String(255))
    description = db.Column(db.Text)
    architecture_name = db.Column(db.String(255))
    architecture_version = db.Column(db.String(50))
    architecture_description = db.Column(db.Text)
    total_params = db.Column(db.Integer)
    model_size = db.Column(db.String(50))
    batch_size = db.Column(db.Integer)
    learning_rate = db.Column(db.Float)
    task_nature = db.Column(db.Enum(TaskNature))