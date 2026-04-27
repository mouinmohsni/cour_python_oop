from animal import Animal

class Oiseau(Animal):
    def __init__(self, nom, espece, age, regime_alimentaire, envergure):
        # Appel du constructeur de la classe parente
        super().__init__(nom, espece, age, regime_alimentaire)
        self._envergure = envergure

    def get_envergure(self):
        return self._envergure

    def voler(self):
        print(f"{self.get_nom()} l' {self.get_espece()} déploie ses ailes de {self._envergure}m et s'envole.")

    def afficher_informations(self):
        # Appel de la méthode de la classe parente
        super().afficher_informations()
        print(f"Envergure: {self._envergure} mètres")
