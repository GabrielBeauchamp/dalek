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
        

class Docteur():
    def __init__(self):
        valide = False
        while not valide:
            self.x = random.randrange(0,Modele.largeur)
            self.y = random.randrange(0,Modele.hauteur)
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
        self.hasZapped = False #Dans le tour, as-t'il zappe ?
        
    def deplacement(self, direction):
        # Prend le nombre sur le pave numerique qui definie la direction.
        if direction == "1":      # bas-gauche
            self.y = self.y + 1
            self.x = self.x - 1
        elif direction == "2":    # bas
            self.y = self.y + 1
        elif direction == "3":    # bas-droite
            self.y = self.y + 1
            self.x = self.x + 1
        elif direction == "4":    # gauche
            self.x = self.x - 1
        elif direction == "5": # bouge pas
            pass   
        elif direction == "6":    # droite
            self.x = self.x + 1
        elif direction == "7":    # haut-gauche
            self.y = self.y - 1
            self.x = self.x - 1
        elif direction == "8":    # haut
            self.y = self.y - 1
        elif direction == "9":    # haut-droite
            self.y = self.y - 1
            self.x = self.x + 1

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

for k in range(10):
    for i in Jeu.docteur:
        print("Docteur" , i.x, ",", i.y)
    j.deplaceDaleks()
    for i in Jeu.daleks:
        print(i.x, ", ", i.y)
    print("==========================")
    a.afficherJeu()
    touche = input("Touche")
    toucheValide = Jeu.docteur[0].toucheValide(touche)
    if  toucheValide == True :
        print(touche)
        Jeu.docteur[0].deplacement(touche)
        print(Jeu.docteur[0].x)
    
    