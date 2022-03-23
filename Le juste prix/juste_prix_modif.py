from random import randint

print(" Bienvenue au Juste prix ")
print("")
print("choisissez un mode de difficulté parmi ces modes :",
  " Le mode facile où le joueur devra deviner le juste prix tiré aléatoirement entre 1 et 100 sans limite d’essais",
  " Le mode normal où le joueur devra deviner le juste prix tiré aléatoirement entre 1 et 100 en 10 essais ou moins",
  " Le mode personnalisé où le joueur pourra choisir quel sera le prix maximal possible (le prix minimal reste de 1) et où le joueur pourra décider du nombre d’essais dont il disposera pour trouver le juste prix (S’il sélectionne 0, il aura un nombre illimité d’essais)",sep="\n")
print("")
mode=str(input("Entrez la lettre f(Le mode facile), n(Le mode normal) ou p(Le mode personnalisé)): "))

if mode=="f":
    
 juste_prix = randint(1, 100)
 prix_propose = int(input("Entrez un prix : "))

 while juste_prix != prix_propose:
    if  prix_propose > juste_prix:
        print("C'est moins")
        prix_propose = int(input("Entrez un prix: "))
    else:
        print("C'est plus")
        prix_propose = int(input("Entrez un prix: " ))
 if juste_prix == prix_propose:
    print("Félicitation! Vous avez gagné")
    exit()

if mode=="n":
   juste_prix = randint(1, 100)
   tentative = 9
   nbreTentative = 0
   cptEssais = 1
   prix_propose =int(input("Entrez une proposition de prix entre 1 et 100: "))
   while juste_prix != prix_propose:
    tentative -= 1
    nbreTentative = nbreTentative + 1
    cptEssais = cptEssais + 1
    
    if prix_propose > juste_prix:
        print(f"C'est mois, il vous reste {tentative} tentative(s)")
        prix_propose = int(input("Entrer une proposition de prix entre 1 et 100: " ))
    else:
        print(f"C'est plus, il vous reste {tentative} tentative(s)")
        prix_propose = int(input("Entrer une proposition de prix entre 1 et 100: " ))
    if juste_prix == prix_propose:
       print(f"Félicitation!. Vous avez gagné à la {cptEssais} éme tentative. Le juste prix est {juste_prix}. ")
    if nbreTentative >= 10:
       print(f"La partie est terminée, vous avez échoué à la {cptEssais} éme tentative! Le juste prix est {juste_prix}")
       exit()
if mode=="p":
        mini = int(input("Entrez le prix minimum:\n "))
        max = int(input("Entrez le prix maximum: \n"))
        nbre_essais = int(input(f"Entrez le nombre d'essais que vous voulez entre {mini} et {max}:\n "))
        prix_propose = int(input(f"Entrer un nombre entre {mini} et {max} :\n "))
        juste_prix = randint(mini, max)
        tentative = 1
        while juste_prix != prix_propose :

            if juste_prix < prix_propose:
                print("c'est moin ")
                prix = int(input(f"Entre un nombre entre {mini} et {max} : "))

            elif juste_prix > prix_propose:
                print("c'est plus ")
                prix_propose = int(input(f"Entre un nombre entre {mini} et {max} : "))

            if nbre_essais != 0:
                tentative += 1
                print(f"Vous avez utiliser {tentative} essai sur {nbre_essais}")
        else:
            if juste_prix != prix_propose:
                print(f"La partie est terminée, vous avez échoué! Le juste prix est ({juste_prix})")

            else:
                if nbre_essais != 0:
                    print (f"Félicitation!. Vous avez gagné, le juste prix est {juste_prix} ,vous avez trouvé aprés {tentative} tentative d 'essai .")
                    exit()