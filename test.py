# import re
import pprint
# from wcArtikliTxt import wcArtikli
# from connections import db

# opis = 'Laptop Fujitsu H710 Workstation\r\nFSC Celsius H910 \r\nProizvoÄ‘aÄŤ: Fujitsu\r\nDijagonala ekrana: 17,3" LED  \r\nRezolucija ekrana: Full HD (1920x1080)\r\nProcesor.Tip: Intel Core i7 2620M - 3,4 GHz 2-nd Gen \r\nProcesor.ProizvoÄ‘aÄŤ: Intel\r\nMemorija.Tip: 8GB DDR3 \r\nHard Disk.Velicina: 500GB \r\nSSD Disk.Velicina: -\r\nGrafika: NVidia Quadrro 4000M 2 GB \r\nOptika: DVD-RW\r\nBoja: -\r\nTouch screen: Ne\r\nOperativni system: -\r\nGarancija:6 mjeseci'

# atributi_iz_opisa = []

# for red in opis.splitlines():
#   atribut = {}
#   kljuc_atributa = re.findall(r'.+?(?=:)', red)
#   vrijednost_atributa = re.findall(r'(?<=:).*', red)
#   if len(kljuc_atributa) > 0:
#     atribut['name'] = kljuc_atributa[0].strip()
#     options = []
#     options.append(vrijednost_atributa[0].strip())
#     atribut['options'] = options
#     atributi_iz_opisa.append(atribut)

# pprint.pprint(atributi_iz_opisa)

# def update_polja_postavi_na_web_sajt():
#     cur = db.cursor()

#     out_of_stock = []
#     for artikli in wcArtikli:
#         for artikal in artikli:
#             if artikal['stock_status'] == 'outofstock' :
#                 out_of_stock.append(artikal['sku'])
#     # print(out_of_stock)
#     # print(len(out_of_stock))

#     for x in out_of_stock:
#         upit = f"update tHE_SetItem set acFieldSF = 'DA' where acIdent = '{x}'"
#         cur.execute(upit)
#         db.commit()
#         print('Promjenjen je', x)

# # update_postavi_na_web_sajt()

# string = 'Proizćčđš\nlkasjdflkasj\nlaskdjflksj'

# for red in string.splitlines():
#     print(red)


# from wcCategories import woocommerce_kategorije
# from digitehProducts import categories

# for cat in categories:
#     print (cat['title'],";",cat['parentId'],";",cat['id'],";",cat['categoryIdPath'])

# print('---')
# for wccat in woocommerce_kategorije:
#     print (wccat['name'],";",wccat['id'])

# uparena_lista_kategorija = [
#    [100,3369],	[101,3369],	[102,3369],	[103,3369],	[104,3369],	[106,3011],	[11,3369],	[12,3369],	[120,3339],	[122,3339],	[123,3856],	[124,3856],	[13,3369],	[132,3478],	[133,3478],	[134,3478],	[136,3515],	[137,3515],	[138,3515],	[139,3515],	[14,3369],	[140,3515],	[141,3854],	[142,3854],	[144,3499],	[146,3499],	[147,3855],	[148,3855],	[15,3369],	[150,3855],	[151,3499],	[152,3478],	[153,3478],	[154,3010],	[155,3580],	[156,3580],	[159,3339],	[16,3369],	[161,3486],	[162,3604],	[164,3857],	[165,3855],	[166,3854],	[167,162],	[168,3369],	[169,3369],	[17,3007],	[170,3369],	[171,3369],	[172,3369],	[173,3854],	[174,3854],	[18,3007],	[19,3007],	[20,3007],	[21,3007],	[22,3007],	[23,3007],	[24,3369],	[25,3369],	[26,3369],	[27,3369],	[28,3369],	[3,3380],	[31,3336],	[32,3336],	[33,3336],	[34,3336],	[35,3336],	[36,3336],	[37,3336],	[38,3336],	[39,3336],	[4,3380],	[40,3336],	[41,3515],	[42,3515],	[43,3515],	[44,3515],	[45,3384],	[46,3384],	[47,3384],	[48,3384],	[49,3384],	[5,3380],	[51,3478],	[52,3478],	[53,3478],	[54,3478],	[55,3478],	[56,3478],	[57,3478],	[58,3478],	[59,3478],	[6,3380],	[63,3382],	[64,3011],	[66,3479],	[67,3479],	[68,3381],	[69,2911],	[7,3380],	[70,2911],	[71,2911],	[72,3382],	[73,2911],	[74,3479],	[75,3479],	[76,3479],	[77,2911],	[78,2911],	[80,3384],	[81,3384],	[83,3011],	[85,3384],	[86,3384],	[88,3369],	[89,3369],	[90,3369],	[91,3369],	[92,3369],	[93,3384],	[94,3384],	[95,3369],	[96,3478],	[97,3478],	[98,3478],	[99,3478]
# ]

# for par in uparena_lista_kategorija:
#     if 336 in par:
#         print(par[1])

import re

racunari = ['No Name / i3-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'No Name Gigabyte / i7-3gen/ RAM 4GB/ HDD 250GB/ TWR', 'Dell OptiPlex 7020/ i3-4gen/ RAM 4GB/ DISK 0GB/ SFF', 'Dell OptiPlex 7020/ i5-4gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP Elite 8200/ i3-2gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP Compaq Pro 6300/ i5-3gen/ RAM 4GB/ HDD 250GB/ SFF', 'HP Elite 8300/ i3-3gen/ RAM 4Gb/ HDD 320GB/ SFF', 'Intel/No Name/i7-2 gen/ RAM 4GB/ HDD 320GB M Tower', 'Acer Veriton M490G/i5-1 gen/ RAM 4GB/ HDD 320GB M Tower', 'Acer Veriton M4610G/i5-2 gen/ RAM 4GB/ HDD 320GB M Tower', 'No Name Gigabyte B75/ i7-3gen/ RAM 4GB/ DISK 0GB/ TWR', 'HP Compaq 8200 Elite/ i7-2gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP Elite 8300/ i3-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP ProDesk 400 G1/ i3-4 gen/ RAM 4GB/ HDD 250GB/ SFF', 'HP ProDesk 400 G1/ i3-4gen/ RAM 4GB/ DISK 0GB/ SFF', 'Hyundai G-Series I7 /3 gen /4 GB/500 GB/ M. tower', 'Tarox Celeron E3300 /4 GB/500 GB/M.tower', 'Acer Veriton M4610G/i5-2 gen/ RAM 4GB/ HDD 500GB M Tower', 'Acer Veriton M490G/i5- 760/ RAM 4GB/ HDD 500GB M Tower', 'FTS Esprimo P910 E90/ i7-3gen/ RAM 4GB/ DISK 0GB/ TWR', 'Dell OptiPlex 9020/ i7-4gen/ RAM 4GB/ HDD 250GB/ SFF', 'Dell OptiPlex 7020/ i5-4gen/ RAM 4GB/ HDD 320GGB/ SFF', 'No Name/i5-2 gen/ RAM 4GB/ HDD 500GB M Tower 2', 'FTS Esprimo P700 E90+/ i5-2gen/ RAM 4GB/ DISK 0GB/ TWR', 'HP Compaq 8200 Elite/ i5-2gen/ RAM 4GB/ HDD 230GB/ SFF', 'HP Compaq 6200/ i5-2gen/ RAM 4GB/ HDD 300GB/ TWR', 'HP ProDesk 600 G1/ G1820/ RAM 4GB/ HDD 300GB/ SFF', 'HP Compaq 6300/ i5-3gen/ RAM 4GB/ HDD 250GB/ SFF', 'HP EliteDesk 800 G1/ i5-4gen/ RAM 4GB/ DISK 0GB/ TWR', 'Tarox I5-6400/2,70GHz/8 GB/500 GB /M.tower', 'FTS C910 I7-3770/3,40GHz/4 GB/500 GB /SFF', 'Dell Optiplex 990 /I7- 2 gen/ RAM 4GB/ HDD 500GB SFF', 'FTS Esprimo 710 E85+/i5-3 gen/ RAM 4GB/ HDD 500GB SFF', 'Dell OptiPlex 5040/ i3-6gen/ RAM 4GB/ DISK 0GB/ TWR', 'Dell OptiPlex 5040/ i5-6gen/ RAM 4GB/ DISK 0GB/ TWR', 'Dell OptiPlex 7040/ i5-6gen/ RAM 4GB/ DISK 0GB/ TWR', 'Acer Veriton / i3-3gen/ RAM 4GB/ HDD 250GB/ TWR', 'HP ProDesk 600 G1/ i5-4gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP Compaq 8300/ i7-2gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP Compaq 8300/ i7-2gen/ RAM 4GB/ HDD 250GB/ SFF', 'HP Elite 8300/ i3-3gen/ RAM 4GB/ HDD 400GB/ SFF', 'HP ProDesk 600 G1/ i5-4gen/ RAM 4GB/ HDD 250GB/ SFF', 'Lenovo ThinkCentre M92p/ i5-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'Dell OptiPlex 5050/ i5-6gen/ RAM 4GB/ HDD 320GB/ SFF', 'Dell OptiPlex 5050/ i5-6gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP Pro 3500/ PENTIUM/ RAM 4GB/ DISK 0GB/ TWR', 'Dell OptiPlex 3020/ i5-4gen/ RAM 4GB/ HDD 320GB/ SFF', 'FTS Esprimo P500/ i3-2gen/ RAM 4GB/ DISK 0GB/ TWR', 'Dell OptiPlex 3040/ i5-6gen/ RAM 4GB/ DISK 0GB/ SFF', 'Dell OptiPlex 7010/ i3-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'Dell OptiPlex 5040/ i5-6gen/ RAM 4GB/ DISK 0GB/ SFF', 'FTS Esprimo P2760/ i3-1gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo P720/ i3-4gen/ RAM 4GB/ HDD 320GB/ TWR', 'Tarox / i5-1gen/ RAM 4GB/ HDD 250GB/ TWR', 'Bluechip / i7-3gen/ RAM 4GB/ HDD 250GB/ TWR', 'FTS Esprimo P2760/ i5-1gen/ RAM 4GB/ HDD 250GB/ TWR', 'HP Compaq 6200 Pro/ i5-2gen/ RAM 4GB/ DISK 0GB/ TWR', 'Bluechip / i5-2gen/ RAM 4GB/ HDD 250GB/ SFF', 'FTS Esprimo P720/ i3-4gen/ RAM 4GB/ HDD 230GB/ TWR', 'FTS Esprimo P900/ i3-4gen/ RAM 4GB/ HDD 320GB/ TWR', 'HP Compaq Pro 6300/ i5-3gen/ RAM 4GB/ HDD 320GB/ TWR', 'Acer Veriton / i3-3gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo P720/ i3-4gen/ RAM 4GB/ HDD 250GB/ TWR', 'Dell OptiPlex 3020/ i5-4gen/ RAM 4GB/ HDD 250GB/ SFF', 'No Name /G620 / RAM 4GB/ HDD 250GB/ SFF', 'Dell Optiplex 7010/ i5-3gen/ RAM 4GB/ HDD 250GB/ SFF', 'Dell OptiPlex 7020/ i3-4gen/ RAM 4GB/ HDD 320GB/ SFF', 'Hyundai Pentino G-Serie/ G2030/ RAM 4GB/ DISK 0GB/ SFF', 'FTS Esprimo P520 E85+/ i5-4gen/ RAM 4GB/ DISK 0GB/ TWR', 'No Name Gigabyte / i7-3gen/ RAM 8GB/ DISK 0GB/ TWR', 'Giada F301/ i3-5gen/ RAM 8GB/ HDD 120GB/ MINI PC', 'Giada F302/ i3-6gen/ RAM 8GB/ DISK 0GB/ MINI PC', 'BlueChip PC G5400/ RAM 8GB/ HDD 130GB/ TWR', 'Terra 1009420/ i3-4gen/ RAM 4GB/ HDD 120GB/ SFF', 'BlueChip PC/ i5-3gen/ RAM 8GB/ HDD 500GB/ TWR', 'No Name Intel Pentium G3220/ dualcore/ RAM 4GB/ HDD 500GB/ TWR', 'No Name BlueChip/ i5-4gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo D756 I5-6400/4 GB/500 GB/SFF', 'ACE Veriton X4640  I5-6400/2,7 Ghz/8 GB/240 GB SSD/SFF', 'No Name Hyrican CTS00200/ i3-4gen/ RAM 4GB/ HDD 500GB/ TWR', 'No Name BlueChip/ i5-4gen/ RAM 2GB/ HDD 500GB/ TWR', 'Acer Veriton X4650G/ i5-6gen/ RAM 8GB/ HDD 250GB/ SFF', 'No Name / i5-3gern/ RAM 4GB/ HDD 500GB/ SFF', 'No Name BlueChip/ i5-4gen/ RAM 4GB/ HDD 120GB/ TWR', 'No Name BlueChip/ i5-4gen/ RAM 4GB/ HDD 1TB/ TWR', 'Acer Veriton X2631G/ G1840/ RAM 4GB/ HDD 500GB/ SFF', 'NoName PC/ i3-4gen/ RAM 4GB/ 128SSD/ MINI PC', 'No Name Intel Pentium E6320/ core 2 duo/ RAM 4GB/ DISK 0GB/ TWR', 'Giada F302/ i3-6gen/ RAM 8GB/ HDD 120GB/ MINI PC', 'FTS P700 E85+/ i5-2gen/ RAM 4GB/ HDD 320GB/ TWR', 'Lenovo/ThinkCentre M92p/i7-3 gen/ RAM 4GB/ HDD 320GB M.Tower', 'FTS Esprimo E700 / i5-2 gen/ RAM 4GB/ HDD 500GB SFF', 'Tarox G4400/RAM 4GB/ HDD 320GB M.Tower', 'HP Compaq Pro 6300/i3-3 gen/ RAM 4GB/ HDD 250GB/ SFF', 'HP Compaq 8200 Elite/i5-2 gen/ RAM 4GB/ HDD 500GB SFF', 'FTS Esprimo E910/i5-3 gen/ RAM 4GB/ HDD 250GB SFF', 'Dell Optiplex 7010/ i3-3gen/ RAM 2GB/ HDD 300GB/ TWR', 'Dell OptiPlex 7010/ i3-3gen/ RAM 4GB/ HDD 300GB/ TWR', 'FTS Esprimo D556  i5-6400\t2,70 GHz/SFF/4GB/128GB/SDD', 'HP Compaq  Pro 6300 I3-3220/4 GB/250 GB/M.tower', 'FTS Esprimo D556  i5-6400\t2,70 GHz/SFF/8 GB/128GB/SDD', 'Tarox I5-2400/8 GB/250 GB /M.tower', 'FTS Esprimo P410 E85+ I5-3330/4 GB/250 GB/M.tower', 'HP Compaq  6200 Pro I5-2500/4 GB/250 GB/M.tower', 'HP Compaq Pro 6300/i5-2 gen/ RAM 4GB/HDD 500GB M.Tower', 'Dell Optiplex 790 /i5-2gen/ RAM 4GB/ DISK 0GB/ SFF', 'Dell Precision T1600/ i3-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'Dell OptiPlex 390/ i3-2gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP Compaq 8200 Elite/i5- 2 GEN/RAM 4GB/ HDD 500GB SFF', 'FTS Esprimo P520 E85+ /i5-4gen/ RAM 4GB/ HDD 250GB/ TWR', 'Tarox /i7-1gen/ RAM 4GB/ HDD 500GB/ Tower', 'HP Compaq 8300/i5-3gen/ RAM 4GB/ HDD 250GB/ Tower', 'HP Elite 8300/i5-3gen/ RAM 4GB/ DISK 0GB/ Tower', 'FTS Esprimo E900/i5-3gen/ RAM 4GB/ DISK 0GB/ Tower', 'FTS Esprimo E900/i5-2gen/ RAM 4GB/ HDD 500GB/Tower', 'HP Compaq 8200 /i5-2gen/ RAM 4GB/ DISK 0GB/ SFF', 'Lenovo ThinkCentre M73/i3-4 gen/ RAM 4GB/ HDD 320GB/ Tower', 'Fts Esprimo E710 E85+/i5-3gen/ RAM 4GB/ DISK 0GB/Tower', 'FTS Esprimo E710 E85+/i5-2gen/ RAM 4GB/ DISK 0GB/ Tower', 'FTS Esprimo E700 E85+/ i5-2gen/ RAM 4GB/ DISK 0GB/Tower', 'FTS Esprimo E900/i5-2gen/ RAM 4GB/ HDD 320GB/ Tower', 'HP Compaq 8200 /i5-2gen/ RAM 4GB/ DISK 0GB/ Tower', 'FTS Esprimo P710 E85+/i5-3gen/ RAM 4GB/ DISK 0GB/ Tower', 'Lenovovo ThinkStation E31/i5-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'Lenovo ThinkCentre M82/i3-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'FTS Esprimo P710/i3-3gen/ RAM 4GB/ DISK 0GB/ Tower', 'Dell Optiplex 3010/i3-2 gen/ RAM 4GB/ DISK 0GB/ SFF', 'Dell Optiplex 3020/i3-4 gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP Compaq Pro 6300/i3-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'No Name/ i5-2gen/ RAM 4GB/ DISK 0GB/ Tower', 'Tarox / i7-1 gen/ RAM 4GB/ HDD 500GB/ Tower', 'HP ProDesk 400 G2/ i5-4gen/ RAM 4GB/ HDD 250GB/ TWR', 'HP ProDesk 400 G2/ i5-4gen/ RAM 4GB/ DISK 0GB/ TWR', 'Dell Optiplex 790/ i7-2gen/ RAM 4GB/ DISK 0GB/ TWR', 'HP Compaq 8200 / i7-2gen/ RAM 4GB/ DISK 0GB/ TWR', 'HP Compaq 6300 / i5-3gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS P910 E90+/ i5-3gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS P920 0-WATT/ i5-4gen/ RAM 4GB/ DISK 0GB/ TWR', 'HP Compaq 8200 / i7-2gen/ RAM 8GB/ DISK 0GB/ TWR', 'FTS Esprimo P900 0-WATT/ i5-2gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo P2760/i5-1gen/ RAM 4GB/ HDD 500GB/ Tower', 'FTS Esprimo P400/i5-2gen/ RAM 4GB/ HDD 500GB/Tower', 'Exone/i5-2 gen/ RAM 4GB/HDD 500GB TWR', 'FTS Esprimo P700 E90+ / i5-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'HP Compaq 8300/i5-3gen/ RAM 4GB/ DISK 0GB/ Tower', 'FTS Esprimo P400/i5-2gen/ RAM 4GB/ DISK 0GB/ Tower', 'Fujitsu Esprimo P400  i5-2310 2.90 4 GB PC3 250 GB', 'HP ProDesk 400 G2/ G3240/ RAM 0GB/ HDD 0GB/ TWR', 'HP pro 6300 / i5-3 gen/ RAM 4GB/ HDD 250GB', 'FTS Esprimo E910/i5-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'FTS Esprimo P900 0-WATT/ i5-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'HP ProDesk 400 G2/ G3250/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo P910 0-WATT/ i5-3gen/ RAM 4GB/ HDD 250GB/TWR', 'FTS Esprimo P900 0-WATT/ i5-2gen/ RAM 4GB/ HDD 500GB/ TWR', 'HP 280 G1/ G3250/ RAM 4GB/ DISK 0GB/ TWR', 'HP ProDesk 400 G3/ G4400/ RAM 0GB/ DISK 0GB/ TWR', 'HP Compaq 8200 Elite Intel i5-2400;  _____GB RAM;  _____GB HDD', 'No Name BlueChip/ i5-4gen/ RAM 4GB/ HDD 500GB/ TWR', 'Acer Veriton M6620G/ i7-4gen/ RAM 8GB/ HDD 2TB/ TWR', 'Terra 1009420/ i3-4gen/ RAM 4GB/ DISK 0GB/ SFF', 'Tarox/ i3- 1 gen/ RAM 4GB/ HDD 500GB/ Tower', 'Dell D07D /i3-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'Acer Veriton M2631/ i5-4gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo P910 E90+/ i5-3gen/ RAM 4GB/ HDD 250GB/ TWR', 'Microstar /i5-2gen/ RAM 4GB/ HDD 500GB/ Tower', 'HP Compaq 8300/ i5-3gen/ RAM 0GB/ DISK 0GB/ TWR', 'HP Compaq 8300/ i5-3gen/ RAM 2GB/ HDD 250GB/ TWR', 'HP Compaq 8200 / i7-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'Dell D08S /i3-4gen/ RAM 4GB/ HDD 500GB/ SFF', 'HP Compaq 6300/ i5-3gen/ RAM 4GB/ HDD 250GB/ TWR', 'HP 6300 Pro/i5-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'Terra / i5-3gen/ RAM 4GB/ HDD 250GB/ TWR', 'HP Compaq 8100 / i5-1gen/ RAM 4GB/ DISK 0GB/ TWR', 'Bluechip / i7-4gen/ RAM 4GB/ HDD 250GB/ TWR', 'No Name i5-4gen/ RAM 4GB/ HDD 250GB/ SFF', 'FTS Esprimo P9900 / i5-1gen/ RAM 4GB/ DISK 0GB/ TWR', 'Tarox / i7-1gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo P400/ G870/ RAM 4GB/ HDD 500GB/ TWR', 'Acer Veriton X2631G/ i5-4gen/ RAM 4GB/ HDD 250GB/ SFF', 'FTS Esprimo P910/ i5-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'FTS Esprimo P900/ i5-3gen/ RAM 4GB/ HDD 250GB/ TWR', 'FTS Esprimo E710 E90+/ i5-3gen/ RAM 4GB/ HDD 600GB/ SFF', 'FTS Esprimo E710 E90+/ i5-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'HP 8300 / i7-2gen/ RAM 4GB/ HDD 1TB/ SFF', 'No Name/ i5-2gen/ RAM 4GB/ HDD 250GB/ SFF', 'HP Compaq 8100 / i5-1gen/ RAM 4GB/ HDD 250GB/ TWR', 
'FTS Esprimo E700/ i5-2gen/ RAM 4GB/ HDD 320GB/ TWR', 'HP ProDesk 600 G1/ i3-4gen/ RAM 4GB/ HDD 250GB/ SFF', 'HP ProDesk 600 G1/ i3-4gen/ RAM 4GB/ HDD 400GB/ SFF', 'HP Elite 8300/ i3-3gen/ RAM 4GB/ HDD 350GB/ SFF', 'FTS Esprimo P720/ i3-4gen/ RAM 4GB/ HDD 360GB/ TWR', 'Dell OptiPlex 3020/ i5-4gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo P720 E85+/ i3-4gen/ RAM 4GB/ HDD 260GB/ TWR', 'Hyundai PENTINO G SERIES/ PENTIUM/ RAM 4GB/ DISK 0GB/ SFF', 'FTS Esprimo P510/ i3-2gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo P700 E85+/ i5-2gen/ RAM 4GB/ DISK 0GB/ TWR', 'Lenovo ThinkCentre M82/i5-3gen/ RAM 4GB/ HDD 250GB/ TWR', 'Acer Veriton M4620G/ i3-2gen/ RAM 4GB/ DISK 0GB/ TWR', 'FTS Esprimo P700 E85+/ i5-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'Acer Veriton M2610G/ i5-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'HP Compaq 6200 Pro/ i5-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'Dell T1500/ i5-1gen/ RAM 4GB/ HDD 250GB/ TWR', 'No Name Gigabyte B75M/ i7-3gen/ RAM 2GB/ DISK 0GB/ TWR', 'HP Compaq Pro 6300/ i5-3gen/ RAM 4GB/ HDD 300GB/ TWR', 'HP Elite 8300/ i3-3gen/ RAM 4GB/ HDD 160GB/ TWR', 'FTS Esprimo P920/ i5-4gen/ RAM 4GB/ DISK 0GB/ TWR', 'Dell OptiPlex 3010/ i5-3gen/ RAM 4GB/ DISK 0GB/ SFF', 'Dell OptiPlex 3010/ i3-4gen/ RAM 4GB/ HDD 320GB/ SFF', 'HP ProDesk 600 G1/ G1820/ RAM 2GB/ DISK 0GB/ SFF', 'HP ProDesk 600 G1/ G1820/ RAM 4GB/ DISK 0GB/ SFF', 'Hyundai Pentino Business F/ PENTIUM/ RAM 4GB/ HDD 500GB/ SFF', 'HP Compaq 8000 / E8500/ RAM 4GB/ HDD 250GB/ SFF', 'Dell OptiPlex 990/ i3-2gen/ RAM 4HB/ HDD 250GB/ TWR', 'FTS Esprimo P720 E90+/ i5-2gen/ RAM 4GB/ HDD 250GB/ TWR', 'Dell OptiPlex 3020/ i5-4gen/ RAM 4GB/ DISK 0GB/ SFF', 'FTS Esprimo E720 E85+/ G3260/ RAM 4GB/ HDD 300GB/ SFF', 'Dell OptiPlex 390/ i5-2gen/ RAM 4GB/ DISK 0GB/ SFF']

racunari = ['Dell Laptop E7240/ i5-5gen/ 12,5"/ RAM 8GB/ SSD256/ B Klasa', 'LEN Laptop L440/ 3550M/ 14"/ RAM 4GB/ HDD 500GB','HP Elite 8300/ i3-3gen/ RAM 4Gb/ HDD 320GB/ SFF', 'Hyundai G-Series I7 /3 gen /4 GB/500 GB/ M. tower', 'FTS Esprimo D756 I5-6400/4 GB/500 GB/SFF', 'HP ProDesk 600 G1/ i3-4gen/ RAM 4GB/ HDD 250GB/ SFF', 'Exone/i5-2 gen/ RAM 4GB/HDD 500GB TWR']

# proizvod = 'No Name / i3-2gen/ RAM 4GB/ HDD 250GB/ asdffs TWR'
# pprint.pprint(sorted(racunari))
# print(len(racunari))






# for racunar in racunari:
#     if '/' in racunar:
#         podaci_o_proizvodu = re.findall(r'(?!\/).+?(?=\/)', racunar)
#         zadnji_string = re.findall(r')([^/]*$)', racunar
#         podaci_o_proizvodu.append(zadnji_string[0])
#         podaci_o_proizvodu = [i.strip() for i in podaci_o_proizvodu]
#         naziv_racunara = podaci_o_proizvodu[0]
#         proizvodjac = None
#         procesor_proizvodjac = None
#         procesor = None
#         disk = None
#         ram = None
#         print('naziv:',naziv_racunara)
        
#         for naziv in podaci_o_proizvodu:

#             if 'RAM' in naziv:
#                 ram = naziv           
#             if 'DISK' in naziv:
#                 disk_tip = 'HDD'
#                 disk = naziv
#                 # print('disk:', disk.replace('DISK', '').strip(), disk_tip)
#             elif 'HDD' in naziv:
#                 disk_tip = 'HDD'
#                 disk = naziv
#                 # print('disk:', disk.replace('HDD', '').strip(), disk_tip)
#             elif 'SSD' in naziv:
#                 disk_tip = 'SSD'
#                 disk = naziv
#                 # print('disk:', disk.replace('SSD', '').strip(), disk_tip)

#             if 'gen' in naziv:
#                 procesor_proizvodjac = 'Intel'
#                 procesor = naziv
# #
# #   DISK
# #

#         try:
#             disk = disk.replace('SSD', '').replace('HDD', '').replace('DISK', '').strip()
#         except:
#             disk = re.findall(r'[^\d]\d{2,3} *?GB', racunar)[0]
#             disk = disk[0]
#         try:        
#             disk2 = re.findall(r'\d+ *?GB', disk)
#             disk2 = disk2[0]
#             if disk2 == '0GB':
#                 disk2 = 'nema disk'
#                 disk_tip = ''
#                 print('disk2:', disk2, disk_tip)
#             else:
#                 disk_tip = 'HDD'
#                 print('disk2:', disk2, disk_tip)
#         except:
#             print('nije dobar string za disk')

# #
# #  RAM
# # 

#         try:
#             ram = ram.replace('Gb', 'GB').replace(' ', '').strip()
#         except:
#             ram = re.findall(r'[^\d]\d{1,2} *?GB', racunar)
#             ram = ram[0]
#         try:        
#             ram = re.findall(r'\d+ *?GB', ram)
#             ram = ram[0].replace(' ', '')
#             if ram == '0GB':
#                 ram = 'nema ram'
#         except:
#             print('nije dobar string za ram')
# #
# #   KUCISTE
# #

#         kuciste = zadnji_string[0].strip()
#         if 'TWR' in kuciste:
#             kuciste = 'Tower'
#         elif 'M Tower' in kuciste:
#             kuciste = 'Mini Tower'

# #
# #   PROIZVODJAC
# #

#         proizvodjac = re.findall(r'^\w+', naziv_racunara)[0]
#         if proizvodjac == 'FTS':
#             proizvodjac = 'Fujitsu'
#         if proizvodjac == 'No':
#             proizvodjac = 'No name'

#         print('ram:',ram)

#         print('kuciste', kuciste)

#         print('procesor:', procesor_proizvodjac, procesor)

#         print('proizvodjac:', proizvodjac)

#         print('------------------------------------------------------')



for racunar in racunari:
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
    except:
        print('Naziv proizvoda vjerovatno nije dobar')
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


    print(racunar)
    print('HD:', disk_velicina, disk_tip)
    print('RAM:', ram)
    print('PROIZVODJAC:', proizvodjac)
    print('PROCESOR PROIZVODJAC:', procesor_proizvodjac)
    print('PROCESOR MODEL:', procesor_model)
    print('VELICINA EKRANA:', velicina_ekrana)


    print('==============================================')


