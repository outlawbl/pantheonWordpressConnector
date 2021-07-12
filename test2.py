import time
from console_progressbar import ProgressBar
from connections import wcapi

# pb = ProgressBar(total=100,prefix='Here', suffix='Now', decimals=3, length=50, fill='X', zfill='-')
# pb.print_progress_bar(2)
# time.sleep(5)
# pb.print_progress_bar(25)
# time.sleep(5)
# pb.print_progress_bar(50)
# time.sleep(5)
# pb.print_progress_bar(95)
# time.sleep(5)
# pb.print_progress_bar(100)

data = {
    "name": "Color",
    "slug": "pa_color7",
    "type": "select",
    "order_by": "menu_order",
    "has_archives": True
}

novi_attr = wcapi.post("products/attributes", data).json()
print(novi_attr)
novi_attr_id = novi_attr['id']
print(novi_attr_id)
