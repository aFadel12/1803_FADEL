

DonneesVente = [

    ['Date', 'Ville', 'Marque du smartphone', 'Modèle du smartphone', 'Vente max', 'Vente min'],
    ['2022-01-01', 'Toronto', 'Apple', 'iPhone 12', 500, 300],
    ['2022-01-01', 'Toronto', 'Samsung', 'Galaxy S21', 400, 200],
    ['2022-01-01', 'Toronto', 'Google', 'Pixel 6', 300, 150],
    ['2022-01-02', 'Toronto', 'Apple', 'iPhone 12', 480, 270],
    ['2022-01-02', 'Toronto', 'Samsung', 'Galaxy S21', 380, 190],
    ['2022-01-02', 'Toronto', 'Google', 'Pixel 6', 270, 130],
    ['2022-01-03', 'Toronto', 'Apple', 'iPhone 12', 520, 310],
    ['2022-01-03', 'Toronto', 'Samsung', 'Galaxy S21', 420, 210],
    ['2022-01-03', 'Toronto', 'Google', 'Pixel 6', 310, 160],
    ['2022-01-01', 'Montréal', 'Apple', 'iPhone 12', 450, 250],
    ['2022-01-01', 'Montréal', 'Samsung', 'Galaxy S21', 350, 180],
    ['2022-01-01', 'Montréal', 'Google', 'Pixel 6', 250, 120],
    ['2022-01-02', 'Montréal', 'Apple', 'iPhone 12', 420, 240],
    ['2022-01-02', 'Montréal', 'Samsung', 'Galaxy S21', 320, 170],
    ['2022-01-02', 'Montréal', 'Google', 'Pixel 6', 240, 110],
    ['2022-01-03', 'Montréal', 'Apple', 'iPhone 12', 480, 260],
    ['2022-01-03', 'Montréal', 'Samsung', 'Galaxy S21', 380, 200],
    ['2022-01-03', 'Montréal', 'Google', 'Pixel 6', 260, 130],
    ['2022-01-01', 'Vancouver', 'Apple', 'iPhone 12', 550, 320],
    ['2022-01-01', 'Vancouver', 'Samsung', 'Galaxy S21', 420, 230],
    ['2022-01-01', 'Vancouver', 'Google', 'Pixel 6', 320, 170],
    ['2022-01-02', 'Vancouver', 'Apple', 'iPhone 12', 520, 300],
    ['2022-01-02', 'Vancouver', 'Samsung', 'Galaxy S21', 400, 220],
    ['2022-01-02', 'Vancouver', 'Google', 'Pixel 6', 300, 160],
    ['2022-01-03', 'Vancouver', 'Apple', 'iPhone 12', 580, 340],
    ['2022-01-03', 'Vancouver', 'Samsung', 'Galaxy S21', 450, 240],
    ['2022-01-03', 'Vancouver', 'Google', 'Pixel 6', 340, 180],
    ['2022-01-01', 'Calgary', 'Apple', 'iPhone 12', 480, 280],
    ['2022-01-01', 'Calgary', 'Samsung', 'Galaxy S21', 380, 190],
    ['2022-01-01', 'Calgary', 'Google', 'Pixel 6', 280, 140],
    ['2022-01-02', 'Calgary', 'Apple', 'iPhone 12', 450, 260],
    ['2022-01-02', 'Calgary', 'Samsung', 'Galaxy S21', 350, 180],
    ['2022-01-02', 'Calgary', 'Google', 'Pixel 6', 260, 120],
    ['2022-01-03', 'Calgary', 'Apple', 'iPhone 12', 500, 290],
    ['2022-01-03', 'Calgary', 'Samsung', 'Galaxy S21', 400, 210],
    ['2022-01-03', 'Calgary', 'Google', 'Pixel 6', 290, 150]
]

def afficher_tableau(data):
    headers = data[0]
    max_lengths = [max(len(str(row[i])) for row in data) for i in range(len(headers))]
    
   
    for i, header in enumerate(headers):
        print(f"{header:{max_lengths[i]}}", end=" | ")
    print()
    
    
    for length in max_lengths:
        print("-" * length, end=" | ")
    print()
    
   
    for row in data[1:]:
        for i, item in enumerate(row):
            print(f"{item:{max_lengths[i]}}", end=" | ")
        print()



def ftr_vnt_V (tableau,ville):
    print("Date | Ville | Marque du smartphone | Modèle du smartphone | Vente max | Vente min ") 
    for parcours in tableau:
        if parcours[1] == ville:
            print(f"{parcours[0]} | {parcours[1]} | {parcours[3]} | {parcours[4]} | {parcours[5]}")


def ftr_vnt_Mx_Mi(tableau, ville):
    print("Ville | Marque | Vente max | Vente min") 
    for parcours in tableau:
        if parcours[1] == ville:
            print(f"{parcours[1]} | {parcours[2]} | {parcours[4]} | {parcours[5]}")

def ftr_vnt_P(tableau, DteD, DteF):
    print("Date | Ville | Marque | Modèle | Vente max | Vente min") 
    for parcours in tableau:
        if DteD <= parcours[0] <= DteF:
            print(f"{parcours[0]} | {parcours[1]} | {parcours[2]} | {parcours[3]} | {parcours[4]} | {parcours[5]}")
           


def ftr_PM (tableau, ville):
    total_prix = 0
    nb_ventes = 0
    
    for parcours in tableau[1:]: 
        if parcours[1] == ville:  
            prix_moyen_vente = (parcours[4] + parcours[5]) / 2  
            total_prix += prix_moyen_vente  
            nb_ventes += 1  
        
    if nb_ventes == 0:
        print(f"Aucune vente trouvée pour la ville {ville}")
    else:
        prix_moyen = total_prix / nb_ventes
        print(f"Le prix moyen des ventes dans la ville de {ville} est de : {prix_moyen:.2f}")


def sous_programme_1():
    print("Sous-programme 1 en ex�cution...")
    print( "  ")
    ville = input("Entrer le nom d'une des villes du Tableau: ")
    ftr_vnt_V(DonneesVente,ville)

def sous_programme_2():
    print("Sous-programme 2 en ex�cution...")
    print( "  ")
    DteD = input("Entrer une Date de Debut (AAAA-MM-JJ) :"  + ' ')
    print( "  ")
    DteF = input(f"Entrer une Date de Fin (AAAA-MM-JJ) :"+ ' ')
    print( "  ")
    ftr_vnt_P(DonneesVente, DteD ,DteF )
def sous_programme_3():
    print("Sous-programme 3 en ex�cution...")
    print( "  ")
    ville = input("Entrer le nom d'une des villes du Tableau: ")
    ftr_vnt_Mx_Mi(DonneesVente,ville)
def sous_programme_4():
    print("Sous-programme 4 en ex�cution...")
    print( "  ")
    ville = input("Entrer le nom d'une des villes du Tableau: ")
    ftr_PM (DonneesVente,ville)

def sous_programme_5():
    print("Sous-programme 5 en ex�cution...")

def afficher_menu():
    print("\nMenu du programme:")
    print("1. Filtrer les ventes par ville")
    print("2. Filtrer les ventes entre deux dates")
    print("3. Afficher les ventes maximales et minimales par ville")
    print("4. Calculer le prix moyen des ventes dans une ville")
    print("5. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1-5): ")
        
        if choix == '1':
            sous_programme_1()
        elif choix == '2':
            sous_programme_2()
        elif choix == '3':
            sous_programme_3()
        elif choix == '4':
            sous_programme_4()
        elif choix == '5':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")



afficher_tableau(DonneesVente)
main()

