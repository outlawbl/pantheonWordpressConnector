from connections import db
from connections import wcapi
cur = db.cursor()

select_kategorije = "select C.acName as acClassif2Name from  tHE_SetItemCateg C"

def query_db(query, args=(), one=False):
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
            for i, value in enumerate(row)) for row in cur.fetchall()]
    return (r[0] if r else None) if one else r

cur.execute(select_kategorije)
pantheon_kategorije = query_db(select_kategorije)

# insert category

def insert_categories():
    for item in pantheon_kategorije:
        kategorija = {}
        kategorija['name'] = item['acClassif2Name']
        wcapi.post("products/categories", kategorija).json()
        print(wcapi.post("products/categories", kategorija).json())

