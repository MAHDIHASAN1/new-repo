#Default Argument
#Positional Argument
#Kewword Argument


def multiply(a, b):
    return a * b

print(multiply(40,100 ))




def multiply(a, b, c, d):
    return a * b * c * d

print(multiply(40,100,5,9 ))



def multiply(a, b=23):
    return a * b 

print(multiply(40))



def multiply(a=90, b=23):
    return a * b 

print(multiply(40))



def multiply_by_pi(a, pi=6.1614):
    return a * pi 

print(multiply_by_pi(40))


def multiply(a, b, c, d, e, f, g):
    return a * b * c * d

print(multiply(g=40, c=100, e=5, a=9, f=4,b=9, d=45))



def divide_by (*args):
    for number in args:
        print("divide by 2:",number/2)

      
divide_by(3,4,6,8,2,9,2,4,6,4,7,223,654,75,23234,1341)     
          





