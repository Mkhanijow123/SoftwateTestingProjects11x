def decorator(func):
    def wrapper():
        print("good morning")
        print("start the browser")
        func()
        print("Thanks for using")
        print("Quit the run")

    return wrapper()

@decorator
def hello():
    print("Hello Everyone")

hello()
