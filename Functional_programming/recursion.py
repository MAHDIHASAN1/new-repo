# Recursion Function
# Function calls himself, recursion function

#def add(a, b):
#    add()
#   return a + b

#print(add(2, 3))


# factorial

1 * 2 * 3 * 4

1 * 2 * 3



def factorial(numb):
    if numb ==1:
        return 1
    else:
        current_num = numb - 1
        return numb * factorial(current_num)

print(factorial(3))
print(factorial(4))
print(factorial(100))

# # 1st step:
#    3 * factorial(2)

# # 2nd step:
#   3 * 2* factorial()

# # third step:
#    3 * 2 * 1


#def recursive():
#    print("I am from a recursive")
#    return recursive()

#recursive()




































