import sys
from connections import wcapi
# from wcAtributiTxt import stari_shop_atributi

def new_shop_categories_fn():
    global new_shop_categories
    i=1
    nove_kategorije = []

    while i <= 2:
        new_shop_categories = (wcapi.get(f"products/categories?per_page=100&page={i}").json())
        print('Novi shop ima:', len(new_shop_categories), 'kategorija')
        nove_kategorije.append(new_shop_categories)
        i+=1

    original_stdout = sys.stdout

    with open('newWcCategories.py', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(nove_kategorije)
        sys.stdout = original_stdout # Reset the standard output to its original value
        

new_shop_categories_fn()