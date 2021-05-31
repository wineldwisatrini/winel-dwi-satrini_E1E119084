import random

def my_choice(data):
    return data[random.randrange(0, len(data) - 1)]
                                 
alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]
                                 
print(my_choice(alpha))
