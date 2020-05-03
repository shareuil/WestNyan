import tkinter as tk
import random

from settings import Settings

class Obstacle :


    def __init__(self, img, canvas, y) :
        self.x = Settings.Fenetre.largeur
        self.deleted = False
        self.img = img
        self.imgObstacle = tk.PhotoImage(file=img)
        self.y = y
        self.obstacle = canvas.create_image(self.x, self.y, image=self.imgObstacle)
        self.canvas = canvas

    def deplacement (self) :
        self.canvas.move(self.obstacle, 0 - Settings.Obstacle.vitesseDeplacment, 0)
        self.x = self.x - Settings.Obstacle.vitesseDeplacment

    def update(self):
        if self.deleted == False :
            self.deplacement()
            if self.x < 0 :
                self.deleted = True
                self.canvas.delete(self.obstacle)

# En fonction du score, le nombre de tuyau qui apparait augmente, et le sens inversé aussi #
    @staticmethod 
    def generateObstacle(score, canvas):
        randomInverse = random.randint(0, 100)
        maxScore = min(score * 10, 50)
        inverse = True if maxScore > randomInverse else False
        randomDecalage = random.randint(0, 100)
        decalage = randomDecalage if inverse == False else 0 - randomDecalage

        image = Settings.Obstacle.images[1] if inverse else Settings.Obstacle.images[0]
        position = 0 + Settings.Obstacle.hauteur / 2 if inverse else Settings.Fenetre.hauteur - Settings.Fenetre.hauteurSol - Settings.Obstacle.hauteur / 2

        return Obstacle(image, canvas, position + decalage)

