from wcAtributiTxt import wc_atributi

# Laptopi
# sec_class_0142 = {'Proizvođač':'', 'Dijagonala ekrana':'', 'Rezolucija ekrana':'', 'Touch screen':'', 'Procesor.Tip':'', 'Procesor.Proizvođač':'', 'Memorija.Tip':'', 'Memorija.Brzina':'', 'Hard Disk.Velicina':'', 'SSD Disk.Velicina':'', 'Grafika':'', 'Optika':'', 'Boja':'', 'Operativni system':'', 'Garancija':''}

# Laserski stampaci
sec_class_0050 = {'attr1':4, 'attr2':5, 'attr3':6}

sec_class_0142 = ['Proizvođač', 'Dijagonala ekrana', 'Rezolucija ekrana', 'Touch screen', 'Procesor.Tip', 'Procesor.Proizvođač', 'Memorija.Tip', 'Memorija.Brzina', 'Hard Disk.Velicina', 'SSD Disk.Velicina', 'Grafika', 'Optika', 'Boja', 'Operativni system', 'Garancija']



# def sablonArtibuta(sec_class):
#     global atributi
#     atributi = []
#     for x in sec_class:
#         atributi.append(sec_class[x])
#     return atributi

# klasifikacija = 'sec_class_0142'

# sablonArtibuta(eval(klasifikacija))

# print(atributi)

def dodavanje_atributa(sec_class):
    brojac = 0
    atributi = []
    for naziv in sec_class:
        atribut = {}
        for a in wc_atributi:
            if a['name'] == naziv:
                atribut['id'] = a['id']
                atribut['name'] = a['name']
        atributi.append(atribut)
    return atributi
    brojac += 1

# dodavanje_atributa(eval(klasifikacija))
