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
            
    def deplaceDaleks(self):
        for i in self.daleks:
            i.deplacement()
             
    
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
        for j in Jeu.docteur:
            if self.x > j.x:
                self.x = self.x - 1
            if self.x < j.x:
                self.x = self.x + 1
            if self.y > j.y:
                self.y = self.y - 1
            if self.y < j.y:
                self.y = self.y + 1
        

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
        
    def deplacement(self, direction):
        # Prend le nombre sur le pave numerique qui definie la direction.
        if direction == 1:      # bas-gauche
            self.y = self.y - 1
            self.x = self.x - 1
        elif direction == 2:    # bas
            self.y = self.y - 1
        elif direction == 3:    # bas-droite
            self.y = self.y - 1
            self.x = self.x + 1
        elif direction == 4:    # gauche
            self.x = self.x - 1
        elif direction == 5:    # bouge pas
        elif direction == 6:    # droite
            self.x = self.x + 1
        elif direction == 7:    # haut-gauche
            self.y = self.y + 1
            self.x = self.x - 1
        elif direction == 8:    # haut
            self.y = self.y + 1
        elif direction == 9:    # haut-droite
            self.y = self.y + 1
            self.x = self.x + 1
 
#================================ MAIN===================================================
m = Modele()
j = Jeu()

for i in Jeu.docteur:
    print(i.x, ",", i.y)
for k in range(10):
    j.deplaceDaleks()
    for i in Jeu.daleks:
        print(i.x, ", ", i.y)
    print("==========================")
            
                        
