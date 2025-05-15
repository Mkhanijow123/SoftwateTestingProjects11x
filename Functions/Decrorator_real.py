import time


def decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        print("end")

    return wrapper()


@decorator
def test_ui_2():
    print("Hello decorators")


test_ui_2()
