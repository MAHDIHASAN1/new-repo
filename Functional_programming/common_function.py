# map
# Iterable: string, list, tuple, set, dictionary

# map(function, iterable)
from functools import reduce

nums = [20, 40, 70, 30, 59, 547, 94]

print(map(lambda x: x **3, nums))
print(list(map(lambda x: x **3, nums)))
print(list(map(lambda x: x * 3, nums)))

def multiply(a):
    return a * 3

print(list(map(multiply, nums)))


######
######
######
######
######
######
######



# Filter function

# filter (function, iterable)

print(filter(lambda x: x % 5==0, nums))
print(list(filter(lambda x: x % 5==0, nums)))
print(list(filter(lambda x: x % 5==0, range(1,20))))
print(list(filter(lambda x: x ==10, range(1,300))))

def puls(a):
    return a % 5==0

print(list(filter(puls, nums)))


######
######
######
######
######
######
######


# reduce
from functools import reduce

num_list = [ 45, 23, 67, 75, 36,76]
print(reduce(lambda x, y: x * y,num_list))
print(reduce(lambda x, y: x * y,num_list, 100))















































