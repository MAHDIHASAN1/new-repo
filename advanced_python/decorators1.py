# first Decorator

def my_decorator(func):
    
    def inner():
        func()
        print("I am from decorator")
        func()
    
    return inner


def say_hello():
    print("hello bangladash")

greeting = my_decorator(say_hello)
greeting()


print("                      ")



def my_decorator(func):
    
    def inner():
        func()
        print("I am from decorator")
        
    
    return inner

@my_decorator
def say_hello():
    print("hello bangladash")


say_hello()


print("                            ")



def make_uppercase(func):
    def inner():
        greet = func()
        print(greet.upper())
    return inner

@make_uppercase
def say_hello():
    return "Hello world"

say_hello()
