import random
import os
# Classe Modele


class Modele():
    hauteur = 20
    largeur = 30
    
    
    #options
    #quitter
    
    
class Jeu():
    nbDaleks = 5
    nbDalekInc = 5
    #finPartie = False
    
    daleks = []
    docteur = []
    tas = []
    def __init__(self):
        self.finPartie = False
        for i in range(self.nbDaleks):
            self.daleks.append(Dalek())
        self.docteur.append(Docteur())
            
    def deplaceDaleks(self):
        for i in self.daleks:
            i.deplacement()
            
    def collisionDaleks(self):
        aDelete = []
        for i in self.daleks:
            if i.collision() == True:
                aDelete.append(i)
        if len(aDelete) > 0:
            for tas in aDelete:
                self.daleks.remove(tas)
    
class Dalek():
    def __init__(self):
        valide = False
        while not valide:
            self.x = random.randrange(0,Modele.largeur)
            self.y = random.randrange(0,Modele.hauteur)
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
                
    def collision(self):
        for i in Jeu.daleks:
            if self is i:
                pass
            else:
                if self.x == i.x and self.y == i.y:
                    t = Tas(self.x,self.y)
                    Jeu.tas.append(t)
                    return True

class Docteur():
    def __init__(self):
        #self.estMort = False
        valide = False
        while not valide:
            self.x = random.randrange(0,Modele.largeur)
            self.y = random.randrange(0,Modele.hauteur)
            if len(Jeu.daleks) != 0:
                for i in Jeu.daleks:
                    if i.x == self.x and i.y == self.y:
                        valide = False
                        break
                    else:
                        valide = True
            else:
                valide = True
        self.nbZap = 1
        self.hasZapped = False #Dans le tour, as-t'il zappe ?
     
    def deplacementValide(self, nouvellePosX, nouvellePosY):
         if nouvellePosX < 0 or nouvellePosX >= Modele.largeur:
             return False
         if nouvellePosY < 0 or nouvellePosY >= Modele.hauteur:
             return False
         for i in Jeu.tas:
             if i.x == nouvellePosX and i.y == nouvellePosY:
                 return False
        #Regarder aussi les daleks ?
        
         return True
        
    def deplacement(self, direction):
        # Prend le nombre sur le pave numerique qui definie la direction.
        if direction == "1":      # bas-gauche
            if self.deplacementValide(self.x - 1, self.y + 1):
                self.y = self.y + 1
                self.x = self.x - 1
        elif direction == "2":    # bas
            if self.deplacementValide(self.x, self.y + 1):
                self.y = self.y + 1
        elif direction == "3":    # bas-droite
            if self.deplacementValide(self.x + 1, self.y + 1):
                self.y = self.y + 1
                self.x = self.x + 1
        elif direction == "4":    # gauche
            if self.deplacementValide(self.x - 1, self.y):
                self.x = self.x - 1
        elif direction == "5": # bouge pas
            pass   
        elif direction == "6":    # droite
            if self.deplacementValide(self.x + 1, self.y):
                self.x = self.x + 1
        elif direction == "7":    # haut-gauche
            if self.deplacementValide(self.x - 1, self.y - 1):
                self.y = self.y - 1
                self.x = self.x - 1
        elif direction == "8":    # haut
            if self.deplacementValide(self.x, self.y - 1):
                self.y = self.y - 1
        elif direction == "9":    # haut-droite
            if self.deplacementValide(self.x + 1, self.y - 1):
                self.y = self.y - 1
                self.x = self.x + 1
            
    def estMort(self, jeu):
        for i in Jeu.daleks:
            if self.x == i.x and self.y == i.y:
                jeu.finPartie = True
        for i in Jeu.tas:
            if self.x == i.x and self.y == i.y:
                jeu.finPartie = True

    def toucheValide(self,touche):
        if touche == "1":      # bas-gauche
            return True

        elif touche == "2":    # bas
            return True
        
        elif touche == "3":    # bas-droite
            return True

        elif touche == "4":    # gauche
            return True

        elif touche == "5":    # bouge pas
            return True
        elif touche == "6":    # droite
            return True

        elif touche == "7":    # haut-gauche
            return True

        elif touche == "8":    # haut
            return True

        elif touche == "9":    # haut-droite
            return True

class Tas():
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Affichage():
    caseVide = "-" #ce qui sera affiche quand il y a une case vide
    
    def __init__(self):
        self.matriceJeu = []
        for i in range(Modele.largeur):
            self.matriceJeu.append([])
            for j in range(Modele.hauteur):
                self.matriceJeu[i].append(self.caseVide)

    
    def clear(self):
        if os.sys.platform == 'win32':
            os.system("cls")
        else:
            os.system('clear')
    
    def actualiserPlateauJeu(self):
        for i in range(Modele.hauteur):
            for j in range(Modele.largeur):
                self.matriceJeu[j][i] = self.caseVide #Vide la matrice d'affichage
                
        for i in Jeu.daleks:
            self.matriceJeu[i.x][i.y] = 'x' #Ajoute les daleks dans la matrice d'affichage
            
        for i in Jeu.tas:
            self.matriceJeu[i.x][i.y] = '*' #Ajoute les tas dans la matrice d'affichage
            
        for i in Jeu.docteur:
            self.matriceJeu[i.x][i.y] = 'd' #Ajoute le docteur dans la matrice d'affichage
            
    def afficherJeu(self):
        self.clear()
        self.actualiserPlateauJeu()
        for i in range(Modele.hauteur):
            for j in range(Modele.largeur):
                print(self.matriceJeu[j][i], end="")
            print()
            
 
#================================ MAIN===================================================
m = Modele()
j = Jeu()
a = Affichage()

while len(j.daleks) > 0 and j.finPartie == False:
    for i in Jeu.docteur:
        print("Docteur" , i.x, ",", i.y)
    for i in Jeu.daleks:
        print(i.x, ", ", i.y)
    print("==========================")
    a.afficherJeu()
    touche = input("Touche")
    toucheValide = Jeu.docteur[0].toucheValide(touche)
    if  toucheValide == True :
        j.deplaceDaleks()
        Jeu.docteur[0].deplacement(touche)
        j.collisionDaleks()
        Jeu.docteur[0].estMort(j)

        
a.afficherJeu()
input("GAME OVER")
    
    