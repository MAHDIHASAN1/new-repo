#Object oriented programming    / OOP

# Class name starts with a capital letter
# Function name starts with a small letter

# Property / Attributes,
# Functions / Methods
# Methods

#Structure to create real life person 

class person:
    hands = 2
    legs = 2
    mouth = 1
    country = {
        "name" : "BD"
    }

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def speak(myself):
        print("Hi, welcome to python master class" )
    def speak_1(myself_1 , mgs_1):
        print("MAHMUD HASAN:" , mgs_1)
    def speak_2(myself_2 , mgs_2):
        print("MAHDI HASAN:" , mgs_2)

# crate instance from class

hasan = person("Hasan","Mahdi")
mahdi = person("Mahdi","Hasan")
mahmud = person("Mahmud","Hasan")         
masnun = person("Masnun","Hasan")
razia = person("Razia","Bazom")
jamal = person("Jamal","Uddin")
mahfuza = person("Mahfuza","Bazom")
marfua = person("Marfua","Bazom")

        
print("mahdi legs:",mahdi.legs)
print("razia mouth:",razia.mouth)

print("MAHDI_HASAN'S first name and last name:",mahdi.first_name,mahdi.last_name)
print("JAMAL_UDDIN'S first name and last name:",jamal.first_name,jamal.last_name)

mahdi.speak()

mahmud.speak_1("What is your name?")
mahdi.speak_2("My name is Mahdi Hasan.and you?")

mahmud.speak_1("My name is Mahmud Hasan.")
mahdi.speak_2("How are you?")

mahmud.speak_1("I am fine.and you?")
mahdi.speak_2("I am fine too.")







class product:
    
    def __init__(self,incoming_name,incoming_price,incoming_color):
        self.name = incoming_name
        self.price = incoming_price
        self.color = incoming_color


pen = product("Econo",10,"white")
print("Pen Name:",pen.name)
print("Pen Price:",pen.price)
print("Pen Color:",pen.color)



computer = product("Product name:Lenovo""\n","Product price: 40000""\n","Product color: gray")

print(computer.name,computer.price,computer.color)



