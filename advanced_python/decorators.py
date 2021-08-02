# Decorator 
#1 We can pass a function as a parameter for another function
# Higher order function(HOF)
#2 We can decaler a function inside another function
#3 We can return a function from another function




def make_uppercase(funct):
    pass


def say_hello(message):
    print(message)
    return message

say_hello("Hello Mahdi Hasan")
say_hello(123456)
say_hello(["Hello Mahdi Hasan"])
say_hello({"name" : "Mahdi Hasan"})


print("                  ")


def say_hello(message):

    def print_msg():
        
        def print_nested_msg():
            print(message)

        print_nested_msg()

    print_msg()

    return message

say_hello("Hello Mahdi Hasan")
say_hello(123456)
say_hello(["Hello Mahdi Hasan"])
say_hello({"name" : "Mahdi Hasan"})




print("                  ")


def say_hello(message):

    def print_msg():
        print(message)

    return print_msg

greeting = say_hello("Hello Mahdi Hasan")
greeting()
print("Greeting:",greeting)
 



