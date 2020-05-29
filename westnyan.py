# programme principal # 
import tkinter as Tk 
import random

from settings import Settings
from joueur import Joueur
from obstacle import Obstacle
from score import Score

root = Tk.Tk()
root.resizable(width = False, height = False)
root.title("Westnyan")
root.geometry(str(Settings.Fenetre.largeur) + 'x' + str(Settings.Fenetre.hauteur))

canvas = Tk.Canvas(root, bg = Settings.Fenetre.backgroundColor , width = Settings.Fenetre.largeur , height = Settings.Fenetre.hauteur)
canvas.pack()
# liste de un element car qu'un seul joueur actuellement #
joueur1 = Joueur(1, Settings.Chats.images[0], Settings.toucheJ1, canvas)
joueurs = [joueur1]
# définit la position du premier obstacle a fin que ca lance le jeu de facon facile #
obstacle1 = Obstacle(Settings.Obstacle.images[0], canvas, Settings.Fenetre.hauteur - Settings.Fenetre.hauteurSol - (Settings.Obstacle.hauteur / 2) + 200)
obstacles = [obstacle1]
score = 0
maxScore = max(Settings.Obstacle.frequence / 2, 1)
tuyauApparition = max(Settings.Obstacle.frequenceMin, random.randint(0, Settings.Obstacle.frequence - maxScore))
texteScore = Score(canvas)

def verifColision(obstacle: Obstacle, joueur: Joueur):
    if obstacle.x - (Settings.Obstacle.largeur / 2) < joueur.posHorizontale + (Settings.Joueur.largeurChat / 2) and obstacle.x + (Settings.Obstacle.largeur / 2) > joueur.posHorizontale - (Settings.Joueur.largeurChat / 2):
        if obstacle.inverse:
            if obstacle.y + (Settings.Obstacle.hauteur / 2) > joueur.posVerticale - (Settings.Joueur.hauteurChat / 2):
                joueur.enVie = False
        else:
            if obstacle.y - (Settings.Obstacle.hauteur / 2) < joueur.posVerticale + (Settings.Joueur.hauteurChat / 2):
                joueur.enVie = False

def verifPass(obstacle: Obstacle, joueur: Joueur):
    if obstacle.x + (Settings.Obstacle.largeur / 2) < joueur.posHorizontale - (Settings.Joueur.largeurChat / 2):
        return True
    return False

# fonction qui permet au jeu de mettre a jour le score les obstacles et les parametres joueur #
def actualiserJeu():
    root.after(Settings.Fenetre.delaisMiseAJour(), actualiserJeu)
    global obstacles
    global score
    global joueurs
    global tuyauApparition
    
    perdu = True
    for obstacle in obstacles :
        obstacle.update()
        if obstacle.deleted :
            obstacles.remove(obstacle)
            for joueur in joueurs:
                if joueur.enVie:
                    joueur.score += 1
        else:
            for joueur in joueurs:
                if joueur.enVie:
                    verifColision(obstacle, joueur)
                    if obstacle.passe == False and verifPass(obstacle, joueur):
                        score += 1
                        obstacle.passe = True
    for joueur in joueurs :
        if joueur.enVie:
            joueur.update()
            perdu = False
    if perdu == False:
        texteScore.mettreajour(score)
    if tuyauApparition == 0 :
        tuyau = Obstacle.generateObstacle(score, canvas)
        obstacles.append(tuyau)
        maxScore = max(Settings.Obstacle.frequence / 2, 1)
        tuyauApparition = max(Settings.Obstacle.frequenceMin, random.randint(0, Settings.Obstacle.frequence - maxScore))
        tuyauApparition = max(Settings.Obstacle.frequenceMin, random.randint(0, Settings.Obstacle.frequence - score * 2))
    else :
        tuyauApparition -= 1

    canvas.lift(texteScore.label)
    canvas.update_idletasks()
    canvas.update()

    
# permet d'avoir le chat qui bouge en fonction de la touche appuyee #
for joueur in joueurs :
    root.bind(joueur.touche, joueur.saut)

root.after(Settings.Fenetre.delaisMiseAJour(), actualiserJeu)

# ne rien ecrire sous main #
root.mainloop()