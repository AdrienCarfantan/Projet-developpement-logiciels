class TarifsManager:
    TARIFS = {
        4: {100: (0,0), 200: (0,0), 300: (0,0), "+300": (0,0)},
        5: {100: (0,0), 200: (0,0), 300: (0,0), "+300": (0,0)},
        6: {100: (0,0), 200: (0,0), 300: (0,0), "+300": (0,0)},
    }

    @classmethod
    def obtenir_tarif(cls, cylindree: int, forfait_km: int):
        """
        Retourne (cout_journalier, prix_km_supp) pour la cylindrée et le forfait donnés.
        """
        pass 

    @classmethod
    def afficher_grille(cls):
        """
        Affiche la grille tarifaire formatée.
        """
        pass 
