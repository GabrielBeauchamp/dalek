import random
# Classe Modele


class Modele():
    hauteur = 24
    largeur = 80
    
    
    #options
    #quitter
    
    
class Jeu():
    nbDaleks = 5
    nbDalekInc = 5
    
    daleks = []
    docteur = []
    tas = []
    def __init__(self):
        for i in range(self.nbDaleks):
            self.daleks.append(Dalek())
        self.docteur.append(Docteur())
            
             
    
class Dalek():
    def __init__(self):
        valide = False
        while not valide:
            self.x = random.randrange(Modele.hauteur)
            self.y = random.randrange(Modele.largeur)
            if len(Jeu.daleks) != 0:
                for i in Jeu.daleks:
                    if i.x == self.x and i.y == self.y:
                        valide = False
                        break
                    else:
                        valide = True
            else:
                valide = True
    
    def deplacement(self):
        

class Docteur():
    def __init__(self):
        valide = False
        while not valide:
            self.x = random.randrange(Modele.hauteur)
            self.y = random.randrange(Modele.largeur)
            if len(Jeu.daleks) != 0:
                for i in Jeu.daleks:
                    if (i.x == self.x and i.y == self.y):
                        valide = False
                        break
                    else:
                        valide = True
            else:
                valide = True
        self.nbZap = 1
        self.hasZapped = False #Dans le tour, as-t'il zappe?
        
m = Modele()
j = Jeu()

for i in Jeu.daleks:
    print(i.x, ", ", i.y, "\n")
            
                        