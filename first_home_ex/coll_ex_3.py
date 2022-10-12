cust_bel_1 = {"Jack", "Jill", "Elisa", "Tom"}
cust_bel_2 = {"John", "Nicholas", "Eric", "Elisa", "Rupert", "Jack"}
cust_fran_1 = {"Thomas", "Charlotte", "Naomi", "John", "Tom"}

#unique customers belgium
un_cust_belgium = set()

for name in cust_bel_1:
    un_cust_belgium.add(name)

for name in cust_bel_2:
    un_cust_belgium.add(name)

#or simpler with union
all_cust_belg = cust_bel_1.union(cust_bel_2)

#both customer in france and belgium
both_count_cust = un_cust_belgium.intersection(cust_fran_1)
