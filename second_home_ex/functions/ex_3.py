cust_dict = {"jack": {"products": ["apple", "chocolate", "salad"], "quantities": [1, 2, 1]},
             "jill": {"products": ["chips", "sausage", "carrots", "bread"], "quantities": [3, 1, 1, 2]},
             "john": {"products": ["pasta", "cookies", "steak", "chocolate"], "quantities": [1, 2, 3, 1]},
             "sarah": {"products": ["banana", "tomato", "salad", "bread"], "quantities": [4, 6, 1, 1]},
             "michael": {"products": ["milk", "chips"], "quantities": [1, 1]}}

prices = {"apple": 1.2,
          "chocolate": 2.3,
          "chips": 1.6,
          "sausage": 3.4,
          "carrots": 1.2,
          "pasta": 1.4,
          "cookies": 2.7,
          "milk": 2.0,
          "steak": 4.5,
          "banana": 1.2,
          "tomato": 1.4,
          "salad": 1.6,
          "bread": 1.3}


def cust_rev(dict_cust, dict_prices):
    return_dict = {}
    for name, values in dict_cust.items():
        total_one_customer = 0
        for product, quantity in zip(values["products"], values["quantities"]):
            value_product = dict_prices[product]
            total_one_product = value_product * quantity
            total_one_customer += total_one_product
        return_dict[name] = total_one_customer
    return return_dict

print(cust_rev(cust_dict, prices))

