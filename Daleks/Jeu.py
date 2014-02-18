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
    nbPointsDalekMort = 5
    #nbDalekInc = 5
    #finPartie = False
    
    daleks = []
    docteur = []
    tas = []
    def __init__(self, niveau, points):
        self.finPartie = False
        self.niveau = niveau
        self.nbDaleks *= niveau
        self.points = points
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
                self.points += self.nbPointsDalekMort
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
        for i in Jeu.tas:
            if self.x == i.x and self.y == i.y:
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
    
    def teleportation(self):
        valide = False
        while not valide:
            nouveauX = random.randrange(0,Modele.largeur)
            nouveauY = random.randrange(0,Modele.hauteur)
            for i in Jeu.daleks:
                if abs(i.x - nouveauX) <= 1 and abs(i.y - nouveauY) <= 1:
                    valide = False
                    break
                else:
                    valide = True
            if valide == True:
                for i in Jeu.tas:
                    if i.x == nouveauX and i.y == nouveauY:
                        valide = False
                        break;
                    else:
                        valide = True
        self.x = nouveauX
        self.y = nouveauY        
    
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
       
    def deplacement(self, direction, jeu):
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
        elif direction == "t":    # teleportage
            self.teleportation()
        elif direction == "z":    # zappeur
            self.zapper(jeu)
    
    def zapper(self, jeu):
        if(self.nbZap > 0):
            for i in jeu.daleks:
                if (abs(i.x - self.x) <= 1) and (abs(i.y - self.y) <=1):
                    jeu.daleks.remove(i)
                    jeu.points += jeu.nbPointsDalekMort
            self.nbZap -= 1
            
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
        elif touche == "t":    # teleportage
            return True
        elif touche == "z":    # zappeur
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

    
    def clear(self):            # Ca, ca c'est bien. Je t'aime Francois.
        if os.sys.platform == 'win32':
            os.system("cls")
        else:
            os.system('clear')
    
    def actualiserPlateauJeu(self):
        for i in range(Modele.hauteur):
            for j in range(Modele.largeur):
                self.matriceJeu[j][i] = self.caseVide #Vide la matrice d'affichage
                
        for i in Jeu.daleks:
            self.matriceJeu[i.x][i.y] = 'X' #Ajoute les daleks dans la matrice d'affichage
            
        for i in Jeu.tas:
            self.matriceJeu[i.x][i.y] = '*' #Ajoute les tas dans la matrice d'affichage
            
        for i in Jeu.docteur:
            self.matriceJeu[i.x][i.y] = '@' #Ajoute le docteur dans la matrice d'affichage
            
    def afficherJeu(self):
        self.clear()
        self.actualiserPlateauJeu()
        for i in range(Modele.hauteur):
            for j in range(Modele.largeur):
                print(self.matriceJeu[j][i], end="")
            print()
            
 
#================================ MAIN===================================================
m = Modele()
j = Jeu(1,0)
a = Affichage()

while len(j.daleks) > 0 and j.finPartie == False:
    for i in Jeu.docteur:
        print("Docteur" , i.x, ",", i.y)
    for i in Jeu.daleks:
        print(i.x, ", ", i.y)
    print("==========================")
    a.afficherJeu()
    print("Points: ", j.points)
    print("Niveau: ", j.niveau)
    print("Nombre de zappeur: ", j.docteur[0].nbZap)
    touche = input("Touche: ")
    toucheValide = j.docteur[0].toucheValide(touche)
    if  toucheValide == True :
        #le docteur doit se deplacer avant les daleks !
        Jeu.docteur[0].deplacement(touche, j)
        j.deplaceDaleks()
        j.collisionDaleks()
        Jeu.docteur[0].estMort(j)

        
a.afficherJeu()
print(len(j.daleks))
input("GAME OVER")
    
    
