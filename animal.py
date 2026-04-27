class Animal:
    def __init__(self, nom, espece, age, regime_alimentaire):
        # Attributs protégés (convention Python avec _)
        self._nom = nom
        self._espece = espece
        self._age = age
        self._regime_alimentaire = regime_alimentaire

    # Getters
    def get_nom(self):
        return self._nom

    def get_espece(self):
        return self._espece

    def get_age(self):
        return self._age

    def get_regime_alimentaire(self):
        return self._regime_alimentaire

    # Setters avec validation
    def set_age(self, nouvel_age):
        if nouvel_age >= 0:
            self._age = nouvel_age
        else:
            print(f"Erreur pour {self._nom}: L'âge ne peut pas être négatif.")

    def set_regime_alimentaire(self, nouveau_regime):
        if nouveau_regime and nouveau_regime.strip():
            self._regime_alimentaire = nouveau_regime
        else:
            print(f"Erreur pour {self._nom}: Le régime alimentaire ne peut pas être vide.")

    def afficher_informations(self):
        print(f"Nom: {self._nom}, Espèce: {self._espece}, Âge: {self._age}, Régime: {self._regime_alimentaire}")
