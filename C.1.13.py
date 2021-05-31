my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def reverse(data):
    temp = []
    n = len(data) - 1
    for thing in range(n, -1, -1):
        temp.append(data[thing])
    return temp


print(my_list)

print(reverse(my_list))
