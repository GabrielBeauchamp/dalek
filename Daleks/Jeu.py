import random
import os
from tkinter import *

class VueTkinter():
    def __init__(self, parent):
        self.iconeDocteur = "@"
        #self.caseVide = "-"
        self.espacePixel = 20
        self.parent = parent
        self.matriceJeu = []
        for i in range(self.parent.getLargeur()):
            self.matriceJeu.append([])
            for j in range(self.parent.getHauteur()):
                self.matriceJeu[i].append("")

        self.root = Tk()
        self.root.title("Dalek qui est le fun quand on y joue avec nos culculatrices")
        self.canevas = Canvas(self.root, height=self.parent.getHauteur() * self.espacePixel, width=self.parent.getLargeur() * self.espacePixel, bg ="white")
        self.canevas.pack()
        self.actualiserPlateauJeu()
        self.dessinerGrille()
        self.afficherJeu()
        
    def actualiserPlateauJeu(self):
        for i in range(self.parent.getHauteur()):
            for j in range(self.parent.getLargeur()):
                self.matriceJeu[j][i] = "" #Vide la matrice d'affichage
                
        for i in self.parent.getDaleks():
            #print("daleks ", i.x, " ", i.y)
            self.matriceJeu[i.x][i.y] = 'X'  #Ajoute les daleks dans la matrice d'affichage
            
        for i in self.parent.getTas():
            #print("tas ", i.x, " ", i.y)
            self.matriceJeu[i.x][i.y] = '*' #Ajoute les tas dans la matrice d'affichage
            
        for i in self.parent.getDocteur():
            #print("docteur ", i.x, " ", i.y)
            self.matriceJeu[i.x][i.y] = self.iconeDocteur #Ajoute le docteur dans la matrice d'affichage
    
    def dessinerGrille(self):
        for i in range(self.parent.getLargeur()):
            self.canevas.create_line(i*self.espacePixel,0,i*self.espacePixel,self.parent.getHauteur() * self.espacePixel)
        for i in range(self.parent.getHauteur()):
            self.canevas.create_line(0, i*self.espacePixel,self.parent.getLargeur() * self.espacePixel,i*self.espacePixel)
            
    def afficherJeu(self):
         for i in range(self.parent.getHauteur()):
            for j in range(self.parent.getLargeur()):
                self.canevas.create_text(j*self.espacePixel+self.espacePixel/2, i*self.espacePixel+self.espacePixel/2, text= self.matriceJeu[j][i])
                
class VueConsole():
    iconeDocteur = "@"
    caseVide = "-" * len(iconeDocteur) #ce qui sera affiche quand il y a une case vide
    
    def __init__(self, parent):
        self.parent = parent
        self.matriceJeu = []

        for i in range(self.parent.getLargeur()):
            self.matriceJeu.append([])
            for j in range(self.parent.getHauteur()):
                self.matriceJeu[i].append(self.caseVide)
   
    def clear(self):
        for i in range(255):
            print()
    
    def clearOs(self):            # Ca, ca c'est bien. Je t'aime Francois.
        if os.sys.platform == 'win32':
            os.system("cls")
        else:
            os.system('clear')
    
    def actualiserPlateauJeu(self):
        for i in range(self.parent.getHauteur()):
            for j in range(self.parent.getLargeur()):
                self.matriceJeu[j][i] = self.caseVide #Vide la matrice d'affichage
                
        for i in self.parent.getDaleks():
            #print("daleks ", i.x, " ", i.y)
            self.matriceJeu[i.x][i.y] = 'X' #Ajoute les daleks dans la matrice d'affichage
            
        for i in self.parent.getTas():
            #print("tas ", i.x, " ", i.y)
            self.matriceJeu[i.x][i.y] = '*' #Ajoute les tas dans la matrice d'affichage
            
        for i in self.parent.getDocteur():
            #print("docteur ", i.x, " ", i.y)
            self.matriceJeu[i.x][i.y] = self.iconeDocteur #Ajoute le docteur dans la matrice d'affichage
            
    def afficherJeu(self):
        self.clear()
        self.actualiserPlateauJeu()
        for i in range(self.parent.getHauteur()):
            for j in range(self.parent.getLargeur()):
                print(self.matriceJeu[j][i], end="")
            print()
        print("Points: ", self.parent.getPoints())
        print("Niveau: ", self.parent.getNiveau())
        for i in self.parent.getDocteur():
            print("Nombre de zappeur: ", i.nbZap)
            
    def afficherMenu(self):
        print("1. Jouer")
        print("2. Options")
        print("3. Highscores")
        print("4. GTFO")
        
    def afficherOption(self):
        self.clear()
        print("1. Changer taille de la planche de jeu")
        print("2. Changer l'icone du docteur")
        print("3. Changer les touches")
        print("4. GTFO")
        
    def afficherHighscore(self,highscore):  
        self.clear()
        print("Meilleurs joueurs")
        print("----")
        if len(highscore) > 0 :
            for i in highscore:
                print(highscore.index(i)+ 1,". Nom:", i[0], " Points:", i[1])
        else:
            print("Il n'y a aucun score !")
        return input("Appuyer sur une touche pour retourner au menu...")
            
    def getTouche(self):
        return input("Touche: ")
        
    def getChoix(self):
        return input("Votre choix: ")
        
    def nouvelleLargeur(self):
        return input("Nouvelle largeur: ")
    
    def nouvelleHauteur(self):
        return input("Nouvelle hauteur: ")
    
    def changerIcone(self):
        print("Nous vous deconseillons X, -, et *")
        print("Votre avatar present est: ", self.iconeDocteur)
        self.iconeDocteur = input("Quel sera votre nouvel avatar? ")  
        self.caseVide = self.caseVide + "-" * len(self.iconeDocteur)
    
    def finJeu(self):
        print("Vous etes mort.\nVotre score est de: ", self.parent.getPoints())
        nom = input("Votre nom : ")
        input("Appuyer sur une touche pour retourner au menu...")
        return [nom, self.parent.getPoints()]
    
class Modele():
   # highscore = {}
    highscore = []
    def __init__(self, parent):
        self.hauteur = 20
        self.largeur = 30
        self.parent = parent
    
    #options
    def changerTaille(self, largeur, hauteur):
        if (largeur < 100 and hauteur < 100) and (largeur > 5 and hauteur > 5):
            self.hauteur = hauteur
            self.largeur = largeur
    
    def lancerJeu(self):
        self.j = Jeu(self)
    
    def changerNiveau(self):
        self.j.changementNiveau()
        
    def nouveauScore(self, infoScore):
        self.highscore.append(infoScore)
        self.highscore.sort(key=lambda highscore: highscore[1], reverse=True)
        self.sauvegarderHighscore()
    
    def ouvrirHighscore(self):
        try:
            fichierHighscore = open("score.txt", 'r')
            self.highscore = [] #Pour etre sur d'avoir seulement les socres du fichier
            for line in fichierHighscore:
                self.highscore.append(line.split(','))
            for i in self.highscore:
                i[1] = int(i[1])
            fichierHighscore.close()
        except:
            pass
    
    def sauvegarderHighscore(self):
       # for key, value in self.highscore.items():
       #     print(key, " ", value)
        fichierHighscore = open("score.txt", 'w')
        for i in self.highscore:
            fichierHighscore.write((str(i[0]) + ","+ str(i[1])+ "\n"))
        fichierHighscore.close()
    
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
    def __init__(self, parent):
        self.finPartie = False
        self.tas = []
        self.debutNiveau(0,0)
        self.hauteur = parent.hauteur
        self.largeur = parent.largeur
        self.docteur = []
        self.docteur.append(Docteur(self))
        self.parent = parent
    
    def debutNiveau(self,niveau, points):
        self.daleks = []
        self.niveau = niveau
        self.nbDaleks = self.nbDalekInc * niveau
        self.points = points
        for i in range(self.nbDaleks):
            self.daleks.append(Dalek(self))
    
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
    def __init__(self, parent):
        self.parent = parent
        valide = False
        while not valide:
            self.x = random.randrange(0, self.parent.largeur)
            self.y = random.randrange(0, self.parent.hauteur)
            if len(self.parent.daleks) != 0:
                for i in self.parent.daleks:
                    if i.x == self.x and i.y == self.y:
                        valide = False
                        break
                    else:
                        valide = True
            else:
                valide = True
    
    def deplacement(self):
        for j in self.parent.docteur:
            if self.x > j.x:
                self.x = self.x - 1
            if self.x < j.x:
                self.x = self.x + 1
            if self.y > j.y:
                self.y = self.y - 1
            if self.y < j.y:
                self.y = self.y + 1
                
    def collision(self):
        for i in self.parent.daleks:
            if self is i:
                pass
            else:
                if self.x == i.x and self.y == i.y:
                    t = Tas(self.x,self.y)
                    self.parent.tas.append(t)
                    return True
        for i in self.parent.tas:
            if self.x == i.x and self.y == i.y:
                return True

class Docteur():
    def __init__(self, parent):
        #self.estMort = False
        self.parent = parent
        valide = False
        while not valide:
            self.x = random.randrange(0, self.parent.largeur)
            self.y = random.randrange(0, self.parent.hauteur)
            if len(self.parent.daleks) != 0:
                for i in self.parent.daleks:
                    if i.x == self.x and i.y == self.y:
                        valide = False
                        break
                    else:
                        valide = True
            else:
                valide = True
        self.nbZap = 0 #Pour le niveau 0
    
    def teleportation(self):
        nb = 0
        valide = False
        while not valide:
            if nb > (self.parent.largeur * self.parent.hauteur * 2):
                return
            nouveauX = random.randrange(0, self.parent.largeur)
            nouveauY = random.randrange(0, self.parent.hauteur)
            for i in self.parent.daleks:
                if abs(i.x - nouveauX) <= 1 and abs(i.y - nouveauY) <= 1:
                    valide = False
                    nb = nb + 1
                    break
                else:
                    valide = True
            if valide == True:
                for i in self.parent.tas:
                    if i.x == nouveauX and i.y == nouveauY:
                        valide = False
                        nb = nb + 1
                        break;
                    else:
                        valide = True
                            #deux fois la meme place
        
        self.x = nouveauX
        self.y = nouveauY        
    
    def deplacementValide(self, nouvellePosX, nouvellePosY):
         if nouvellePosX < 0 or nouvellePosX >= self.parent.largeur:
             return False
         if nouvellePosY < 0 or nouvellePosY >= self.parent.hauteur:
             return False
         for i in self.parent.tas:
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
        elif direction == "t":    # teleportage
            self.teleportation()
        elif direction == "z":    # zappeur
            self.zapper()
    
    def zapper(self):
        if(self.nbZap > 0):
            aDelete = []
            for i in self.parent.daleks:
                if (abs(i.x - self.x) <= 1) and (abs(i.y - self.y) <=1):
                    aDelete.append(i)
                    #jeu.daleks.remove(i)
                    self.parent.points += self.parent.nbPointsDalekMort
            if len(aDelete) > 0:
                for i in aDelete:
                    self.parent.daleks.remove(i)
            self.nbZap -= 1
            
    def estMort(self):
        for i in self.parent.daleks:
            if self.x == i.x and self.y == i.y:
                self.parent.finPartie = True
        for i in self.parent.tas:
            if self.x == i.x and self.y == i.y:
                self.parent.finPartie = True

class Tas():
    def __init__(self,x,y):
        self.x = x
        self.y = y
       
class Controleur():
    def __init__(self, type): #main-ish..
        self.m = Modele(self)
        if type == "c":
            self.a = VueConsole(self)
            self.console()
        else:
            self.graphique()
            

    def console(self):
        self.jouer()
       
    def graphique(self):
        self.m.lancerJeu()
        self.m.changerNiveau()
        self.a = VueTkinter(self)
        self.a.root.mainloop() 

    
    def jouer(self):
        while True:
            self.menu()     
            self.partie()
                              
            self.a.afficherJeu()
            #print(len(j.daleks))
            infoScore = self.a.finJeu()
            self.m.nouveauScore(infoScore)
            

    def menu(self):
        repValide = False
        while not repValide:
            self.a.clear()
            self.m.ouvrirHighscore()
            self.a.afficherMenu()
            reponse = self.a.getChoix()
            if reponse == "1":
                repValide = True
                self.m.lancerJeu()
            elif reponse == "2":
                self.option()
            elif reponse == "3":
                #self.m.sauvegarderHighscore()
                self.a.afficherHighscore(self.m.highscore)
            elif reponse == "4":
                self.m.quitter()
                
    def option(self):
        self.a.afficherOption()
        repValide = False
        while not repValide:
            reponse = self.a.getChoix()
            if reponse == "1":
                repValide = True
                try:
                    self.m.changerTaille(int(self.a.nouvelleLargeur()), int(self.a.nouvelleHauteur()))
                except :
                    pass
                
            elif reponse == "2":
                repValide = True
                self.a.changerIcone()
            elif reponse == "3":
                repValide = True
                print("Peut-etre plus tard, si z'etes chanceux et gentils.")
            elif reponse == "4":
                return
    
    def partie(self):
        while self.m.j.finPartie == False:
            print(len(self.m.j.daleks))
            self.m.changerNiveau()
            while len(self.m.j.daleks) > 0 and self.m.j.finPartie == False:
                self.a.afficherJeu()
                touche = self.a.getTouche()
                toucheValide = self.toucheValide(touche)
                if  toucheValide == True :
                    #le docteur doit se deplacer avant les daleks !
                    self.m.j.docteur[0].deplacement(touche)
                    self.m.j.deplaceDaleks()
                    self.m.j.collisionDaleks()
                    self.m.j.docteur[0].estMort()
                        
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
   
    def getLargeur(self):
        return self.m.largeur
    def getHauteur(self):
       return self.m.hauteur
    def getPoints(self):
       return self.m.j.points
    def getNiveau(self):
       return self.m.j.niveau
    def getDaleks(self):
       return self.m.j.daleks
    def getDocteur(self):
       return self.m.j.docteur
    def getTas(self):
       return self.m.j.tas

#================================ MAIN===================================================
if __name__ == '__main__':
   # t = input("[c]onsole ou [g]raphique")
    c = Controleur("c")


        
    
