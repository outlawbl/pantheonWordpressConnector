from wcArtikliTxt import wcArtikli
from connections import wcapi

mobilni_telefoni = '[ao_descript-custom category_ao_slug="mobilni-telefoni"][/ao_descript-custom]'
desktop_racunari = '[ao_descript-custom category_ao_slug="desktop-racunari"][/ao_descript-custom]'
racunari_polovni = '[ao_descript-custom category_ao_slug="desktop-racunari"][/ao_descript-custom]'
alf_om_racunari = '[ao_descript-custom category_ao_slug="alf-om-racunari"][/ao_descript-custom]'
monitori_racunari_i_komponente = '[ao_descript-custom category_ao_slug="monitori-racunari-i-komponente"][/ao_descript-custom]'
televizori = '[ao_descript-custom category_ao_slug="televizori"][/ao_descript-custom]'
fotoaparati = '[ao_descript-custom category_ao_slug="fotoaparati"][/ao_descript-custom]'
slusalice = '[ao_descript-custom category_ao_slug="slusalice"][/ao_descript-custom]'
hi_fi_zvucnici = '[ao_descript-custom category_ao_slug="hi-fi-zvucnici"][/ao_descript-custom]'
laserski = '[ao_descript-custom category_ao_slug="laserski"][/ao_descript-custom]'
ink_jet = '[ao_descript-custom category_ao_slug="ink-jet"][/ao_descript-custom]'
laserski_mfc_uredaji = '[ao_descript-custom category_ao_slug="laserski-mfc-uredaji"][/ao_descript-custom]'
computer_cases = '[ao_descript-custom category_ao_slug="computer-cases"][/ao_descript-custom]'
laptopi_polovni = '[ao_descript-custom category_ao_slug="computer-cases"][/ao_descript-custom]'
hard_diskovi = '[ao_descript-custom category_ao_slug="hard-diskovi"][/ao_descript-custom]'
bar_kod_citaci = '[ao_descript-custom category_ao_slug="bar-kod-citaci"][/ao_descript-custom]'
maticna_ploca_komponente_racunari_i_komponente = '[ao_descript-custom category_ao_slug="maticna-ploca-komponente-racunari-i-komponente"][/ao_descript-custom]'
procesori_komponente_racunari_i_komponente = '[ao_descript-custom2 category_ao_slug="procesori-komponente-racunari-i-komponente"][/ao_descript-custom2]'
graficke_karte = '[ao_descript-custom2 category_ao_slug="graficke-karte"][/ao_descript-custom2]'
memorije_za_racunar = '[ao_descript-custom2 category_ao_slug="memorije-za-racunar"][/ao_descript-custom2]'
napajanja = '[ao_descript-custom2 category_ao_slug="napajanja"][/ao_descript-custom2]'
usb_flash = '[ao_descript-custom2 category_ao_slug="usb-flash"][/ao_descript-custom2]'
web_kamere = '[ao_descript-custom2 category_ao_slug="web-kamere"][/ao_descript-custom2]'
ruteri = '[ao_descript-custom2 category_ao_slug="ruteri"][/ao_descript-custom2]'
svicevi = '[ao_descript-custom3 category_ao_slug="svicevi"][/ao_descript-custom3]'
eksterni_diskovi = '[ao_descript-custom2 category_ao_slug="eksterni-diskovi"][/ao_descript-custom2]'
stampaci_za_naljepnice = '[ao_descript-custom2 category_ao_slug="stampaci-za-naljepnice"][/ao_descript-custom2]'
kucista_komponente_racunari_i_komponente = '[ao_descript-custom2 category_ao_slug="kucista-komponente-racunari-i-komponente"][/ao_descript-custom2]'
tastature = '[ao_descript-custom2 category_ao_slug="tastature"][/ao_descript-custom2]'
misevi = '[ao_descript-custom2 category_ao_slug="misevi"][/ao_descript-custom2]'

shortcodovi = ['mobilni_telefoni', 'desktop_racunari', 'alf_om_racunari', 'monitori_racunari_i_komponente', 'televizori', 'fotoaparati', 'slusalice', 
'hi_fi_zvucnici', 'laserski', 'ink_jet', 'laserski_mfc_uredaji', 'computer_cases', 'laptopi_polovni', 'hard_diskovi', 'bar_kod_citaci', 'maticna_ploca_komponente_racunari_i_komponente',
'procesori_komponente_racunari_i_komponente', 'graficke_karte', 'memorije_za_racunar', 'napajanja', 'usb_flash', 'web_kamere', 'ruteri', 'svicevi', 'eksterni_diskovi', 'stampaci_za_naljepnice',
'kucista_komponente_racunari_i_komponente', 'tastature', 'misevi']
shortcodovi = ['bar_kod_citaci']


for grupa in wcArtikli:
    for artikal in grupa:
        id = artikal['id']
        for cat in artikal['categories']:
            kategorija_slug = cat['slug'].replace('-', '_')
            if kategorija_slug in shortcodovi and artikal['short_description'] != '':
                try:
                    data = {
                        "short_description" : f"{eval(kategorija_slug)}"
                    }
                    wcapi.put(f"products/{id}", data).json()
                    print('Update-ovan je:', artikal['name'])
                except:
                    print('Kategorija', kategorija_slug, 'nema svoj shortcode')