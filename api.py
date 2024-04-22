from flask import jsonify, request
from model.models import Model
import torch
from tdp_net import TdPNet,ModelArgs
import numpy as np

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

def getModelsWithFilter():
    search_term = request.args.get('search_term', '').lower()
    name_model = request.args.get('name_model', '')
    task_nature = request.args.get('task_nature', '')

    # Construction de la requête de filtrage basée sur les paramètres
    query = Model.query
    if search_term:
         query = query.filter((Model.author.ilike(f'%{search_term}%')) |
                              (Model.name.ilike(f'%{search_term}%')) |
                             (Model.description.ilike(f'%{search_term}%')) |
                             (Model.project_name.ilike(f'%{search_term}%')) |
                             (Model.architecture_name.ilike(f'%{search_term}%')) )

    if name_model:
        query = query.filter(Model.name.ilike(f'%{name_model}%'))
    if task_nature:
        query = query.filter((Model.task_nature.ilike(f'%{task_nature}%')))

    # Exécution de la requête et récupération des résultats
    filtered_models = query.all()

    if filtered_models:
        # Convertir les résultats en une liste de dictionnaires
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
        } for model in filtered_models]
        return jsonify(model_data)
    else:
        return jsonify({"error": "No models found matching the criteria"}), 404


def evaluate_model():
    checkpoint_file='checkpoint-epoch=17-valid_loss=0.03.ckpt'
    checkpoint= torch.load(checkpoint_file, map_location=torch.device('cpu'))
    model_weights= checkpoint["state_dict"]
    for key in list(model_weights):
        model_weights[key.replace("model.","")]=model_weights.pop(key)
    model= TdPNet(ModelArgs(**checkpoint["hyper_parameters"]["model_args"]))
   
    
    for k in ["loss_fn.loss_function.pos_weight",]:
        if k in model_weights:
            del model_weights[k]
    print(model.load_state_dict(model_weights))
    model.eval()
