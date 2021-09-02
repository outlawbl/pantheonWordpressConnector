from pantheonArtikli import pantheon_artikli, id_pantheon_artikala, pantheon_stari_artikli_ids
from woocommerceArtikli import wc_artikli_za_poredjenje, id_woocommerce_artikala, woocommerce_artikli
from jsondiff import diff
import sys

kljucevi_za_poredjenje = ['sku', 'regular_price', 'stock_quantity', 'sale_price'] #'stock_status',

##################################################################################################################
# Pantheon artikli za poredjenje
##################################################################################################################

pt_artikli_za_poredjenje_sa_woocommercom = []
for id in id_pantheon_artikala:
    i = list(filter(lambda x: x['sku'] == id, pantheon_artikli))
    pt_artikli_za_poredjenje_sa_woocommercom.append(i[0])

# pt_artikli_za_poredjenje_sa_woocommercom = []
# for sublist in pta:
#     for y in sublist:
#         pt_artikli_za_poredjenje_sa_woocommercom.append(y)

novi_pt_artikli_za_poredjenje = []

for pt_artikal in pt_artikli_za_poredjenje_sa_woocommercom:
    # if pt_artikal['sku'] not in pantheon_stari_artikli_ids:
    pt_dict = {kljuc: pt_artikal[kljuc] for kljuc in kljucevi_za_poredjenje}
    novi_pt_artikli_za_poredjenje.append(pt_dict)

print('Pantheon ima', len(novi_pt_artikli_za_poredjenje), 'artikala.')

##################################################################################################################
# Woocommerce artikli za poredjenje
##################################################################################################################

wca = []
for pt_id in id_pantheon_artikala:
    j = list(filter(lambda z: z['sku'] == pt_id, wc_artikli_za_poredjenje))
    wca.append(j)
# print(len(id_pantheon_artikala), 'id_pantheon_artikala')

wc_artikli_za_poredjenje_sa_pantheonom = []
for lista in wca:
    for item in lista:
        item['name'] = str(item['name']).replace('&amp;','&')
        wc_artikli_za_poredjenje_sa_pantheonom.append(item)

novi_wc_artikli_za_poredjenje = []

for wc_artikal in wc_artikli_za_poredjenje_sa_pantheonom:
    wc_dict = {wc_k: wc_artikal[wc_k] for wc_k in kljucevi_za_poredjenje}
    novi_wc_artikli_za_poredjenje.append(wc_dict)

print('Woocommerce za poredjenje ima:', len(novi_wc_artikli_za_poredjenje), 'artikala.')


# original_stdout = sys.stdout

# with open('wcArtikliTxt.py', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     print(f'wcArtikli = {novi_wc_artikli_za_poredjenje}')
#     sys.stdout = original_stdout # Reset the standard output to its original value

##################################################################################################################
# Razlika artikala
##################################################################################################################

razlika = [i for i in novi_pt_artikli_za_poredjenje if i not in novi_wc_artikli_za_poredjenje]
for artikal in razlika:
    for item in novi_pt_artikli_za_poredjenje:
        if item['sku'] == artikal['sku']:
            print('----Novi Pantheon Artikal----',item)

    sku = artikal['sku']
    artikal['backorders'] = 'yes'

    for grupa_artikala in woocommerce_artikli:
        for y in grupa_artikala:
            if y['sku'] == sku:
                artikal['id'] = y['id']

    if artikal['stock_quantity'] > 0:
        artikal['status'] = 'publish'
    else:
        artikal['status'] = 'draft'
                       
    artikal['manage_stock'] = 'true'
    

    # artikal['manage_stock'] = 'true'
    for item in novi_wc_artikli_za_poredjenje:
        if item['sku'] == sku:
            print('--Stari Woocommerce Artikal--',item)
            print('-------------------------------------')       
print('Broj artikala koji se razlikuju je: ',len(razlika))
# print(razlika)


# razlika = [{'sku': '00101487', 'regular_price': '40.52', 'stock_quantity': 1, 'id': 10092, 'manage_stock': 'true'}, {'sku': '00102229', 'regular_price': '58.50', 'stock_quantity': 12, 'id': 10029, 'manage_stock': 'true'}]
