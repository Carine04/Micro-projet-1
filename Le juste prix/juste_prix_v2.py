from random import randint
print ("Bienvenue au Juste prix!")
juste_prix = randint(1, 100)
tentative = 10
nbreTentative = 0
prix_proposé =int(input("Entrer une proposition de prix entre 1 et 100: "))
while juste_prix != prix_proposé:
    tentative -= 1
    nbreTentative = nbreTentative + 1
    
    if prix_proposé > juste_prix:
        print(f"C'est mois, il vous reste {tentative} tentation(s)")
        prix_proposé = int(input("Entrer une proposition de prix entre 1 et 100: " ))
    else:
        print(f"C'est plus, il vous reste {tentative} tentation(s)")
        prix_proposé = int(input("Entrer une proposition de prix entre 1 et 100: " ))
    if juste_prix == prix_proposé:
       print(f"Félicitation!. Vous avez gagné à la{nbreTentative} éme tentative. ")
    if nbreTentative > 10:
       print(f"La partie est terminée, vous avez échoué le juste prix est {juste_prix}")
    if tentative == 1:
       print(f"La partie est terminée")
       exit()







    

