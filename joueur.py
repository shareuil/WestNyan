import tkinter as tk
from settings import Settings

##creation de personnage##

class Joueur :
    posHorizontale = Settings.Joueur.positionX
    posVerticale = Settings.Joueur.positionY
    indexGif = 0
    saute = False
    frameSaut = 0
    enVie = True
    score = 0

    def __init__(self, id, img, touche, canvas) :
        self.id = id
        self.img = img
        self.touche = touche
        self.frames = [tk.PhotoImage(file=img,format = 'gif -index %i' %(i)) for i in range(Settings.Joueur.maxImageGif)]
        self.chatImg = self.frames[0]
        self.chat = canvas.create_image(self.posHorizontale, self.posVerticale, image=self.frames[0])
        self.canvas = canvas

# fonction qui sert a voir si le chat doit bouger ou non #
    def saut(self, event):
        if self.saute == False :
            self.saute = True
            self.frameSaut = 0
    
# fonction qui utilise la position du chat sans le faire tomber #    
    def monte(self):
        position = self.canvas.coords(self.chat)
        positionY = position[1] - (Settings.Joueur.hauteurChat / 2)
        if positionY < Settings.Joueur.vitesseChute * 1.5:
            self.canvas.move(self.chat, 0, 0 - positionY)
        else :
            self.canvas.move(self.chat, 0, 0 - Settings.Joueur.vitesseChute * 2)

# fonction qui utilise la position du chat pour le faire de tomber avec la vitesseChute, ou fait quil marche sur le sol #
    def tombe(self):
        position = self.canvas.coords(self.chat)
        positionY = position[1] + (Settings.Joueur.hauteurChat / 2)
        yMax = Settings.Fenetre.hauteur - Settings.Fenetre.hauteurSol
        if positionY >= yMax :
            self.canvas.move(self.chat, 0, yMax - positionY)
        else :
            self.canvas.move(self.chat, 0, Settings.Joueur.vitesseChute)
        

    def update(self):
        self.canvas.itemconfigure(self.chat, image=self.frames[int(self.indexGif / 2)])
        if self.saute:
            self.monte()
            self.frameSaut += 1
            if self.frameSaut >= 4:
                self.saute = False
        else :
            self.tombe()    
        self.indexGif += 1
        if self.indexGif >= Settings.Joueur.maxImageGif * 2:
            self.indexGif = 0