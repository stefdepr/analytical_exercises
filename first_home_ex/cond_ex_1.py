rev_cust_dict = {"shop_1": {"total_rev": 203041 , "num_cust": 3040, "country": "Belgium"},
                 "shop_2": {"total_rev": 4030, "num_cust": 5056, "country": "Japan"},
                 "shop_3": {"total_rev": 49595, "num_cust": 405, "country": "Belgium"},
                 "shop_4": {"total_rev": 3045, "num_cust": 0, "country": "Japan"},
                 "shop_5": {"total_rev": 3001, "num_cust": 601, "country": "Japan"},
                 "shop_6": {"total_rev": 5691005, "num_cust": 0, "country": "Belgium"}}

for rev, num in rev_cust_dict.items():
    if num['num_cust'] == 0:
        print("no customer information")
    else:
        if num['country'] == "Japan":
            revenue = num["total_rev"] * 8 / num['num_cust']
        else:
            revenue = num["total_rev"] / num['num_cust']

        print(f"{rev} has a revenue of {revenue} per customer")

