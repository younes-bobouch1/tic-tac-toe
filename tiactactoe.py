tableau = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
"-------------------------------------------------------------------------------"
leJoueur = "X"
gagnant = None
jeu = True
"-------------------------------------------------------------------------------"


def printTableau(tableau):
    print(tableau[0] + " |", tableau[1] + " |", tableau[2])
    print("__________")
    print(tableau[3] + " |", tableau[4] + " |", tableau[5])
    print("__________")
    print(tableau[6] + " |", tableau[7] + " |", tableau[8])


"-------------------------------------------------------------------------------"


def inputJoueur(tableau):
    case = int(input("Choix d'un chiffre entre 1 et 9 : "))
    if case >= 1 and case <= 9 and tableau[-1] == "-":
        tableau[case - 1] = leJoueur
    else:
        print("Erreur")


"-------------------------------------------------------------------------------"


def resultatHor(tableau):
    global gagnant
    if tableau[0] == tableau[1] == tableau[2] and tableau[1] != "-":
        gagnant = tableau[0]
        return True
    elif tableau[3] == tableau[4] == tableau[5] and tableau[4] != "-":
        gagnant = tableau[3]
        return True
    elif tableau[6] == tableau[7] == tableau[8] and tableau[7] != "-":
        gagnant = tableau[6]
        return True


def resultatVer(tableau):
    global gagnant
    if tableau[0] == tableau[3] == tableau[6] and tableau[3] != "-":
        gagnant = tableau[0]
        return True
    elif tableau[1] == tableau[4] == tableau[7] and tableau[4] != "-":
        gagnant = tableau[1]
        return True
    elif tableau[2] == tableau[5] == tableau[8] and tableau[5] != "-":
        gagnant = tableau[2]
        return True


def resultatDiag(tableau):
    global gagnant
    if tableau[0] == tableau[4] == tableau[8] and tableau[4] != "-":
        gagnant = tableau[0]
        return True
    elif tableau[2] == tableau[4] == tableau[6] and tableau[4] != "-":
        gagnant = tableau[2]
        return True


"-------------------------------------------------------------------------------"


def matchEgal(tableau):
    global jeu
    if "-" not in tableau:
        printTableau(tableau)
        print("Match nul")
        jeu = False


"-------------------------------------------------------------------------------"


def changeJoueur():
    global leJoueur
    if leJoueur == "X":
        leJoueur = "O"
    else:
        leJoueur = "X"


"-------------------------------------------------------------------------------"


def resultatGagne():
    if resultatHor(tableau) or resultatVer(tableau) or resultatDiag(tableau):
        print(f"Gagnant : {gagnant}")


"-------------------------------------------------------------------------------"
while jeu:
    printTableau(tableau)
    inputJoueur(tableau)
    resultatGagne()
    changeJoueur()