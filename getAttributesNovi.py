import sys
from connections import wcapi

def novi_shop_atributi_fn():
    global novi_shop_atributi
    novi_shop_atributi = (wcapi.get("products/attributes").json())
    print('Novi shop ima:', len(novi_shop_atributi), 'atributa')

    original_stdout = sys.stdout

    with open('wcAtributiNoviTxt.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(novi_shop_atributi)
        sys.stdout = original_stdout # Reset the standard output to its original value

novi_shop_atributi_fn()

# stari_shop_atributi_fn()

# def stari_shop_atributi_terms_fn():
#     print('Pronalazenje svih termsa sa starog shopa')
#     # global stari_shop_atributi_terms
#     stari_shop_atributi_terms = []
#     for atribut in stari_shop_atributi:
#         terms = wcapi2.get(f"products/attributes/{atribut['id']}/terms?per_page=100").json()
#         stari_shop_atributi_terms.append(terms)
#     print('Stari shop ima:', len(stari_shop_atributi_terms), 'termsa')

#     original_stdout = sys.stdout

#     # with open('wcAtributiTermsTxt.txt', 'w') as f:
#     #     sys.stdout = f # Change the standard output to the file we created.
#     #     print(stari_shop_atributi_terms)
#     #     sys.stdout = original_stdout # Reset the standard output to its original value

# stari_shop_atributi_terms_fn()