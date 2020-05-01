import os
# tous les parametres modifiables #
class Settings(object):
    toucheJ1 = "<space>"
    class Chats(object):
        images = ['images/chat1.gif', 'images/cat1.png', 'images/cat1.png']

    class Fenetre(object):
        largeur = 480
        hauteur = 360
        backgroundColor = "blue"
        hz = 60
        def delaisMiseAJour ():
            return int(1000 / Settings.Fenetre.hz)

    class Joueur(object):
        positionX = 80
        positionY = 0
        largeurChat = 81
        hauteurChat = 50
        maxImageGif = 12
        vitesseChute = 3

