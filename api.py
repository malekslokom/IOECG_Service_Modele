from flask import jsonify, request
from model.models import Model

def health():
    return jsonify({"status": "up"})


def getAll():
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
    return jsonify(model_data)

