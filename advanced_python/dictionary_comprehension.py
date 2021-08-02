# Dictionary comprehension
# To create dictionary with simple code
 
name_age_dict ={
    "mahdi"  : 30,
    "hasan"  : 40,
    "mahmud" : 30
}

num_dict = {}
for num in range(1, 30):
    num_dict[num] = num **3

print("num_dict",num_dict)



print("                  ")




num_dict_comp = { numb: numb**3 for numb in range(1,50)}
print("num_dict_comp:",num_dict_comp)



print("                  ")



num_dict_comp_1 = { numb: numb**3 for numb in range(1,50) if numb % 2 == 0}
print("num_dict_comp_1:",num_dict_comp_1)



print("                  ")



num_dict_comp_2 = { numb: numb**3 for numb in range(1,50) if numb % 2 == 1}
print("num_dict_comp_2:",num_dict_comp_2)



print("                  ")



num_dict_comp_3 = { numb: numb**3 for numb in range(1,50) if numb % 2 == 0 if numb % 5 == 0}
print("num_dict_comp_3:",num_dict_comp_3)



print("                  ")



num_dict_comp_4 = { numb: numb**3 for numb in range(1,50) if numb % 2 == 1 if numb % 5 == 0}
print("num_dict_comp_4:",num_dict_comp_4)



print("                  ")



num_dict_comp_5 = { numb: numb**3 if numb % 2 == 0 else "Odd" for numb in range(1,50)}
print("num_dict_comp_5:",num_dict_comp_5)



print("                  ")



num_dict_comp_6 = { numb: numb**3 if numb % 2 == 0  else numb**2 for numb in range(1,50)}
print("num_dict_comp_6:",num_dict_comp_6)


print("                  ")

name_age_dict ={
    "mahdi"  : 16,
    "hasan"  : 20,
    "mahmud" : 24,
    "masnun" : 14,
    "jamal"  : 45,
    "Razia"  : 40
}

age_dict = {name:"old" if age >= 40 else "Young" for name, age in name_age_dict.items()}
print("Age_dict:",age_dict)





