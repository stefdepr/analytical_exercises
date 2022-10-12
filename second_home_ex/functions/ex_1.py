def number_of_upper_char(string):
    return sum(1 for c in string if c.isupper())

string = "DikkeKinder "'çà(§'"éç(èA"

print(number_of_upper_char(string))

