import random
import os

class Modele():
    def __init__(self):
        self.hauteur = 20
        self.largeur = 30
    
    #options
    def changerTaille(self, largeur, hauteur):
        self.hauteur = hauteur
        self.largeur = largeur
        
    #quitter
    def quitter(self):
        exit()
    
class Jeu():
    nbPointsDalekMort = 5
    nbDalekInc = 5
    #finPartie = False
    
    daleks = []
    docteur = []
    tas = []
    def __init__(self, niveau, points,hauteur, largeur):
        self.finPartie = False
        self.debutNiveau(niveau, points)
        self.hauteur = hauteur
        self.largeur = largeur
        self.docteur.append(Docteur(self.hauteur, self.largeur))
    
    def debutNiveau(self,niveau, points):
        self.niveau = niveau
        self.nbDaleks = self.nbDalekInc * niveau
        self.points = points
        for i in range(self.nbDaleks):
            self.daleks.append(Dalek(self.hauteur, self.largeur))
    
    def changementNiveau(self):
        self.tas = []   #Enleve les tas
        for i in self.docteur:
            i.nbZap += 1
        self.debutNiveau(self.niveau+1,self.points)
            
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
    def __init__(self, largeur, hauteur):
        valide = False
        while not valide:
            self.x = random.randrange(0, largeur)
            self.y = random.randrange(0, hauteur)
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
    def __init__(self, largeur, hauteur):
        #self.estMort = False
        valide = False
        while not valide:
            self.hauteur = hauteur
            self.largeur = largeur
            self.x = random.randrange(0, self.hauteur)
            self.y = random.randrange(0, self.largeur)
            if len(Jeu.daleks) != 0:
                for i in Jeu.daleks:
                    if i.x == self.x and i.y == self.y:
                        valide = False
                        break
                    else:
                        valide = True
            else:
                valide = True
        self.nbZap = 0 #Pour le niveau 0
    
    def teleportation(self):
        valide = False
        while not valide:
            nouveauX = random.randrange(0,self.largeur)
            nouveauY = random.randrange(0,self.hauteur)
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
                        #deux fois la meme place
        self.x = nouveauX
        self.y = nouveauY        
    
    def deplacementValide(self, nouvellePosX, nouvellePosY):
         if nouvellePosX < 0 or nouvellePosX >= self.largeur:
             return False
         if nouvellePosY < 0 or nouvellePosY >= self.hauteur:
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
            aDelete = []
            for i in jeu.daleks:
                if (abs(i.x - self.x) <= 1) and (abs(i.y - self.y) <=1):
                    aDelete.append(i)
                    #jeu.daleks.remove(i)
                    jeu.points += jeu.nbPointsDalekMort
            if len(aDelete) > 0:
                for i in aDelete:
                    jeu.daleks.remove(i)
            self.nbZap -= 1
            
    def estMort(self, jeu):
        for i in Jeu.daleks:
            if self.x == i.x and self.y == i.y:
                jeu.finPartie = True
        for i in Jeu.tas:
            if self.x == i.x and self.y == i.y:
                jeu.finPartie = True

    

class Tas():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Affichage():
    caseVide = "-" #ce qui sera affiche quand il y a une case vide
    
    def __init__(self, largeur, hauteur, points, niveau):
        self.hauteur = hauteur
        self.largeur = largeur
        self.points = points
        self.niveau = niveau
        self.matriceJeu = []
        for i in range(self.largeur):
            self.matriceJeu.append([])
            for j in range(self.hauteur):
                self.matriceJeu[i].append(self.caseVide)

    
    def clear(self):            # Ca, ca c'est bien. Je t'aime Francois.
        if os.sys.platform == 'win32':
            os.system("cls")
        else:
            os.system('clear')
    
    def actualiserPlateauJeu(self):
        for i in range(self.hauteur):
            for j in range(self.largeur):
                self.matriceJeu[j][i] = self.caseVide #Vide la matrice d'affichage
                
        for i in Jeu.daleks:
            print(i.x, " ", i.y)
            self.matriceJeu[i.x][i.y] = 'X' #Ajoute les daleks dans la matrice d'affichage
            
        for i in Jeu.tas:
            self.matriceJeu[i.x][i.y] = '*' #Ajoute les tas dans la matrice d'affichage
            
        for i in Jeu.docteur:
            self.matriceJeu[i.x][i.y] = '@' #Ajoute le docteur dans la matrice d'affichage
            
    def afficherJeu(self):
        self.clear()
        self.actualiserPlateauJeu()
        for i in range(self.hauteur):
            for j in range(self.largeur):
                print(self.matriceJeu[j][i], end="")
            print()
        print("Points: ", self.points)
        print("Niveau: ", self.niveau)
        for i in Jeu.docteur:
            print("Nombre de zappeur: ", i.nbZap)
            
    def afficherMenu(self):
        print("1. Jouer")
        print("2. Options")
        print("3. Highscores")
        print("4. GTFO")
        
    def afficherOption(self):
        print("1. Changer taille de la planche de jeu")
        print("2. Changer l'icone du docteur")
        print("3. Changer les touches")
        print("4. GTFO")
        
class Controleur():
    def __init__(self): #main-ish..
        self.m = Modele()
        self.a = Affichage(self.m.largeur, self.m.hauteur,0,0)   
        
        repValide = False
        while not repValide:
            self.a.afficherMenu()
            reponse = self.menu()
            if reponse == "1":
                repValide = True
                self.j = Jeu(0,0, self.m.largeur, self.m.hauteur)
        while self.j.finPartie == False:
            print(len(self.j.daleks))
            self.j.changementNiveau()
            while len(self.j.daleks) > 0 and self.j.finPartie == False:
                self.a.afficherJeu()
                touche = input("Touche: ")
                toucheValide = self.toucheValide(touche)
                if  toucheValide == True :
                    #le docteur doit se deplacer avant les daleks !
                    Jeu.docteur[0].deplacement(touche, self.j)
                    self.j.deplaceDaleks()
                    self.j.collisionDaleks()
                    Jeu.docteur[0].estMort(self.j)
                
        self.a.afficherJeu()
        #print(len(j.daleks))
        input("GAME OVER")
        
    def menu(self):
        return input("Votre choix: ")
        
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
   
 
#================================ MAIN===================================================
if __name__ == '__main__':
    c = Controleur()


        
    
