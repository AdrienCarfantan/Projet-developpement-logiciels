class Reservation:
    def __init__(self, id_reservation: str, id_client: str, id_vehicule: str,
                 date_depart: str, date_retour: str, forfait_km: int,
                 cout_journalier: float, prix_km_supp: float):
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_vehicule = id_vehicule
        self.date_depart = date_depart
        self.date_retour = date_retour
        self.forfait_km = forfait_km
        self.cout_journalier = cout_journalier
        self.prix_km_supp = prix_km_supp
        self.cout_estime = 0.0  # sera calculé plus tard

    def __str__(self):
        return (f"Réservation {self.id_reservation} | Client: {self.id_client} "
                f"| Véhicule: {self.id_vehicule} | {self.date_depart} ➔ {self.date_retour} "
                f"| Forfait: {self.forfait_km} km | Coût estimé: {self.cout_estime:.2f}€")
    
    def to_dict(self):
        """Sérialisation en dictionnaire pour JSON"""
        return {
            "id_reservation": self.id_reservation,
            "id_client": self.id_client,
            "id_vehicule": self.id_vehicule,
            "date_depart": self.date_depart,
            "date_retour": self.date_retour,
            "forfait_km": self.forfait_km,
            "cout_journalier": self.cout_journalier,
            "prix_km_supp": self.prix_km_supp,
            "cout_estime": self.cout_estime
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Création d'une instance à partir d'un dictionnaire JSON"""
        return cls(
            id_reservation=data["id_reservation"],
            id_client=data["id_client"],
            id_vehicule=data["id_vehicule"],
            date_depart=data["date_depart"],
            date_retour=data["date_retour"],
            forfait_km=data["forfait_km"],
            cout_journalier=data.get("cout_journalier", 0.0),
            prix_km_supp=data.get("prix_km_supp", 0.0)
        )
