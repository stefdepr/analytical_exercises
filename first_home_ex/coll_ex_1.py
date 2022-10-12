customers = {"jack": True,
             "jill": False,
             "tom": False,
             "jade": True,
             "thomas": False,
             "math": False,
             "nicholas": False,
             "abigail": True,
             "eric": False}

quantity_cust = len(customers)

count = 0
for left in customers.values():
    print(left)
    if left == True:
        count += 1
#or because true = 1
customers_left = sum(customers.values())

percentage = round(count/quantity_cust * 100, 2)


print(f'{percentage}% left the company.')
