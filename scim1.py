# a expense splitter after an event with friends (very basic) -- learn variables , data types , arithemetic , f strings
event_name=input("What did we gather for..? ")

group_size =int(input("how many people came including the host ? "))

cost = float(input("Total bill for the event ( excluding service charge)").replace(",",""))

service_percent = int(input("what percent was the service charge? "))

service_cost = float(cost * service_percent / 100)

total_cost = float(cost + service_cost)

costpp = float(total_cost / group_size)

print(f"so guys the total bill was {total_cost} which includes the service charge of {service_cost}. \n so each person owes anna {costpp:.2f}")

