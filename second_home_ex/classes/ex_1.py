class Company():

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cust_purch_hist = {}

    def add_new_cust(self, name):
        if name not in self.cust_purch_hist.keys():
            self.cust_purch_hist[name] = list()

    def delete_old_cust(self, name):
        self.cust_purch_hist.pop(name)

    def update_purchase_history(self, list_purchases, name):
        for purchase in list_purchases:
            self.cust_purch_hist[name].append(purchase)

    def cust_stat(self, name):
        unique = set(self.cust_purch_hist[name])
        return name, len(self.cust_purch_hist[name]), len(unique)

    def getCustomers(self):
        return list(self.cust_purch_hist.keys())