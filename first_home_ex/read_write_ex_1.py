customer_list = ["jack---belgium---02/260.05.02---9080",
                 "sarah---belgium---02/261.45.11---8192",
                 "jill---belgium---02/288.03.12---1030",
                 "tom---belgium---02/251.21.78---9103",
                 "john---belgium---02/278.05.98---7348",
                 "elisa---belgium---02/291.99.81---9080"]

with open("read_write_ex_1", "w") as f:
    for customer in customer_list:
        name, country, phone, postal = customer.split('---')

        f.write(f"name:{name};")
        f.write(f"country:{country};")
        f.write(f"phone:{phone};")
        f.write(f"postal:{postal};\n")


