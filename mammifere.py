from animal import Animal

class Mammifere(Animal):
    def __init__(self, nom, espece, age, regime_alimentaire, couleur_poil):
        # Appel du constructeur de la classe parente
        super().__init__(nom, espece, age, regime_alimentaire)
        self._couleur_poil = couleur_poil

    def get_couleur_poil(self):
        return self._couleur_poil

    def allaiter(self):
        print(f"{self.get_nom()} le {self.get_espece()} allaite ses petits.")

    def afficher_informations(self):
        # Appel de la méthode de la classe parente
        super().afficher_informations()
        print(f"Couleur du poil: {self._couleur_poil}")
