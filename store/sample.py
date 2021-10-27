def decorator(func):
    def inner():
        print("Good morning")
        func()
        print("Good night")
    return inner


@decorator
def hello():
    print("Hello World")


@decorator
def pune():
    print("Hello Pune")


hello()
pune()
