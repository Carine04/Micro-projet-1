from random import randint
print ("Bienvenue au Juste prix!")
juste_prix = randint(1, 100)
tentative = int(input("Entrez le nombre d'essaie que vous voulez: "))
nbreTentative = 0
cptEssais = 0
prix_propose =int(input("Entrez une proposition de prix entre 1 et 100: "))
while juste_prix != prix_propose:
    tentative -= 1
    nbreTentative = nbreTentative + 1
    cptEssais = cptEssais + 1
    
    if prix_propose > juste_prix:
        print(f"C'est moins, il vous reste {tentative} tentative(s)")
        prix_propose = int(input("Entrer une proposition de prix entre 1 et 100: " ))
    else:
        print(f"C'est plus, il vous reste {tentative} tentative(s)")
        prix_propose = int(input("Entrer une proposition de prix entre 1 et 100: " ))
    if juste_prix == prix_propose:
       print(f"Félicitation!. Vous avez gagné à la{cptEssais} éme tentative. Le juste prix est {juste_prix}. ")
    if nbreTentative >= tentative:
       print(f"La partie est terminée, vous avez échoué à la {cptEssais} émé tentative! Le juste prix est {juste_prix}")
       exit()







    

