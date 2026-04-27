from mammifere import Mammifere
from oiseau import Oiseau

def tester_zoo():
    print("--- Création des animaux ---")
    lion = Mammifere("Simba", "Lion", 5, "Carnivore", "Doré")
    aigle = Oiseau("Aiglon", "Aigle Royal", 3, "Carnivore", 2.2)

    print("\n--- Informations initiales ---")
    lion.afficher_informations()
    aigle.afficher_informations()

    print("\n--- Actions spécifiques ---")
    lion.allaiter()
    aigle.voler()

    print("\n--- Test de l'encapsulation (Modification d'âge) ---")
    lion.set_age(-5) # Invalide
    lion.set_age(6)  # Valide
    lion.afficher_informations()

if __name__ == "__main__":
    tester_zoo()
