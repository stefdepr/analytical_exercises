# initialize a dictionary
cust_dict = dict()

# define path were file will is stored
file_path = "./customer_info_ex.csv"

# open the file
with open(file_path, "r") as f:
    # initialize cust id
    cust_id = 0

    # loop through the lines
    for line in f:
        # remove newline 
        line = line.replace("\n", "")
        # split by separater
        key_vals = line.split(";")
        # initialize cust info
        cust_info = dict()
        # loop through key vals
        for key_val in key_vals:
            # get every key and val
            key, val = key_val.split(":")
            # add to cust info
            cust_info[key] = val
        # add to cust dict
        cust_dict[cust_id] = cust_info
        # update cust id
        cust_id += 1