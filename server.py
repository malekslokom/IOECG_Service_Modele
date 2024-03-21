from models.models import Model
from consul import register_service_with_consul
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

import json

app = Flask(__name__)
CORS(app)

#connection bd
app.config["SQLALCHEMY_DATABASE_URI"]= 'postgresql://postgres:postgresql@localhost:5433/models'
#app.config.from_object('config')
db = SQLAlchemy(app)

class TaskNature(Enum):
    BINARY_CLASSIFICATION = 'classification binaire'
    CLASSIFICATION_MULTI_CLASS = 'classification multi-class'
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
    task_nature = db.Column(db.String(50))

# Définition de la route pour récupérer les modèles
@app.route("/api/models", methods=["GET"])
def get_models():
    # Récupérer tous les modèles depuis la base de données
    models = Model.query.all()
    # Créer une liste des données des modèles pour les renvoyer au client
    model_data = [{
        "id": model.id,
        "name": model.name,
        "author": model.author,
        "project_name": model.project_name,
        "description": model.description,
        "architecture_name": model.architecture_name,
        "architecture_version": model.architecture_version,
        "architecture_description": model.architecture_description,
        "total_params": model.total_params,
        "model_size": model.model_size,
        "batch_size": model.batch_size,
        "learning_rate": model.learning_rate,
        "task_nature": model.task_nature
    } for model in models]
    # Renvoyer les données des modèles au format JSON
    return jsonify(model_data)

if __name__ == "__main__":
    register_service_with_consul() 
    app.run(debug=True)
