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
    def inner(*args, **kwargs):
        greet = func(*args, **kwargs)
        print(greet.upper())
        return func(*args, **kwargs)
    return inner


def remove_whitespace(func):
    def inner(*args, **kwargs):
        greet = func(*args, **kwargs)
        print(greet.strip())
        return func(*args, **kwargs)
    return inner

'''
@make_uppercase
def say_hello():
    return "Hello world"

say_hello()

@make_uppercase 
def hello_my_guest():
    return "My Guest,welcome to home"

hello_my_guest()
'''


@remove_whitespace
@make_uppercase
def small_to_upper(msg):
    return msg 

small_to_upper("Hello World")





















