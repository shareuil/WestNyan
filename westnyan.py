# programme principal # 
import tkinter as Tk 
from settings import Settings
from joueur import Joueur

root = Tk.Tk()
root.resizable(width = False, height = False)
root.title("Westnyan")
root.geometry(str(Settings.Fenetre.largeur) + 'x' + str(Settings.Fenetre.hauteur))

canvas = Tk.Canvas(root, bg = Settings.Fenetre.backgroundColor , width = Settings.Fenetre.largeur , height = Settings.Fenetre.hauteur)
canvas.pack()
# liste de un element car qu'un seul joueur actuellement #
joueur1 = Joueur(1, Settings.Chats.images[0], Settings.toucheJ1, canvas)
joueurs = [joueur1]

#permet d'avoir le chat qui bouge en fonction de la touche appuyee#
def actualiserJeu():
    for joueur in joueurs :
        joueur.update()
    canvas.update_idletasks()
    canvas.update()
    root.after(Settings.Fenetre.delaisMiseAJour(), actualiserJeu)
    for joueur in joueurs :
        root.bind(joueur.touche, joueur.saut)

root.after(Settings.Fenetre.delaisMiseAJour(), actualiserJeu)

#ne rien ecrire sous main
root.mainloop()