from ex_1 import Company
from ex_3 import DaughterCompany

company = Company('NV', 'Ghent')

company.add_new_cust("jill")
company.add_new_cust("jack")
company.add_new_cust("elisa")

print(company.cust_purch_hist)

company.update_purchase_history(['chips', 'cookies'], "jill")
company.update_purchase_history(['water', 'milk', 'bread'], "jack")
company.update_purchase_history(['steak'], "elisa")

print(company.cust_purch_hist)

company.update_purchase_history(['water', 'milk', 'cookies'], "jack")
company.update_purchase_history(['cola'], "elisa")

daughter = DaughterCompany('nikie', 'Russia')

daughter.add_new_cust('thomas')
daughter.add_new_cust('charlotte')
daughter.add_new_cust('jill')

daughter.update_purchase_history(['beer', 'chips'], 'thomas')
daughter.update_purchase_history(['wine', 'cheese', 'fish'], 'jill')

print(daughter.cust_purch_hist)
print(daughter.cust_stat('jill'))

print(daughter.shared_customers(company))

