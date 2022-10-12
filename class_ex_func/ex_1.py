list_1 = [3, 5, -1, 5, 2, 10]
list_2 = [3, 4, "banana", 4, 2, "apple"]


def sum_of_list(list):
    if all([isinstance(item, int) for item in list]):
        return (sum(list))
    else:
        return None

print(sum_of_list(list_1))
print(sum_of_list(list_2))
