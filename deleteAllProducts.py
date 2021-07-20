from connections import wcapi
from woocommerceArtikli import woocommerce_artikli, id_woocommerce_artikala
import time
# from progressBar import progressBar
from console_progressbar import ProgressBar

def delete_all_products():
    for artikal in woocommerce_artikli:
        obrisani_artikli = 0
        for x in artikal:
            pb = ProgressBar(total=len(id_woocommerce_artikala),prefix='Brisanje svih artikala', suffix=f'{obrisani_artikli}/{len(id_woocommerce_artikala)}', decimals=3, length=50, fill='█', zfill='-')
            wcapi.delete(f"products/{x['id']}", params={"force": True}).json()
            obrisani_artikli += 1
            pb.print_progress_bar(obrisani_artikli)

# delete_all_products()

