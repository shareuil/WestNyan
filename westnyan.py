# programme principal # 
import tkinter as Tk 
import random

from settings import Settings
from joueur import Joueur
from obstacle import Obstacle
from score import Score
from solnuage import Nuage, Sol


root = Tk.Tk()
root.resizable(width = False, height = False)
root.title("Westnyan")
root.geometry(str(Settings.Fenetre.largeur) + 'x' + str(Settings.Fenetre.hauteur))

canvas = Tk.Canvas(root , width = Settings.Fenetre.largeur , height = Settings.Fenetre.hauteur)
canvas.pack()
imageperdu = -1

# preparation image perdu #
perduImg = Tk.PhotoImage(file=Settings.ImagePerdu.img)
imageperdu = canvas.create_image(Settings.Fenetre.largeur/2, Settings.Fenetre.hauteur/2, image=perduImg)
# creation du fond #
img = Tk.PhotoImage(file=Settings.Fenetre.fond)
fond = canvas.create_image(Settings.Fenetre.largeur/2, Settings.Fenetre.hauteur/2, image=img)

nuages : [Nuage] = []
for i in range(3) :
    nuage = Nuage(Settings.Nuage.images[i], canvas, Settings.Nuage.largeur * i)
    nuages.append (nuage)
sols : [Sol] = []
for i in range(3) :
    sol = Sol(Settings.Sol.images[i], canvas, Settings.Sol.largeur * i)
    sols.append (sol)

# liste de un element car qu'un seul joueur actuellement #
joueurs: [Joueur] = []
for i in range(Settings.Joueur.nombreJoueur):
    joueur = Joueur(i, Settings.Chats.images[i], Settings.Joueur.touches[i], canvas)
    joueurs.append(joueur)

# définit la position du premier obstacle a fin que ca lance le jeu de facon facile #
obstacle1 = Obstacle(Settings.Obstacle.images[0], canvas, Settings.Fenetre.hauteur - Settings.Sol.hauteur - (Settings.Obstacle.hauteur / 2) + 200)
obstacles = [obstacle1]
score = 0
maxScore = max(Settings.Obstacle.frequence / 2, 1)
tuyauApparition = max(Settings.Obstacle.frequenceMin, random.randint(0, Settings.Obstacle.frequence - maxScore))
texteScore = Score(canvas)

def verifColision(obstacle: Obstacle, joueur: Joueur):
    if obstacle.x - (Settings.Obstacle.largeur / 2) < joueur.posHorizontale + (Settings.Joueur.largeurChat / 2) - 10 and obstacle.x + (Settings.Obstacle.largeur / 2) > joueur.posHorizontale - (Settings.Joueur.largeurChat / 2):
        if obstacle.inverse:
            if obstacle.y + (Settings.Obstacle.hauteur / 2) > joueur.posVerticale - (Settings.Joueur.hauteurChat / 2):
                joueur.enVie = False
                joueur.canvas.delete(joueur.chat)
        else:
            if obstacle.y - (Settings.Obstacle.hauteur / 2) < joueur.posVerticale + (Settings.Joueur.hauteurChat / 2):
                joueur.enVie = False
                joueur.canvas.delete(joueur.chat)

def verifPass(obstacle: Obstacle, joueur: Joueur):
    if obstacle.x + (Settings.Obstacle.largeur / 2) < joueur.posHorizontale - (Settings.Joueur.largeurChat / 2):
        return True
    return False

# fonction qui permet au jeu de mettre a jour le score les obstacles et les parametres joueur #
def actualiserJeu():
    root.after(Settings.Fenetre.delaisMiseAJour(), actualiserJeu)
    global obstacles
    global canvas
    global score
    global joueurs
    global tuyauApparition
    global imageperdu
    perdu = True
    for nuage in nuages :
        nuage.deplacement()
        if nuage.x <= 0 - Settings.Nuage.largeur :
            nuage.deplacerVers (2*Settings.Nuage.largeur)
    for sol in sols :
        sol.deplacement()
        if sol.x <= 0 - Settings.Sol.largeur :
            sol.deplacerVers (2*Settings.Sol.largeur)

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
        tuyauApparition = max(Settings.Obstacle.frequenceMin, random.randint(0, Settings.Obstacle.frequence - score * 2))
    else :
        tuyauApparition -= 1

    for sol in sols :
        canvas.lift(sol.sol)

    if perdu == True :
        canvas.lift(imageperdu)
            


    # permer de mettre le score toujours en haut
    canvas.lift(texteScore.label)
    canvas.update_idletasks()
    canvas.update()

    
# permet d'avoir le chat qui bouge en fonction de la touche appuyee #
for joueur in joueurs :
    root.bind(joueur.touche, joueur.saut)

root.after(Settings.Fenetre.delaisMiseAJour(), actualiserJeu)

# ne rien ecrire sous main #
root.mainloop()