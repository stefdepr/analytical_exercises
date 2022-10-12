rev_cust_dict = {"shop_1": {"total_rev": 203041, "num_cust": 3040},
                 "shop_2": {"total_rev": 403010, "num_cust": 5056},
                 "shop_3": {"total_rev": 49595, "num_cust": 405},
                 "shop_4": {"total_rev": 30450, "num_cust": 0},
                 "shop_5": {"total_rev": 30501, "num_cust": 601},
                 "shop_6": {"total_rev": 5691005, "num_cust": 0}}

total_cust = 0
count = 0
for num in rev_cust_dict.values():
    if num['num_cust'] != 0:
        total_cust += num['num_cust']
        count += 1

avg_cust = total_cust/count


for rev, num in rev_cust_dict.items():
    try:
        avg_rev_cust = round(num["total_rev"] / num["num_cust"], 2)
        print(f'{rev} has an average revenue of {avg_rev_cust} per customer')
    except:
        avg_rev_cust = round(num["total_rev"] / avg_cust, 2)
        print(f'{rev} does not have any information regarding number of customers')
        print(f'When looking at average customer per shop we conclude an average of {avg_rev_cust}')