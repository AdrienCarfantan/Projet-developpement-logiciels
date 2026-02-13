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

from data_manager import charger_clients, charger_vehicules, sauvegarder_reservation, generer_id_reservation
from Models.reservations import Reservation
from Models.tarifs import TarifsManager

def demander_reservation():
    print("="*60)
    print("CRÉER UNE NOUVELLE RÉSERVATION")
    print("="*60)

    clients = charger_clients()
    if not clients:
        print("Aucun client disponible.")
        return

    print("Clients disponibles :")
    for c in clients:
        print(f"- {c.id_client} - {c.prenom} {c.nom} ({c.mail})")
    
    id_client = input("ID du client : ").strip()
    if not any(c.id_client == id_client for c in clients):
        print(f"Erreur : client {id_client} inconnu")
        return

    vehicules = charger_vehicules()
    if not vehicules:
        print("Aucun véhicule disponible.")
        return

    print("Véhicules disponibles :")
    for v in vehicules:
        print(f"- {v.id_vehicule} - {v.marque} {v.modele} ({v.cylindree} cyl., {v.kilometrage_actuel} km)")

    id_vehicule = input("ID du véhicule : ").strip()
    vehicule_sel = next((v for v in vehicules if v.id_vehicule == id_vehicule), None)
    if vehicule_sel is None:
        print(f"Erreur : véhicule {id_vehicule} inconnu")
        return

    date_depart = input("Date de départ (AAAA-MM-JJ) : ").strip()
    date_retour = input("Date de retour (AAAA-MM-JJ) : ").strip()

    forfait_dispo = [100, 200, 300, "+300"]
    print("Forfaits disponibles : 100, 200, 300, +300")
    forfait_km = input("Forfait kilométrique : ").strip()
    if forfait_km not in map(str, forfait_dispo):
        print(f"Erreur : forfait {forfait_km} non disponible")
        return

    forfait_km_val = int(forfait_km) if forfait_km.isdigit() else forfait_km

    cout_journalier, prix_km_supp = TarifsManager.obtenir_tarif(vehicule_sel.cylindree, forfait_km_val)

    id_reservation = generer_id_reservation()
    reservation = Reservation(
        id_reservation=id_reservation,
        id_client=id_client,
        id_vehicule=id_vehicule,
        date_depart=date_depart,
        date_retour=date_retour,
        forfait_km=forfait_km_val,
        cout_journalier=cout_journalier,
        prix_km_supp=prix_km_supp
    )

    afficher_recapitulatif(reservation)

    sauvegarder = input("Sauvegarder cette réservation ? (o/n) : ").strip().lower()
    if sauvegarder == "o":
        sauvegarder_reservation(reservation)
        print("✓ Réservation enregistrée avec succès !")
    else:
        print("Réservation annulée.")

def afficher_recapitulatif(reservation: Reservation):
    print("="*60)
    print("RÉCAPITULATIF DE LA RÉSERVATION")
    print("="*60)
    print(reservation)
    print("="*60)
