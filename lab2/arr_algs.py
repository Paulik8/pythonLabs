mas = [0, 4, 10, 6, 657, 35, 3456, 2]


def minimum(mas):
    return min(mas)

def sa(mas):
    sum = 0
    for n in mas:
        sum = sum + n
    return sum/len(mas)


print (minimum(mas))
print (sa(mas))