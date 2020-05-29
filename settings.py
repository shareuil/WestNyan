import os

# tous les parametres modifiables #
class Settings(object):
    toucheJ1 = "<space>"
    class Chats(object):
        images = ['images/chat1.gif', 'images/cat1.png', 'images/cat1.png']


    class Obstacle (object):
        images = ['images/tuyauBas.png', 'images/tuyauHaut.png']
        vitesseDeplacment = 8
        hauteur = 300
        largeur = 122
        frequence = 60
        frequenceMin = 25

    class Sol (object):
<<<<<<< HEAD
        images = ['images/sol/1b.jpg', 'images/sol/2b.jpg', 'images/sol/3b.jpg']
        positionX = 960
        positionY = 300
        vitesseDeplacment = 8


    class Nuage (object):
        images = ['images/nuage/1b.png', 'images/nuage/2b.png', 'images/nuage/3b.png']
        positionX = 960
        positionY = 300
        vitesseDeplacment = 3

=======
        images = ['images/tuyauBas.png', 'images/tuyauHaut.png']
        vitesseDeplacment = 9
        hauteur = 300
        largeur = 122

    class Nuage (object):
        images = ['images/tuyauBas.png', 'images/tuyauHaut.png']
        vitesseDeplacment = 5
        hauteur = 300
        largeur = 120
>>>>>>> 53e1f9a4bb60cec0989fd325e210b301c1fda7d2

    class Fenetre(object):
        largeur = 960
        hauteur = 720
        images = ['images/fond.jpg']
        hz = 24
        hauteurSol = 160
        # https://docs.quantifiedcode.com/python-anti-patterns/correctness/method_has_no_argument.html
        @staticmethod 
        def delaisMiseAJour ():
            return int(1000 / Settings.Fenetre.hz)

    class Joueur(object):
        positionX = 160
        positionY = 80
        largeurChat = 81
        hauteurChat = 50
        maxImageGif = 12
        vitesseChute = 14

    class Score(object):
        positionX = 160
        positionY = 80
        police = "{Arial} 16"
