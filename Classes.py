import csv




class Cartes:
    def __init__(self, ID, type,descriptions,durée):
        self.ID = ID
        self.Type = type
        self.Descriptions = descriptions
        self.Durée = durée

class Joueurs:
    def __init__(self, pseudo):
        self.Pseudo = pseudo
        self.Stock = 0
        self.Points = 0
        self.Trajets = []

class Trajets:
    def __init__(self, ID, villeDepart, villeArrivée,coûts, points):
        self.ID = ID
        self.VilleDepart = villeDepart
        self.VilleArrivée = villeArrivée
        self.Coûts = coûts
        self.Points = points

        if coûts >= 0 and coûts <= 400:
            self.Difficulté = "A"

        elif coûts >= 401 and coûts <= 900:
            self.Difficulté = "B"

        else:
            self.Difficulté = "C"

class Questions_Réponses:
    def __init__(self, ID, question, réponse,difficulté,récompense):
        self.ID = ID
        self.Question = question
        self.Réponse = réponse
        self.Difficulté = difficulté
        self.Récompense = récompense

def CSV_to_trajets():
    liste_trajets = []
    with open("Trajets.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
            Trajets(int(row[0]), row[1], row[2], int(row[3]), int(row[4]))
            liste_trajets.append(Trajets)

    return liste_trajets

def CSV_to_cartes():
    liste_cartes = []
    with open("Cartes.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            Cartes(int(row[0]), row[1], row[2], int(row[3]))
            liste_cartes.append(Cartes)

    return liste_cartes

