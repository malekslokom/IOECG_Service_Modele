import requests
import json

SERVICE_NAME = "models"
SERVICE_PORT = 5000
CONSUL_AGENT_URL = "http://127.0.0.1:8500/v1/agent/service/register"

def register_service_with_consul():
    service_info = {
        "name": SERVICE_NAME,
        "tags": ["models"],
        "port": SERVICE_PORT,
        "check": {
            "http": f"http://127.0.0.1:{SERVICE_PORT}/api/models",
            "interval": "3s"
        }
    }

    try:
        response = requests.put(CONSUL_AGENT_URL, data=json.dumps(service_info))
        if response.status_code == 200:
            print("Service enregistré avec succès dans Consul.")
        else:
            print("Erreur lors de l'enregistrement du service dans Consul:", response.text)
    except Exception as e:
        print("Erreur lors de la communication avec Consul:", str(e))
