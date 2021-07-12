from connections import wcapi2
import pprint

woocommerce_atributi = []

def getAllAttributes():
    page = 1
    while page < 15:
        atributi = wcapi2.get("products/attributes", params={"per_page": 100, 'page':page}).json()
        woocommerce_atributi.append(atributi)
        page+=1

getAllAttributes()
    


# ################################################################################################
wc_atributi_lista = []

for atribut in woocommerce_atributi:
    for x in atribut:
        wc_atributi_lista.append(x)

print(len(wc_atributi_lista))
print(wc_atributi_lista)

# def sjedinjenje_idjeva_atributa():
#     for item in wc_atributi_lista:
#         ids_lista = []
#         for attr in wc_atributi_lista:
#             if attr['name'] == item['name']:
#                 ids_lista.append(attr['id'])
#         item_new_id = str(sorted(ids_lista)[0])
#         item_new_id_dict = {'id':item_new_id}

#         print('Atribut:', item['name'])
#         print('Stari ID:', item['id'])
#         print('Novi ID', item_new_id)
#         print(wcapi.put(f"products/attributes/{item['id']}", item_new_id_dict).json())
#         wcapi.put(f"products/attributes/{item['id']}", item_new_id_dict).json()

# idjevi_koji_se_koriste = []
# ids_lista_svi = []
# for item in wc_atributi_lista:
#     ids_lista = []
#     for attr in wc_atributi_lista:
#         if attr['name'] == item['name']:
#             ids_lista.append(attr['id'])
#             ids_lista_svi.append(attr['id'])
#     item_new_id = sorted(ids_lista)[0]
#     idjevi_koji_se_koriste.append(item_new_id)

# # print(set(idjevi_koji_se_koriste))
# # print(set(ids_lista_svi))

# idjevi_koji_se_ne_koriste =set(ids_lista_svi).difference(set(idjevi_koji_se_koriste))

# def brisanje_atributa_koji_se_ne_koriste():
#     for atribut in idjevi_koji_se_ne_koriste:
#         print(wcapi.delete(f"products/attributes/{atribut}", params={"force": True}).json())

# # brisanje_atributa_koji_se_ne_koriste()


# # for x in wc_atributi_lista:
#     # print(x['name'], x['id'])
# pprint.pprint(wc_atributi_lista)
# print('atributa ima',len(wc_atributi_lista))

