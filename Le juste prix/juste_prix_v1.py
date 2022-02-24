from random import randint
print("Bienvenue au juste prix")
juste_prix = randint(1, 100)
prix_proposé = int(input("Entrer un prix : "))

while juste_prix != prix_proposé:
    if  prix_proposé > juste_prix:
        print("c'est moins")
        prix_proposé = int(input("entrer un prix: "))
    else:
        print("c'est plus")
        prix_proposé = int(input("entrer un prix: " ))
if juste_prix == prix_proposé:
    print("Félicitation! vous avez gagné")
    exit()