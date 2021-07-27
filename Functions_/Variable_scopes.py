#Global scope
#Local scope
#Nonlocal scope

# x in global scope
# powerfull_number in local scope
#  

x = 10

def make_powerful(number):
    global powerfull_number
    powerfull_number = number ** x
    return powerfull_number


make_powerful(58)
print(x)
print(powerfull_number)
print("printing from global scope:",powerfull_number)





