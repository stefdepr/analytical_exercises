from collections import Counter

customer_purchases = {"jack": [1, 3, 1, 1, 2, 4, 5, 3, 1, 3, 3],
                      "jill": [4, 1, 1, 3, 7, 8, 4, 4, 2],
                      "john": [6, 7, 8, 8, 8, 4, 5, 9, 2, 1, 3, 3, 5, 1, 6, 7, 6],
                      "lisa": [5, 8, 5, 1, 6]}

print("dikkn")
def get_num_purchases(cust_purchases):
    num_purchases = dict()

    for name, products in cust_purchases.items():
        list_prod_id = dict()
        for product_id in products:
            if product_id not in list_prod_id:
                list_prod_id[product_id] = 0
            list_prod_id[product_id] += 1
        num_purchases[name] = list_prod_id

    return num_purchases

print(get_num_purchases(customer_purchases))
