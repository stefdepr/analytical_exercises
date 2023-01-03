from ex_1 import Company


class DaughterCompany(Company):

    def __init__(self, name, location, mother_company):
        #super().__init__(name, location)
        self.mother_company = mother_company
        self.name = name
        self.location = location
        self.cust_purch_hist = {}

    def shared_customers(self, company):
        mother = set(Company.getCustomers(company))
        daughter = set(self.getCustomers())
        return mother.intersection(daughter)
