from pantheonArtikli import pantheon_neaktivni_artikli
from wcArtikliTxt import wcArtikli
from connections import wcapi


def brisanje_neaktivnih_artikala():
    wcartikli = []

    for grupa in wcArtikli:
        for artikal in grupa:
            wcartikli.append(artikal)

    for pt_artikal in pantheon_neaktivni_artikli:
        for wc_artikal in wcartikli:
            if pt_artikal['acIdent'] == wc_artikal['sku']:
                print(wc_artikal['name'], wc_artikal['sku'])
                id = wc_artikal['id']
                # print(wcapi.delete(f"products/{id}", params={"force": True}).json())

brisanje_neaktivnih_artikala()
