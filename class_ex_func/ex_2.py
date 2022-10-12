rev_cust_dict = {"shop_1": {"total_rev": 203041, "num_cust": 3040, "country": "Belgium"},
                 "shop_2": {"total_rev": 4030, "num_cust": 5056, "country": "Japan"},
                 "shop_3": {"total_rev": 49595, "num_cust": 405, "country": "Belgium"},
                 "shop_4": {"total_rev": 3045, "num_cust": 102, "country": "Japan"},
                 "shop_5": {"total_rev": 3001, "num_cust": 601, "country": "Japan"},
                 "shop_6": {"total_rev": 5691005, "num_cust": 301, "country": "Belgium"}}

def calc_avg_rev_per_cust(rev_dict, shop):

    #get revenue
    if rev_dict[shop]["country"] == "Japan":
        revenue = rev_dict[shop]["total_rev"] * 8
    else:
        revenue = rev_dict[shop]["total_rev"]

    #get # of customers
    customers = rev_dict[shop]["num_cust"]

    #get avg per customer
    avg = round(revenue/customers, 2)

    #get shop
    shop_dict = rev_dict[shop]

    return print(f'Average revenue per customer in euros '
                 f'for {shop} is {avg}')

calc_avg_rev_per_cust(rev_cust_dict, "shop_1")
calc_avg_rev_per_cust(rev_cust_dict, "shop_4")