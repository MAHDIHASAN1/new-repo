# Generator

# Generator Function, Generator Expression

# Normal Function
def Normal_hello():
    return "Hello Mahdi Hasan"


# Generator Function
def gen_hello():
    n = 1
    print("First world num:",n)
    yield "Hello world"

    n += 1
    print("second world num:",n) 
    yield "Hello second world"

    n += 1
    print("third world num:",n) 
    yield "Hello third world"

    n += 1
    print("fourth world num:",n) 
    yield "Hello fourth world"

normal = Normal_hello()
print("Normal:",normal)

# Generator

gen = gen_hello()
print(next(gen))
print(next(gen))
print(next(gen))


def gen_power_two():
    number = 1
    while number < 20:
        yield number ** 2 
        number += 1

num_power = gen_power_two()

print(next(num_power))
print(next(num_power))
print(next(num_power))
print(next(num_power))

for i in num_power:
    print(i)

nums = [1, 2, 3, 4, 5]
nums = [num for num in range(1, 6 )]
print(nums)

gun_nums = (num for num in range(1, 20))
print(gun_nums)

print(next(gun_nums))
print(next(gun_nums))
print(next(gun_nums))
print(next(gun_nums))

for num in gun_nums:
    print("Number:",num)

    































































