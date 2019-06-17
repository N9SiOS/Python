import os
from random import randrange
from math import ceil

money = 1000 # Argent de départ
continue_partie = True # Boolean indiquant VRAI tant que l'on doit contiuer la partie

print("Bienvenue à la Roulette ! vous avez actuelment ", money, " $. ")

while continue_partie:
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Choisissez le nombre sur lequel vous souhaiter miser (entre 0 et 49)")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print(" Vous n'avez pas saisie de nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Ce nombre est négatif !")
        if nombre_mise > 49:
            print(" Ce nombre est supèrieur  à 49 .")
    mise = 0
    while mise <= 0 or mise > money:
        mise = input("Mainteant choisissez votre mise ?  argent en banque : ", money, " $ ")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisie de nombre !")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie n'est pas valable !")
        if mise >money:
            print("Vous ne pouvez pas miser autant il vous reste ", money, "$ en banque")
nombre_gagnant = randrange(50)
print("La roulette tourne ! ... .. et ... s'arrete sur le numéro ", nombre_gagnant, " ! ")
if nombre_gagnant == nombre_mise:
    print("Félicitation vous obtenez ", mise * 3, " $! ")
    money += mise * 3
elif nombre_gagnant % 2 == nombre_mise % 2:
    mise = ceil(mise * 0.5)
    print("Vous avez miser sur la bonne couleur vous obtenez ", mise, "$ ")
else:
    print("Désoler vous perdez votre mise :/ ", mise)
    money -= mise
if money <= 0:
    print(" Vous êtes ruiné ! -> GAME OVER <- ")
    continue_partie = False
else:
    print(" Vous avez a présent ", money, "$ ")
    quit = input("Souhaitez-vous quitter o/n ?")
    if quit == "o" or quit == "O":
        print("Fin de partie avec un total en banque de ", money, "$ .")
        continue_partie = False
