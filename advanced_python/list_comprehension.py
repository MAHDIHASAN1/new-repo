# list comprehension

# MAHDI HASAN
# ["M", "A", "H", "D", "I", "H", "A", "S", "A", "N"]

name_chars =[]
print("name char list:",name_chars)





name = "MAHDI HASAN"
for char in name:
    name_chars.append(char)

print("Final list:",name_chars)






num_list = []
for number in range(5000):
    num_list.append(number)

print("num_list:",num_list)


# list comprehension



num_list_1 = [number for number in range(50) ]

print("num_list_1:",num_list_1)




name_1 = [name for name in "mahdi hasan"]

print("name:",name_1)





num_list_2 = [ number for number in range(50) if number % 2 == 0 ]

print("num_list_2:",num_list_2)




num_list_3 = [ number for number in range(50) if number % 2 == 0 if number % 5 == 0]

print("num_list_3:",num_list_3)




num_list_4 = [ number if number % 2 == 0 else "Odd" for number in range(50)]

print("num_list_4:",num_list_4)







num_list_5 = [ "Even" if number % 2 == 0 else "Odd" for number in range(50)]

print("num_list_5:",num_list_5)















