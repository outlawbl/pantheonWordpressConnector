from wcArtikliTxt import wcArtikli 

wcArtikliAll = []

for grupa in wcArtikli:
    for artikal in grupa:
        wcArtikliAll.append(artikal)
print('WC Artikala ima:',len(wcArtikliAll))

# Kategorije

# for artikal in wcArtikliAll:
#     for katgorija in artikal['categories']:
#             print(katgorija)

# Atributi

for artikal in wcArtikliAll:
    for atribut in artikal['attributes']:
        if atribut['name'] == 'Proizvođač':
            print(atribut['id'],atribut['name'])