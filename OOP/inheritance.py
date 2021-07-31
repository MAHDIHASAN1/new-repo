
#Parent class / Base class
# child mathods and attributes will be used if the attribute and method name are same

class person:
    hands = 2
    legs = 2
    mouth = 1
    country = {
        "name" : "BD"
    }

    def __init__(self,first_name,last_name,country):
        self.first_n9ame = first_name
        self.last_name = last_name
        self.country = country
    def speak(myself,mgs):
        print("Hi, welcome to python master class",mgs )
    def speak_1(myself_1 , mgs_1):
        print("MAHMUD HASAN:" , mgs_1)
    def speak_2(myself_2 , mgs_2):
        print("MAHDI HASAN:" , mgs_2)


    def walk(self):
        print("start moving!")
        super()
    


#Child class

class student(person):
    def __init__ (self):
        pass
    
    def speak(self,mgs):
        print("Hi,",mgs)
        super().walk()


class morningStudent():
    pass

class eveningStudent(student):
    pass

student1 = student( )
student1.speak("How are you?")

#print(dir(student1))



class A:
    pass

class  B():
    pass

class D():
    pass

class c(A,B,D):
    pass