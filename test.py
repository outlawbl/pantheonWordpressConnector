from datetime import datetime

now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d%m%H%M%S")
print("date and time =", dt_string)	

print(datetime.now().strftime("%d%m%H%M%S"))