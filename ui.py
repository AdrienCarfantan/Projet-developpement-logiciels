def afficher_menu():
    print("="*60)
    print("SYSTÈME DE LOCATION DE VÉHICULES")
    print("="*60)
    print("1. Afficher les clients")
    print("2. Afficher les véhicules")
    print("3. Créer une réservation")
    print("4. Afficher la grille tarifaire")
    print("5. Afficher toutes les réservations")
    print("6. Afficher les réservations d'un client")
    print("7. Quitter")
    print("="*60)

def demander_choix_menu():
    choix = input("Votre choix : ")
    return choix

from data_manager import charger_clients, charger_vehicules

def afficher_clients():
    clients = charger_clients()
    print("="*60)
    print("LISTE DES CLIENTS")
    print("="*60)
    for client in clients:
        print(client)
    print("="*60)

def afficher_vehicules():
    vehicules = charger_vehicules()
    print("="*60)
    print("LISTE DES VÉHICULES")
    print("="*60)
    for vehicule in vehicules:
        print(vehicule)
    print("="*60)
