class Company():

    #define constructor
    def __init__(self, name, location, stock):
        #define properties
        self.name = name
        self.location = location
        self.stock = stock

    #total number of stock
    def total_number_products_stock(self):
        print(len(self.stock))

    #add product to stock
    def add_product_stock(self, product):
        self.stock.add(product)

    #remove product from stock
    def remove_product_from_stock(self, product):
        self.stock.remove(product)
