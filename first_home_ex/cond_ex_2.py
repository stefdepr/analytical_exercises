l = [5, 2, 1, 7, -4, 2]

highest_number = l[0]
for i in range(1, len(l)):
    if l[i] > highest_number:
        highest_number = l[i]
