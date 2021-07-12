from connections import wcapi

a=1
while a < 1000:
    print(wcapi.delete(f"products/attributes/{a}", params={"force": True}).json())
    a+=1
