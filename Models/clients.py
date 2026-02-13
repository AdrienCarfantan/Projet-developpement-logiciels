class Client:
    def __init__(self, id_client: str, nom: str, prenom: str,
                 mail: str, telephone: str, adresse: str):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.telephone = telephone
        self.adresse = adresse

    def __str__(self):
        return f"{self.id_client} - {self.prenom} {self.nom} ({self.mail})"


    def to_dict(self):
        return {
            "id_client": self.id_client,
            "nom": self.nom,
            "prenom": self.prenom,
            "mail": self.mail,
            "telephone": self.telephone,
            "adresse": self.adresse
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id_client"],
            data["nom"],
            data["prenom"],
            data["mail"],
            data["telephone"],
            data["adresse"]
        )
