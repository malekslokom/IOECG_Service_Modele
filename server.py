from model.models import db
from consul import register_service_with_consul
from flask import Flask
from flask_cors import CORS
from enum import Enum
from config.config import Config

from api import getAll,health

app = Flask(__name__)
CORS(app)

#connection bd
# app.config["SQLALCHEMY_DATABASE_URI"]= 'postgresql://postgres:postgresql@localhost:5433/models'
app.config.from_object(Config)
db.init_app(app)

# db = SQLAlchemy(app)

# class TaskNature(Enum):
#     BINARY_CLASSIFICATION = 'classification binaire'
#     CLASSIFICATION_MULTI_CLASS = 'classification multi-class'
#     REGRESSION = 'regression'

# class Model(db.Model):
#     __tablename__ = 'models'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     author = db.Column(db.String(255))
#     project_name = db.Column(db.String(255))
#     description = db.Column(db.Text)
#     architecture_name = db.Column(db.String(255))
#     architecture_version = db.Column(db.String(50))
#     architecture_description = db.Column(db.Text)
#     total_params = db.Column(db.Integer)
#     model_size = db.Column(db.String(50))
#     batch_size = db.Column(db.Integer)
#     learning_rate = db.Column(db.Float)
#     task_nature = db.Column(db.String(50))

# Définition de la route pour récupérer les modèles
app.route('/api/models/health')(health)
app.route('/api/models/',methods=["GET"])(getAll)

if __name__ == "__main__":
    register_service_with_consul() 
    app.run(debug=True)
