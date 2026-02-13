class TarifsManager:
    TARIFS = {
        4: {100: (35.0, 0.25), 200: (50.0, 0.20), 300: (65.0, 0.15), "+300": (80.0, 0.10)},
        5: {100: (45.0, 0.30), 200: (60.0, 0.25), 300: (75.0, 0.20), "+300": (95.0, 0.15)},
        6: {100: (60.0, 0.40), 200: (80.0, 0.35), 300: (100.0, 0.30), "+300": (120.0, 0.25)},
    }

    @classmethod
    def obtenir_tarif(cls, cylindree: int, forfait_km):
        """
        Retourne (cout_journalier, prix_km_supp) pour la cylindrée et le forfait donnés.
        """
        if forfait_km == "+300" or forfait_km > 300:
            cle_forfait = "+300"
        else:
            cle_forfait = forfait_km        
        if cylindree not in cls.TARIFS:
            raise ValueError(f"Cylindrée {cylindree} non gérée")
        if cle_forfait not in cls.TARIFS[cylindree]:
            raise ValueError(f"Forfait {forfait_km} non disponible pour {cylindree} cylindres")
        
        return cls.TARIFS[cylindree][cle_forfait]

    @classmethod
    def afficher_grille(cls):
        print("="*70)
        print("GRILLE TARIFAIRE")
        print("="*70)
        print(f"{'Cylindrée':<10} {'Forfait':<7} {'Coût/jour':<10} {'Prix km supp.':<12}")
        print("-"*70)
        
        for cyl, forfaits in cls.TARIFS.items():
            for fk, (cout_j, prix_km) in forfaits.items():
                print(f"{cyl} cyl.   {fk:<7} {cout_j:>6.2f}€     {prix_km:.2f}€/km")
            print("-"*70)


TarifsManager.afficher_grille()

cout_j, prix_km = TarifsManager.obtenir_tarif(6, +300)
print(cout_j, prix_km)
