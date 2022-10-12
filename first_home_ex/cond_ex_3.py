import re

l = ["emma-1021", "john-304", "jack-3041", "sarah-991"]

shortlist_dict = {}
for name_spendings in l:
    spendings = re.sub('[^0-9]', '', name_spendings)
    name = re.sub('[^a-z]', '', name_spendings)
    #print(name, spendings)
    #or
    name_1, spendings_1 = name_spendings.split("-")

    if int(spendings) > 1000:
        shortlist_dict[name] = spendings

print(shortlist_dict)



