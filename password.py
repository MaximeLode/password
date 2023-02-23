import hashlib

mdp = input("Tapez votre mot de passe : ")


def verif_mdp(mdp):
    list_lettres = []
    list_number = []
    nbr_maj, nbr_min, nbr_carspé, nbr_chiffre = 0, 0, 0, 0

    if len(mdp) < 8:
        return "Votre mot de passe doit contenir au moins 8 caractère"

    for i in mdp:
        if 65 <= ord(i) <= 90: 
            list_lettres.append(i)
        elif 97 <= ord(i) <= 122: 
            list_lettres.append(i)
        else:
            list_number.append(i)

    if len(list_lettres) == 0:
        return "Votre mot de passe doit contenir au moins une lettre"

    if len(list_number) == 0:
        return "Votre mot de passe doit contenir au moins un chiffre"

    for j in list_lettres:
        if j.isupper(): 
            nbr_maj += 1 
            if nbr_maj == len(list_lettres): 
                return "Votre mot de passe doit contenir au moins une minuscule"
        if j.islower(): 
            nbr_min += 1 
            if nbr_min == len(list_lettres): 
                return "Votre mot de passe doit contenir au moins une majuscule"


    for k in list_number:
        if k not in ['!', '@', '#', '$', '%', '^', '&', '*']:
            nbr_carspé += 1
            if nbr_carspé == len(list_number):
                return "Votre mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)"
        if k not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            nbr_chiffre += 1
            if nbr_chiffre == len(list_number):
                return "Votre mot de passe doit contenir au moins un chiffre"


result = verif_mdp(mdp)

if result == None:
    print('Mot de pass correct')
else:
    while result != None:
        print(result)
        new_mdp = input("Tapez votre mot de passe : ")
        result = verif_mdp(new_mdp)

    hashlib.sha256(new_mdp.encode()).hexdigest()
    print('Mot de passe correct')
