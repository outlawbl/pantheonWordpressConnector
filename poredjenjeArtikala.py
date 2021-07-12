from pantheonArtikli import pantheon_artikli, id_pantheon_artikala
from woocommerceArtikli import wc_artikli_za_poredjenje, id_woocommerce_artikala, woocommerce_artikli
from jsondiff import diff
import sys

##################################################################################################################
# Woocommerce artikli za poredjenje
##################################################################################################################

wca = []
for id in id_pantheon_artikala:
    x = list(filter(lambda x: x['sku'] == id, wc_artikli_za_poredjenje))
    wca.append(x)
print(len(id_pantheon_artikala), 'id_pantheon_artikala')

wc_artikli_za_poredjenje_sa_pantheonom = []
for lista in wca:
    for item in lista:
        wc_artikli_za_poredjenje_sa_pantheonom.append(item)

kljucevi = ['sku', 'regular_price', 'stock_quantity', 'name']
novi_wc_artikli_za_poredjenje = []

for artikal in wc_artikli_za_poredjenje_sa_pantheonom:
    newdict = {k: artikal[k] for k in kljucevi}
    novi_wc_artikli_za_poredjenje.append(newdict)

print('Woocommerce ima:', len(novi_wc_artikli_za_poredjenje), 'artikala.')

original_stdout = sys.stdout

with open('wcArtikliTxt.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(novi_wc_artikli_za_poredjenje)
    sys.stdout = original_stdout # Reset the standard output to its original value

##################################################################################################################
# Pantheon artikli za poredjenje
##################################################################################################################

pta = []
for id in id_pantheon_artikala:
    x = list(filter(lambda x: x['sku'] == id, pantheon_artikli))
    pta.append(x)

pt_artikli_za_poredjenje_sa_woocommercom = []
for sublist in pta:
    for item in sublist:
        pt_artikli_za_poredjenje_sa_woocommercom.append(item)

novi_pt_artikli_za_poredjenje = []

for artikal in pt_artikli_za_poredjenje_sa_woocommercom:
    newdict = {k: artikal[k] for k in kljucevi}
    novi_pt_artikli_za_poredjenje.append(newdict)

print('Pantheon ima', len(novi_pt_artikli_za_poredjenje), 'artikala.')

with open('ptArtikliTxt.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(novi_pt_artikli_za_poredjenje)
    sys.stdout = original_stdout # Reset the standard output to its original value

##################################################################################################################
# Razlika artikala
##################################################################################################################

razlika = [i for i in novi_pt_artikli_za_poredjenje if i not in novi_wc_artikli_za_poredjenje]
for i in razlika:
    sku = i['sku']
    for x in woocommerce_artikli:
        for y in x:
            if y['sku'] == sku:
                i['id'] = y['id']
                       
    i['manage_stock'] = 'true'
print('Broj artikala koji se razlikuju je: ',len(razlika))
# print(razlika)


# razlika = [{'sku': '00101487', 'regular_price': '40.52', 'stock_quantity': 1, 'id': 10092, 'manage_stock': 'true'}, {'sku': '00102229', 'regular_price': '58.50', 'stock_quantity': 12, 'id': 10029, 'manage_stock': 'true'}]
