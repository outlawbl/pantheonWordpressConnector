from connections import wcapi

import json
import requests
import pprint
from wcArtikliTxt import *
from wcAtributiTxt import wc_atributi
import re
import collections

def get_digiteh_data():
    solditems = requests.get('https://digiteh.com/api/6886ba16-29b8-4a32-a909-7f3c2731a39c/data') # (your url)
    data = solditems.json()
    with open('digitehData.json', 'w') as f:
        json.dump(data, f)

with open('digitehData.json', 'r') as f:
    data = json.load(f)

#
# PROIZVODI
#

products = []
for product in data['products']:
    products.append(product)

#
# KATEGORIJE
#

categories = []
for category in data['categories']:
    categories.append(category)

uparena_lista_kategorija = [
   [100,3369],	[101,3369],	[102,3369],	[103,3369],	[104,3369],	[106,3011],	[11,3369],	[12,3369],	[120,3339],	[122,3339],	[123,3856],	[124,3856],	[177,3856], [13,3369],	[132,3478],	[133,3478],	[134,3478],	[136,3515],	[137,3515],	[138,3515],	[139,3515],	[14,3369],	[140,3515],	[141,3854],	[142,3854],	[144,3499],	[146,3499],	[147,3855],	[148,3855],	[15,3369],	[150,3855],	[151,3499],	[152,3478],	[153,3478],	[154,3010],	[155,3580],	[156,3580],	[159,3339],	[16,3369],	[161,3486],	[162,3604],	[164,3857],	[165,3855],	[166,3854],	[167,162],	[168,3369],	[169,3369],	[17,3007],	[170,3369],	[171,3369],	[172,3369],	[173,3854],	[174,3854],	[18,3007],	[19,3007],	[20,3007],	[21,3007],	[22,3007],	[23,3007],	[24,3369],	[25,3369],	[26,3369],	[27,3369],	[28,3369],	[3,3380],	[31,3336],	[32,3336],	[33,3336],	[34,3336],	[35,3336],	[36,3336],	[37,3336],	[38,3336],	[39,3336],	[4,3380],	[40,3336],	[41,3515],	[42,3515],	[43,3515],	[44,3515],	[45,3384],	[46,3384],	[47,3384],	[48,3384],	[49,3384],	[5,3380],	[51,3478],	[52,3478],	[53,3478],	[54,3478],	[55,3478],	[56,3478],	[57,3478],	[58,3478],	[59,3478],	[6,3380],	[63,3382],	[64,3011],	[66,3479],	[67,3479],	[68,3381],	[69,2911],	[7,3380],	[70,2911],	[71,2911],	[72,3382],	[73,2911],	[74,3479],	[75,3479],	[76,3479],	[77,2911],	[78,2911],	[80,3384],	[81,3384],	[83,3011],	[85,3384],	[86,3384],	[88,3369],	[89,3369],	[90,3369],	[91,3369],	[92,3369],	[93,3384],	[94,3384],	[95,3369],	[96,3478],	[97,3478],	[98,3478],	[99,3478]
]

#
# BRENDOVI
#

brands = []
for brand in data['brands']:
    brands.append(brand)

#
# PROIZVODJACI
#

manufacturers = []
for manufacturer in data['manufacturers']:
    products.append(manufacturer)

proizvodi_za_wc = []
varijacije = []
unikatni_racunari_i_laptopi = []
unikatni_racunari_i_laptopi_names = []
duplirani_racunari_i_laptopi = []
duplirani_racunari_i_laptopi_skus = []

#
# SREDJIVANJE ZA WOOCOMMERCE
#

for product in products:
    try:
        product['status'] = 'publish'
        product['manage_stock'] = 'true'
        product.pop('id')
        product['name'] = product['title']
        del product['title']
        product['sku'] = f"8{product['pantheonKey']}"
        del product['pantheonKey']
        product['price'] = str(product['anRTPrice'])
        product['regular_price'] = str(product['anRTPrice'])
        del product['anRTPrice']
        product['images'] = []
        image = {}
        if product['productPicture']:
            image['src'] = product['productPicture'] + '.jpg'
            product['images'].append(image)
        product['description'] = product['acDescr']
        product['categories'] = []
        for par in uparena_lista_kategorija:
            if product['categoryId'] == par[0]:
                kategorija_proizvoda = {}
                kategorija_proizvoda['id'] = par[1]
                product['categories'].append(kategorija_proizvoda)
        product['manage_stock'] = 'true'
        
        del product['productPicture']
        del product['brand']
        del product['brandId']
        del product['categoryTitle']
        del product['categoryPath']
        del product['categoryIdPath']
        del product['categoryId']
        del product['acName']
        product['stock_quantity'] = str(product['anStock'])
        if product['anStock'] > 0:
            product['stock_status'] = 'instock'
            product['backorders'] = 'yes'
        else:
            product['backorders'] = 'notify'
            product['backordered'] = 'true'
            product['backorders_allowed'] = 'true'
            product['stock_status'] = 'onbackorder'
        del product['anStock']
        del product['acDescr']
        del product['manufacturerPantheonKey']
        del product['manufacturerId']

        product['attributes'] = []
        
        
        try:
            if product['categories'][0]['id'] == 3856 or product['categories'][0]['id'] == 3855:
                racunar = product['name']
                if '/' in racunar:
                    ram = ''
                    proizvodjac = ''
                    procesor_model = ''
                    procesor_proizvodjac = ''
                    kuciste = ''
                    disk_velicina = ''
                    disk_tip = ''
                    velicina_ekrana = ''
                    try:
                        podaci_o_proizvodu = re.findall(r'(?!\/).+?(?=\/)', racunar)
                        podaci_o_proizvodu.append(re.findall(r'([^/]*$)', racunar)[0])
                        naziv_racunara = podaci_o_proizvodu[0].replace('Laptop ', '').replace('Laptopn ', '').replace('Laptopp ', '').replace('LEN', 'Lenovo').replace('LENOVO', 'Lenovo').replace('DELL', 'Dell').replace('FTS', 'Fujitsu')
                        naziv_racunara_sku = {
                            'name':naziv_racunara,
                            'sku':product['sku']
                        }
                        
                    except:
                        print('Naziv proizvoda vjerovatno nije dobar')
                    
                    if naziv_racunara_sku['name'] not in unikatni_racunari_i_laptopi_names:    
                        unikatni_racunari_i_laptopi.append(naziv_racunara_sku)
                        unikatni_racunari_i_laptopi_names.append(naziv_racunara_sku['name'])
                    else:
                        duplirani_racunari_i_laptopi.append(naziv_racunara_sku)
                        duplirani_racunari_i_laptopi_skus.append(naziv_racunara_sku['sku'])
                    # print(podaci_o_proizvodu)
    
                #   RAM
                    for podatak in podaci_o_proizvodu:
                        if 'RAM' in podatak:
                            ram = podatak.replace('RAM', '').strip()
                    
                    if ram == '':
                        try:
                            ram = re.findall(r'\d{1,2} *?GB', racunar)
                            ram = ram[0]
                        except:
                            ram = 'Bez RAM memorije'
                    ram = ram.replace(' ', '').replace('Gb', 'GB').strip()                       
                #   DISK
                    try:
                        disk_velicina = re.findall(r'\d{2,3} *?GB', racunar.replace('GGB', 'GB'))[0].strip()
                        disk_tip = 'HDD'
                    except:
                        try:
                            disk_velicina = re.findall(r'(?<=DISK).*?(?=\/)', racunar)[0].strip()
                        except:
                            try:
                                disk_velicina = re.findall(r'\d{1,3} *?TB', racunar)[0].strip()
                                disk_tip = 'HDD'
                            except:
                                disk_velicina = ''
                    if disk_velicina == '0GB':
                        disk_velicina = 'Bez Hard Diska'
                    if 'SSD' in racunar:
                        disk_tip = 'SSD'
                    if disk_velicina != 'Bez Hard Diska':
                        disk_velicina = disk_velicina.replace(' ', '')
                #   PROCESOR
                    for podatak in podaci_o_proizvodu:
                        if 'gen' in podatak or 'i3' in podatak or 'i5' in podatak or 'i7' in podatak or 'I3' in podatak or 'I5' in podatak or 'I7' in podatak:
                            procesor_proizvodjac = 'Intel'
                            procesor_model = podatak
                            procesor_model = procesor_model.replace(' ', '').strip()
                        else:
                            try:
                                procesor_model = re.findall(r'\d{4}\w', racunar)[0].strip()
                                procesor_proizvodjac = 'Intel'
                            except:
                                pass
                #   PROIZVODJAC
                    try:
                        proizvodjac = re.findall(r'^\w+', podaci_o_proizvodu[0])[0]
                        if proizvodjac == 'FTS':
                            proizvodjac = 'Fujitsu'
                        if proizvodjac == 'No':
                            proizvodjac = 'No name'
                        if proizvodjac == 'LEN':
                            proizvodjac = 'Lenovo'
                    except:
                        print('Naziv proizvoda vjerovatno nije dobar')
                #   VELICINA EKRANA
                    for podatak in podaci_o_proizvodu:
                            if '"' in podatak:
                                velicina_ekrana = podatak
                                velicina_ekrana = velicina_ekrana.strip()


                    # print(racunar)
                    # print('HD:', disk_velicina, disk_tip)
                    # print('RAM:', ram)
                    # print('PROIZVODJAC:', proizvodjac)
                    # print('PROCESOR PROIZVODJAC:', procesor_proizvodjac)
                    # print('PROCESOR MODEL:', procesor_model)
                    # print('VELICINA EKRANA:', velicina_ekrana)


                    # print('==============================================')

                    for a in wc_atributi:
                        if a['name'] == 'Procesor.Tip':                  
                            procesor_attr = {
                                'id': a['id'],
                                'name':'Procesor.Tip',
                                'options':[
                                    f'{procesor_model}'
                                ],
                                'visible':'true'
                            }
                        if a['name'] == 'Memorija.Tip':                  
                            ram_attr = {
                                'id': a['id'],
                                'name':'Memorija.Tip',
                                'options':[
                                    f'{ram}'
                                ],
                                'visible':'true'
                            }
                        if a['name'] == 'Hard Disk.Velicina':
                            disk_attr = {
                                'id': a['id'],
                                'name':'Hard Disk.Velicina',
                                'options':[
                                    f'{disk_velicina}'
                                ],
                                'visible':'true'
                            }
                        if a['slug'] == 'pa_333_proizvodac':
                            proizvodjac_attr = {
                                'id': a['id'],
                                'name':'Proizvođač',
                                'options':[
                                    f'{proizvodjac}'
                                ],
                                'visible':'true'
                            }
                        if a['slug'] == 'pa_333_procesor-proizvodac':
                            procesor_proizvodjac_attr = {
                                'id': a['id'],
                                'name':'Procesor.Proizvođač',
                                'options':[
                                    f'{procesor_proizvodjac}'
                                ],
                                'visible':'true'
                            }
                        if a['slug'] == 'pa_333_dijagonala-ekrana':
                            dijagonala_ekrana_attr = {
                                'id': a['id'],
                                'options':[
                                    f'{velicina_ekrana}'
                                ],
                                'visible':'true'
                            }

                product['attributes'].append(procesor_attr)
                product['attributes'].append(ram_attr)
                product['attributes'].append(disk_attr)
                product['attributes'].append(proizvodjac_attr)
                product['attributes'].append(procesor_proizvodjac_attr)
                if product['categories'][0]['id'] == 3855:
                    product['attributes'].append(dijagonala_ekrana_attr)
                product['name'] = f'{naziv_racunara}/{procesor_proizvodjac} {procesor_model}/{ram}/{disk_velicina} {disk_tip}'
                product['meta_data'] = [
                    {
                    "key": "_specifications_display_attributes",
                    "value": "yes"
                    },
                    {
                    "key": "naziv_racunara",
                    "value": naziv_racunara
                    }
                    ]
                
                # print(product['name'], product['sku'], 'nema na shopu, bice insertovan')
                # print(wcapi.post("products", product).json())
        except:
            pass
        if product['sku'] not in duplirani_racunari_i_laptopi_skus:
            proizvodi_za_wc.append(product)
        else:
            varijacije.append(product)
        
    except:
        pass



    
# for d_proizvod in proizvodi_za_wc:
#     for grupa in wcArtikli:
#         for wc_proizvod in grupa:
#             if d_proizvod['sku'] == wc_proizvod['sku']:
#                 print('ima vec na shopu')
#             else:
#                 print('nema na shopu')
#                 # print(wcapi.post("products", d_proizvod).json())

wc_artikli = []
wc_artikli_skus = []
for grupa in wcArtikli:
    for artikal in grupa:
        wc_artikli.append(artikal)
        wc_artikli_skus.append(artikal['sku'])

# for artikal in wc_artikli:
#     for proizvod in proizvodi_za_wc:
#         if artikal['sku'] == proizvod['sku']:
#             print('ima ga na shopu')
#         else:
#             print(wcapi.post("products", proizvod).json())


# AKO POSTOJI TAKAV ISTI PROIZVOD ONDA JE VARIJACIJA I TREBA GA SREDITI ZA WOOCOMMERCE
duplirani_racunari_i_laptopi_skus = []
for x in duplirani_racunari_i_laptopi:
    duplirani_racunari_i_laptopi_skus.append(x['sku'])
for proizvod in varijacije:
    sredjeni_artikal = {}
    # sredjeni_artikal['image'] = proizvod['images'][0]
    sredjeni_artikal['attributes'] = proizvod['attributes']
    sredjeni_artikal['regular_price'] = proizvod['regular_price']
    sredjeni_artikal['sku'] = proizvod['sku']
    for unikat in unikatni_racunari_i_laptopi:
        if unikat['name'] == proizvod['meta_data'][1]['value']:
            for a in wc_artikli:
                if a['sku'] == unikat['sku']:
                    roditeljski_id = a['id'] 
                    # print('Varijacija:', sredjeni_artikal['sku'])
                    # print('Roditelj:', unikat['sku'], roditeljski_id)
                    # print('==============================================')
                    # print(wcapi.post(f"products/{id}/variations", sredjeni_artikal).json())

# ARTIKAL KOJEM JE ON VARIJACIJA TREBA PREPRAVITI DA JE VARIJABILAN
                    novi_atributi = a['attributes']
                    for stari_attr in novi_atributi:
                        stari_attr['variation'] = 'True'
                    novi_atributi = {'attributes':novi_atributi}
                    print(novi_atributi)
                    print(wcapi.put(f"products/{roditeljski_id}", f'{novi_atributi}').json())
    # UPDATE-OVATI ATRIBUT DA BUDU VARIABILNI
                    for attr in a['attributes']:
                        attr_id = attr['id']
                        data = {
                            "variation": "true"
                        }
                        print(wcapi.put(f"products/attributes/{attr_id}", data).json())

                    



def insert_products():
    for proizvod in proizvodi_za_wc:
        if proizvod['sku'] in wc_artikli_skus:
            print('postoji')
        else:
            print(proizvod['name'], proizvod['sku'], 'nema na shopu, bice insertovan')
            print(wcapi.post("products", proizvod).json())

insert_products()