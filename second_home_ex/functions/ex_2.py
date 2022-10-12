shop_rev = {"shop_1": {"total_rev": 203041, "country": "Belgium"},
            "shop_2": {"total_rev": 4030, "country": "Japan"},
            "shop_3": {"total_rev": 49595, "country": "Belgium"},
            "shop_4": {"total_rev": 3045, "country": "Japan"},
            "shop_5": {"total_rev": 3001, "country": "Japan"},
            "shop_6": {"total_rev": 569100, "country": "Belgium"}}


def avg_rev_given_country(dict_shop, country):
    total_rev = 0
    count = 0
    for values in dict_shop.values():
        print(values)
        if values["country"] == country:
            total_rev += values["total_rev"]
            print(total_rev)
            count += 1

        if country == 'Japan':
            total_rev = total_rev * 8

    avg_rev = total_rev/count

    return avg_rev


print(avg_rev_given_country(shop_rev, 'Belgium'))
