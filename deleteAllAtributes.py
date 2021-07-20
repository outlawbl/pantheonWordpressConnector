from connections import wcapi

def deleteAllAtributes():
    a=1
    while a < 1000:
        print(wcapi.delete(f"products/attributes/{a}", params={"force": True}).json())
        a+=1
