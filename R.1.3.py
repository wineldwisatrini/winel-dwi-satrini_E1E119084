def minmax(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest


alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]

print(minmax(alpha))
