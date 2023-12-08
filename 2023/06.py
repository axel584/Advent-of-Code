import pytest






def enigme_day06(chemin):
    all_time = []
    all_distance = []
    all_nb_victoires = []
    print("chemin",chemin)
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            print(ligne)
            if ligne.startswith("Time:"):
                all_time = [int(i) for i in ligne[ligne.find(':')+1:].split()]
            if ligne.startswith("Distance:"):
                all_distance = [int(i) for i in ligne[ligne.find(':')+1:].split()]
    print(all_time)
    print(all_distance)
    for indice,time in enumerate(all_time):
        nb_victoires = 0
        for vitesse_possible in range(time):
            temps_restant = time-vitesse_possible
            distance_effectuee = vitesse_possible * temps_restant
            if distance_effectuee>all_distance[indice]:
                nb_victoires += 1
        all_nb_victoires.append(nb_victoires)
    somme = 1
    for victoire in all_nb_victoires : 
        somme *= victoire
    return somme

def enigme_day06_second_part(chemin):
    all_time = []
    all_distance = []
    all_nb_victoires = []
    print("chemin",chemin)
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            print(ligne)
            if ligne.startswith("Time:"):
                all_time.append(int(ligne[ligne.find(':')+1:].replace(' ','')))
            if ligne.startswith("Distance:"):
                all_distance.append(int(ligne[ligne.find(':')+1:].replace(' ','')))
    print(all_time)
    print(all_distance)
    for indice,time in enumerate(all_time):
        #print("indice / time : ",indice,time)
        nb_victoires = 0
        for vitesse_possible in range(time):
            temps_restant = time-vitesse_possible
            distance_effectuee = vitesse_possible * temps_restant
            #print("vitesse_possible / distance_effectuee : ",vitesse_possible,distance_effectuee)
            if distance_effectuee>all_distance[indice]:
                nb_victoires += 1
        all_nb_victoires.append(nb_victoires)
    print(all_nb_victoires)    
    somme = 1
    for victoire in all_nb_victoires : 
        somme *= victoire
    print(somme)
    return somme        



def test_enigme_day06():
    assert enigme_day06("input-06a-test.txt") == 288

def test_enigme_day05_second_part():
    assert enigme_day06_second_part("input-06a-test.txt") == 71503
    pass

if __name__ == "__main__" :
    print(enigme_day06_second_part("input-06.txt"))