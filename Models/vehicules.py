class Vehicule:
    def __init__(self, id_vehicule: str, marque: str, modele: str,
                 cylindree: int, kilometrage_actuel: float,
                 date_mise_en_circulation: str):
        self.id_vehicule = id_vehicule
        self.marque = marque
        self.modele = modele
        self.cylindree = cylindree
        self.kilometrage_actuel = kilometrage_actuel
        self.date_mise_en_circulation = date_mise_en_circulation

    def __str__(self):
        return (f"{self.id_vehicule} - {self.marque} {self.modele} "
                f"({self.cylindree} cyl., {self.kilometrage_actuel} km)")


    def to_dict(self):
        return {
            "id_vehicule": self.id_vehicule,
            "marque": self.marque,
            "modele": self.modele,
            "cylindree": self.cylindree,
            "kilometrage_actuel": self.kilometrage_actuel,
            "date_mise_en_circulation": self.date_mise_en_circulation
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id_vehicule"],
            data["marque"],
            data["modele"],
            data["cylindree"],
            data["kilometrage_actuel"],
            data["date_mise_en_circulation"]
        )
