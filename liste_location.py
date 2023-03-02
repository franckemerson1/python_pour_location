'''
    ce programme permet dde calculer la caution, retour sur
    investissement initiale et temps avant 100% retour sur investissement

'''

import os


dest = os.path.abspath(os.path.join(os.getcwd(), "Desktop/projet_immobilier/logiciel_python"))
chemi = os.path.abspath(os.path.join(os.getcwd(), "Desktop/projet_immobilier/logiciel_python"))
chemin = os.path.join(chemi, "loyer.txt")
destination = os.path.join(dest, "tableau.txt")

def immobilier_startup_rent(liste_loyer_mensuel : list):

    caution_a_payer = []
    notre_marge = []
    les_2_premiers_mois = []
    les_10_mois_suivant = []
    revenu_sur_annee = []
    apres_2_premiers_mois = []
    mois_pour_recup_investissement = []
    caution_total_a_payer = 0
    donnees = ["caution", "marge", "revenu_an"]
    liste_dictionnaires = {}
    locataire = []
    caution = 4


    for loyer in liste_loyer_mensuel:
        cautions = loyer * caution
        caution_a_payer.append(cautions)

        marge = int(loyer * (10/100))
        notre_marge.append(marge)

        premiers_mois = int((loyer + marge) * 2)
        les_2_premiers_mois.append(premiers_mois)

        mois_suivant = int(marge * 10)
        les_10_mois_suivant.append(mois_suivant)

    for i in range(len(liste_loyer_mensuel)):
        revenu_annee = int(les_2_premiers_mois[i] + les_10_mois_suivant[i])
        revenu_sur_annee.append(revenu_annee)

        apres_2_mois = int(caution_a_payer[i] - les_2_premiers_mois[i])
        apres_2_premiers_mois.append(apres_2_mois)

        caution_total_a_payer += caution_a_payer[i] #Caution à débouser pour tous les loyers

    for i in range(len(liste_loyer_mensuel)):
        mois_recup_investissement = int(apres_2_premiers_mois[i] / notre_marge[i])
        mois_pour_recup_investissement.append(mois_recup_investissement)

    for i in range(len(liste_loyer_mensuel)):
        liste_dictionnaires = {donnees[0]:caution_a_payer, donnees[1]: notre_marge, donnees[2]: revenu_sur_annee}
    locataire.append(liste_dictionnaires)

    # Ouvrir le fichier en mode écriture
    with open(destination, "w") as f:
    # Imprimer les entêtes
        f.write("caution\tmarge\trevenu_annuel\n")
    # Imprimer les données
        for i in range(len(locataire[0]['caution'])):
            f.write(str(locataire[0]['caution'][i]) + "\t" + str(locataire[0]['marge'][i]) + "\t" + str(locataire[0]['revenu_an'][i]) + "\n")

    

    #print(f"Caution totale: {caution_total_a_payer} frcfa")


def main():
    
    with open(chemin, "r") as f:
    # lire toutes les lignes du fichier et stocker chaque ligne dans une liste
        lignes = f.readlines()
        liste_loyer = []

    for ligne in lignes:
    # utiliser la méthode strip() pour supprimer les caractères de saut de ligne (\n) à la fin de chaque ligne
        chiffres_ligne = [int(chiffre) for chiffre in ligne.strip().split()]
        liste_loyer.extend(chiffres_ligne)
    
    immobilier_startup_rent(liste_loyer)

main()
