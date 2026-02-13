from ui import afficher_menu, demander_choix_menu

def main():
    while True:
        afficher_menu()
        choix = demander_choix_menu()
        
        if choix == "7":
            print("Au revoir !")
            break
        else:
            print(f"Option {choix} sélectionnée (pas encore implémentée).")

if __name__ == "__main__":
    main()
