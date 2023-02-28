'''
    ce programme permet dde calculer la caution, retour sur
    investissement initiale et temps avant 100% retour sur investissement
'''

def immobilier_startup_rent(liste_loyer_mensuel : list):

    caution_a_payer = []
    notre_marge = []
    les_2_premiers_mois = []
    les_10_mois_suivant = []
    revenu_sur_annee = []
    apres_2_premiers_mois = []
    mois_pour_recup_investissement = []
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

    for i in range(len(liste_loyer_mensuel)):
        mois_recup_investissement = int(apres_2_premiers_mois[i] / notre_marge[i])
        mois_pour_recup_investissement.append(mois_recup_investissement)

    print("Revenu sur un An: {}".format(revenu_sur_annee))
    print("Les cautions à payer: {}".format(caution_a_payer))
    print("Les cautions apres 2 premier mois: {}".format(apres_2_premiers_mois))
    print("Notre marge de 10%: {}".format(notre_marge))
    print("Les 2 premiers mois: {}".format(les_2_premiers_mois))
    print("Les 10 mois suivants: {}".format(les_10_mois_suivant))
    print("Recuperer investissement: {}".format(mois_pour_recup_investissement))

    


def main():
    liste_loyer = []
    for i in range(4):
        liste_loyer.append(int(input("Entrer les différents loyer: ")))
    
    immobilier_startup_rent(liste_loyer)

main()
