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


import json
from Models.reservations import Reservation

RESERVATIONS_FILE = "reservations.json"

def charger_reservations(fichier=RESERVATIONS_FILE):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
        reservations = [Reservation.from_dict(r) for r in data]
        print(f"✓ {len(reservations)} réservation(s) chargée(s)")
        return reservations
    except FileNotFoundError:
        print(f" Fichier {fichier} introuvable")
        return []
    except json.JSONDecodeError:
        print(f" JSON invalide dans {fichier}")
        return []

def sauvegarder_reservation(reservation: Reservation, fichier=RESERVATIONS_FILE):
    reservations = charger_reservations(fichier)
    reservations.append(reservation)
    data = [r.to_dict() for r in reservations]

    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✓ Réservation sauvegardée dans {fichier}")
    return True

def generer_id_reservation(fichier=RESERVATIONS_FILE):
    reservations = charger_reservations(fichier)
    if not reservations:
        return "R0001"
    
    dernier_id = max(int(r.id_reservation[1:]) for r in reservations)
    return f"R{dernier_id + 1:04d}"

def filtrer_reservations_par_client(id_client: str, fichier=RESERVATIONS_FILE):
    reservations = charger_reservations(fichier)
    return [r for r in reservations if r.id_client == id_client]
