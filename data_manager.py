import json
from Models.clients import Client
from Models.vehicules import Vehicule

CLIENTS_FILE = "clients.json"
VEHICULES_FILE = "vehicules.json"


def charger_clients(fichier=CLIENTS_FILE):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
        clients = [Client.from_dict(c) for c in data]
        print(f"✓ {len(clients)} client(s) chargé(s)")
        return clients
    except FileNotFoundError:
        print(f" Fichier {fichier} introuvable")
        return []
    except json.JSONDecodeError:
        print(f"JSON invalide dans {fichier}")
        return []

def charger_vehicules(fichier=VEHICULES_FILE):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
        vehicules = [Vehicule.from_dict(v) for v in data]
        print(f"✓ {len(vehicules)} véhicule(s) chargé(s)")
        return vehicules
    except FileNotFoundError:
        print(f" Fichier {fichier} introuvable")
        return []
    except json.JSONDecodeError:
        print(f" JSON invalide dans {fichier}")
        return []


if __name__ == "__main__":
    clients = charger_clients()
    for c in clients:
        print(c)

    vehicules = charger_vehicules()
    for v in vehicules:
        print(v)