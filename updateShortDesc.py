from connections import wcapi
from woocommerceArtikli import woocommerce_artikli
from wcArtikliTxt import wcArtikli

# def updateShortDesc():
#     for artikli in woocommerce_artikli:
#         for artikal in artikli:
#             id = artikal['id']
#             try:
#                 diagonala = artikal['attributes'][next((index for (index, d) in enumerate(artikal['attributes']) if d["name"] == "Rezolucija ekrana"), None)]['options'][0]
#             except TypeError:
#                 diagonala = '-'
            
#             try:
#                 cpu = artikal['attributes'][next((index for (index, d) in enumerate(artikal['attributes']) if d["name"] == "Procesor.Tip"), None)]['options'][0]
#             except TypeError:
#                 cpu = '-'

#             try:
#                 disk = artikal['attributes'][next((index for (index, d) in enumerate(artikal['attributes']) if d["name"] == "SSD Disk.Velicina"), None)]['options'][0]
#             except TypeError:
#                 disk = '-'
            
#             try:
#                 ram = artikal['attributes'][next((index for (index, d) in enumerate(artikal['attributes']) if d["name"] == "Memorija.Tip"), None)]['options'][0]
#             except TypeError:
#                 ram = '-'
    
#             if artikal['sku'] == '01422963':
#                 data = {'short_description' : f'[ao_descript-custom icona="fa-tv" namea="Displej" parama="{diagonala}" iconb="fa-microchip" nameb="CPU" paramb="{cpu}" iconc="fa-memory" namec="RAM" paramc="{ram}" icond="fa-hdd" named="Disk" paramd="{disk}"][/ao_descript-custom]'}
#                 print(wcapi.put(f"products/{id}", data).json())

def updateShortDesc():
    for artikli in woocommerce_artikli:
        for artikal in artikli:
            id = artikal['id']
            kategorija_za_update = 'laserski'
            try:
                kategorija = artikal['categories'][next((index for (index, d) in enumerate(artikal['categories']) if d["slug"] == kategorija_za_update), None)]['slug']
            except TypeError:
                kategorija = 'nepoznata'
            if kategorija == kategorija_za_update: 
                data = {'short_description' : f'[ao_descript-custom category_ao_slug="{kategorija_za_update}"][/ao_descript-custom]'}
                print(wcapi.put(f"products/{id}", data).json())

updateShortDesc()