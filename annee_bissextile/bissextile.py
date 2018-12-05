years = input("Saisissez une année : ")
try:
    years = int(years)
except:
    print("Erreur lors de la conversion de l'année.")
if years % 400 == 0 or (years % 4 == 0 and years % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
