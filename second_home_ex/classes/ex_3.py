from ex_1 import Company


class DaughterCompany(Company):

    def __init__(self, name, location):
        Company.__init__(self, name, location)
        self.name = name
        self.location = location
        self.cust_purch_hist = {}

    def shared_customers(self, company):
        mother = set(Company.getCustomers(company))
        daughter = set(self.getCustomers())
        return mother.intersection(daughter)
