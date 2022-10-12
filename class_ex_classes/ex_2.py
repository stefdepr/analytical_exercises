from ex_1 import Company

#question 1
my_company = Company('stef industries', 'Ghent',
                     {'apples', 'pears', 'peaches'})

#question 2
my_company.total_number_products_stock()

#question 3
my_company.add_product_stock('bananas')

#question 4
my_company.remove_product_from_stock('apples')

#question 5
print(my_company.stock)

