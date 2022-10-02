db_name = []
db_phone = []
db_age = []
db_city = []
db_tie = []

while True:
    print("0-quitter le logiciel")
    print("1-écrire dans la base de données")
    print("2-rechercher dans la base de données")
    print("3-modifier la base de données")
    menu = int(input("Votre choix ? : "))
    print()

    if menu == 0:
        choice0 = input("êtes-vous sûr de vouloir quitter le logiciel [Y/n]? ")
        if choice0 == "y":
            quit()
        elif choice0 == "Y":
            quit()
        print()

    elif menu == 1:

        name = input("nom : ")
        phone = input("téléphone : ")
        age = input("âge : ")
        city = input("ville habitée : ")
        tie = input("lien avec cette personne : ")

        db_name.append(name)
        db_phone.append(phone)
        db_age.append(age)
        db_city.append(city)
        db_tie.append(tie)

        print()
        print("vous avez bien enregistrer cette personne dans la base de données")
        print()

    elif menu == 2:
        if not db_name:
            print("(la base de données est vide)")
            print()
        else:
            print("nom présents dans la base de données : ", ','.join(db_name))
            search = input("Entrer un nom : ")

            if search in db_name:
                nb = db_name.index(search)
                print("le numéro de téléphone de ", search, " est : ", db_phone[nb])
                print("l'age de ", search, " est : ", db_age[nb])
                print("la ville de ", search, " est : ", db_city[nb])
                print("le type de lien avec ", search, " est : ", db_tie[nb])
                print()

            else:
                print(search, " n'est pas dans la base de données, réessayez ...")
                print()

    elif menu == 3:
        if not db_name:
            print("(la base de données est vide)")
            print()
        else:
            print("nom présents dans la base de données : ", ','.join(db_name))
            search2 = input("Quelle personne voulez-vous modifier dans la base de données ? ")
            print()

            if search2 in db_name:
                print("0-revenir au menu principal")
                print("1-Supprimer ", search2, " de la base de données")
                print("2-modifier ", search2, " de la base de données")
                choice = int(input("Votre choix ? : "))
                nb = db_name.index(search2)

                if choice == 0:
                    menu = 0

                elif choice == 1:
                    del db_name[nb]
                    print(search2, " a bien été supprimé de la base de données")
                    print()

                elif choice == 2:
                    name = input("nom : ")
                    phone = input("téléphone : ")
                    age = input("âge : ")
                    city = input("ville habitée : ")
                    tie = input("lien avec cette personne : ")

                    db_name[nb] = name
                    db_phone[nb] = phone
                    db_age[nb] = age
                    db_city[nb] = city
                    db_tie[nb] = tie
                    print()
                    print("vous avez bien enregistrer cette personne dans la base de données")
                    print()

                else:
                    print("erreur de syntaxe, veuillez réessayer")
                    print()
            else:
                print(search2, " n'est pas dans la base de données, réessayez ...")
                print()

    else:
        print("erreur de syntaxe, veuillez réessayer")
        print()
