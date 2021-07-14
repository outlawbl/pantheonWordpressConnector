import re
import pprint

opis = 'Laptop Fujitsu H710 Workstation\r\nFSC Celsius H910 \r\nProizvoÄ‘aÄŤ: Fujitsu\r\nDijagonala ekrana: 17,3" LED  \r\nRezolucija ekrana: Full HD (1920x1080)\r\nProcesor.Tip: Intel Core i7 2620M - 3,4 GHz 2-nd Gen \r\nProcesor.ProizvoÄ‘aÄŤ: Intel\r\nMemorija.Tip: 8GB DDR3 \r\nHard Disk.Velicina: 500GB \r\nSSD Disk.Velicina: -\r\nGrafika: NVidia Quadrro 4000M 2 GB \r\nOptika: DVD-RW\r\nBoja: -\r\nTouch screen: Ne\r\nOperativni system: -\r\nGarancija:6 mjeseci'

atributi_iz_opisa = []

for red in opis.splitlines():
  atribut = {}
  kljuc_atributa = re.findall(r'.+?(?=:)', red)
  vrijednost_atributa = re.findall(r'(?<=:).*', red)
  if len(kljuc_atributa) > 0:
    atribut['name'] = kljuc_atributa[0].strip()
    options = []
    options.append(vrijednost_atributa[0].strip())
    atribut['options'] = options
    atributi_iz_opisa.append(atribut)

pprint.pprint(atributi_iz_opisa)