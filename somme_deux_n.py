import random
def somme_de_deux_nombres():
    score = 0
    response = True
    while response:
        aa = random.randint(0, 15)
        bb = random.randint(0, 15)
        
        s = int(input("Somme des deux nombres ({aa} et {bb}) générés aléatoirement ? ".format(aa = aa, bb = bb)))
        vraie_somme = aa + bb
        if s == vraie_somme:
            score += 1000
            print("Votre score actuel : ", score)
        else:
            response = False
            print("")
            print("RESULTAT :")
            break
    print("Votre score final est  : ", score)
    print("FIN DU PROGRAMME")
somme_de_deux_nombres()