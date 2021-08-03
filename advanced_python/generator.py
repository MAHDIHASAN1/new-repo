# Generator

# Generator Function, Generator Expression

# Normal Function
def Normal_hello():
    return "Hello Mahdi Hasan"


# Generator Function
def gen_hello():
    yield "Hello Mahdi Hasan"

normal = Normal_hello()
print("Normal:",normal)

# Generator

gen = gen_hello()
print("genera:",gen)

































































