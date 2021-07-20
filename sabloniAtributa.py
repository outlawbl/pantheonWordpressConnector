from wcAtributiTxt import wc_atributi
#Svi sabloni
svi_sabloni = ['sec_class_0142', 'sec_class_0142']

# Laptopi
sec_class_0142 = ['Proizvođač', 'Dijagonala ekrana', 'Rezolucija ekrana', 'Touch screen', 'Procesor.Tip', 'Procesor.Proizvođač', 'Memorija.Tip', 'Memorija.Brzina', 'Hard Disk.Velicina', 'SSD Disk.Velicina', 'Grafika', 'Optika', 'Boja', 'Operativni system', 'Garancija']

# Laserski stampaci
sec_class_0050 = {'attr1':4, 'attr2':5, 'attr3':6}


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
