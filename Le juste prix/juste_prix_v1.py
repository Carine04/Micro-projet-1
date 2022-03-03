from random import randint
print("Bienvenue au juste prix")
juste_prix = randint(1, 100)
prix_propose = int(input("Entrer un prix : "))

while juste_prix != prix_propose:
    if  prix_propose > juste_prix:
        print("c'est moins")
        prix_propose = int(input("entrer un prix: "))
    else:
        print("c'est plus")
        prix_propose = int(input("entrer un prix: " ))
if juste_prix == prix_propose:
    print("Félicitation! vous avez gagné")
    exit()