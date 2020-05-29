import tkinter as tk

from settings import Settings

class Sol :

    def __init__(self, img, canvas, y) :
        self.x = Settings.Fenetre.largeur
        self.deleted = False
        self.img = img
        self.imgSol = tk.PhotoImage(file=img)
        self.y = y
        self.sol = canvas.create_image(self.x, self.y, image=self.imgSol)
        self.canvas = canvas
        self.passe = False

    def deplacement (self) :
        self.canvas.move(self.sol, 0 - Settings.Sol.vitesseDeplacment, 0)
        self.x = self.x - Settings.Sol.vitesseDeplacment

#def generateSol(list, canvas):
#if image[0]
#return Obstacle(image, canvas, position + decalage, inverse)

class Nuage :

    def __init__(self, img, canvas, y) :
        self.x = Settings.Fenetre.largeur
        self.deleted = False
        self.img = img
        self.imgNuage = tk.PhotoImage(file=img)
        self.y = y
        self.sol = canvas.create_image(self.x, self.y, image=self.imgNuage)
        self.canvas = canvas
        self.passe = False

    def deplacement (self) :
        self.canvas.move(self.sol, 0 - Settings.Nuage.vitesseDeplacment, 0)
        self.x = self.x - Settings.Nuage.vitesseDeplacment