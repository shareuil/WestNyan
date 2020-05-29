import tkinter as tk

from settings import Settings

class Sol :

    def __init__(self, img, canvas, x) :
        self.x = x + (Settings.Sol.largeur / 2)
        self.imgSol = tk.PhotoImage(file=img)
        self.y = Settings.Fenetre.hauteur - Settings.Sol.hauteur + + (Settings.Sol.hauteur / 2)
        self.sol = canvas.create_image(self.x, self.y, image=self.imgSol)
        self.canvas = canvas

    def deplacement (self) :
        self.canvas.move(self.sol, 0 - Settings.Sol.vitesseDeplacment, 0)
        self.x = self.x - Settings.Sol.vitesseDeplacment

    def deplacerVers(self, x):
        self.canvas.move(self.sol, x - self.x, 0)
        self.x = x

#def generateSol(list, canvas):
#if image[0]
#return Obstacle(image, canvas, position + decalage, inverse)

class Nuage :

    def __init__(self, img, canvas, x) :
        self.x = x + (Settings.Nuage.largeur / 2)
        self.y = (Settings.Fenetre.hauteur - Settings.Nuage.hauteur) + (Settings.Nuage.hauteur / 2)
        self.img = img
        self.imgNuage = tk.PhotoImage(file=img)
        self.nuage = canvas.create_image(self.x, self.y, image=self.imgNuage)
        self.canvas = canvas

    def deplacement (self) :
        self.canvas.move(self.nuage, 0 - Settings.Nuage.vitesseDeplacment, 0)
        self.x = self.x - Settings.Nuage.vitesseDeplacment

    def deplacerVers(self, x):
        self.canvas.move(self.nuage, x - self.x, 0)
        self.x = x
