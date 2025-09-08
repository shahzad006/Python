
#?-------------------------------- Decorators -------------------------------- #

def main(fun):
    def wrapper():
        print("Wellcome")
        fun()
        print("Good bye")
    return wrapper()

@main
def functions():
    print("Muhammad Shahzad")



# ---------------------------------------------------------------------------- #


# Write a decorator that prints "Function is being called" before a function runs. Apply it to a function that prints "Hello World".


def print_decorator(func):
    def wrapper_function():
        print("Function is being called")
        func()
    return wrapper_function

@print_decorator
def hello():
    print("Hello World")


hello()


# ---------------------------------------------------------------------------- #

def decorator_function(func):
    def wrapper_function():
        result = func()
        return result * 10
    return wrapper_function


@decorator_function
def num():
    return 5


print(num())  



# ---------------------------------------------------------------------------- #


