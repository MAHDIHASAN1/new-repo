#stringFormatting
#####
full_info ="\nname:{0} \nvillage:{1} \nAge:{2}".format("'MAHDI HASAN'","'PIROJPUR'","'16'")
print("Full Info:", full_info)

#####
full_info ="name: {0}, village: {1}, Age: {2}".format("MAHDI HASAN","PIROJPUR",16)
print("Full Info:", full_info)

#####
full_info ="name: {name}, village: {village}, Age: {age}".format(name="MAHDI HASAN",village="PIROJPUR",age=16)
print("Full Info:", full_info)

#####
name = input("Please Enter Your Name:")
village = input("Please Enter Your village:")
Age = input("Please Enter Your Age:")
full_bio =f"name: {name}, village: {village}, Age: {Age}"
print("Full Info:", full_bio)