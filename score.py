import tkinter as Tk
import random

from settings import Settings

class Score:

    def __init__(self, canvas) :
        self.x = Settings.Score.positionX
        self.y = Settings.Score.positionY
        self.texte = "0"
        self.deleted = False
        self.label = canvas.create_text(self.x, self.y, font=Settings.Score.police, text=self.texte)
        self.canvas = canvas

    def mettreajour(self, score) :   
        self.canvas.itemconfigure(self.label, text=str(score))
