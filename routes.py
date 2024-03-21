from flask import jsonify, request,Blueprint
from app import app, db
from models import Model, TaskNature



@app.route("/api/models", methods=["GET"])
def get_models():
    models = Model.query.all()
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
        "task_nature": model.task_nature.value
    } for model in models]
    return jsonify(model_data)

# Les autres routes CRUD peuvent être définies de manière similaire
