from connections import wcapi
import pprint
import sys

ukupno_stranica_atributa = wcapi.get("products/attributes?per_page=100").headers['X-WP-TotalPages']

woocommerce_atributi = []

page = 1
while page <= int(ukupno_stranica_atributa):
    atributi = wcapi.get("products/attributes", params={"per_page": 100, 'page':page}).json()
    woocommerce_atributi.append(atributi)
    page+=1

################################################################################################
wc_atributi_lista = []

for atribut in woocommerce_atributi:
    for x in atribut:
        wc_atributi_lista.append(x)

def sjedinjenje_idjeva_atributa():
    for item in wc_atributi_lista:
        ids_lista = []
        for attr in wc_atributi_lista:
            if attr['name'] == item['name']:
                ids_lista.append(attr['id'])
        item_new_id = str(sorted(ids_lista)[0])
        item_new_id_dict = {'id':item_new_id}

        print('Atribut:', item['name'])
        print('Stari ID:', item['id'])
        print('Novi ID', item_new_id)
        print(wcapi.put(f"products/attributes/{item['id']}", item_new_id_dict).json())
        wcapi.put(f"products/attributes/{item['id']}", item_new_id_dict).json()

idjevi_koji_se_koriste = []
ids_lista_svi = []
for item in wc_atributi_lista:
    ids_lista = []
    for attr in wc_atributi_lista:
        if attr['name'] == item['name']:
            ids_lista.append(attr['id'])
            ids_lista_svi.append(attr['id'])
    item_new_id = sorted(ids_lista)[0]
    idjevi_koji_se_koriste.append(item_new_id)

# print(set(idjevi_koji_se_koriste))
# print(set(ids_lista_svi))

idjevi_koji_se_ne_koriste =set(ids_lista_svi).difference(set(idjevi_koji_se_koriste))

def brisanje_atributa_koji_se_ne_koriste():
    for atribut in idjevi_koji_se_ne_koriste:
        print(wcapi.delete(f"products/attributes/{atribut}", params={"force": True}).json())

# brisanje_atributa_koji_se_ne_koriste()


# for x in wc_atributi_lista:
    # print(x['name'], x['id'])
# pprint.pprint(wc_atributi_lista)
print('Atributa ima',len(wc_atributi_lista))

original_stdout = sys.stdout

with open('wcAtributiTxt.py', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(f'wc_atributi = {wc_atributi_lista}')
    sys.stdout = original_stdout # Reset the standard output to its original value

