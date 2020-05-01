# programme principal # 
import tkinter as Tk 
import random

from settings import Settings
from joueur import Joueur
from obstacle import Obstacle

root = Tk.Tk()
root.resizable(width = False, height = False)
root.title("Westnyan")
root.geometry(str(Settings.Fenetre.largeur) + 'x' + str(Settings.Fenetre.hauteur))

canvas = Tk.Canvas(root, bg = Settings.Fenetre.backgroundColor , width = Settings.Fenetre.largeur , height = Settings.Fenetre.hauteur)
canvas.pack()
# liste de un element car qu'un seul joueur actuellement #
joueur1 = Joueur(1, Settings.Chats.images[0], Settings.toucheJ1, canvas)
joueurs = [joueur1]
obstacle1 = Obstacle(Settings.Obstacle.images[0], canvas, Settings.Fenetre.hauteur - Settings.Fenetre.hauteurSol - (Settings.Obstacle.hauteur / 2) + 200)
obstacles = [obstacle1]
score = 0
maxScore = max(Settings.Obstacle.frequence / 2, 1)
tuyauApparition = max(Settings.Obstacle.frequenceMin, random.randint(0, Settings.Obstacle.frequence - maxScore))

def actualiserJeu():
    root.after(Settings.Fenetre.delaisMiseAJour(), actualiserJeu)
    global obstacles
    global score
    global joueurs
    global tuyauApparition
    
    for obstacle in obstacles :
        obstacle.update()
        if obstacle.deleted :
            obstacles.remove(obstacle)
            score += 1
            print(score)
            for joueur in joueurs:
                joueur.score += 1
    for joueur in joueurs :
        if joueur.enVie:
            joueur.update()
    if tuyauApparition == 0 :
        tuyau = Obstacle.generateObstacle(score, canvas)
        obstacles.append(tuyau)
        maxScore = max(Settings.Obstacle.frequence / 2, 1)
        tuyauApparition = max(Settings.Obstacle.frequenceMin, random.randint(0, Settings.Obstacle.frequence - maxScore))
    else :
        tuyauApparition -= 1

    canvas.update_idletasks()
    canvas.update()
    
#permet d'avoir le chat qui bouge en fonction de la touche appuyee#
for joueur in joueurs :
    root.bind(joueur.touche, joueur.saut)

root.after(Settings.Fenetre.delaisMiseAJour(), actualiserJeu)

#ne rien ecrire sous main
root.mainloop()