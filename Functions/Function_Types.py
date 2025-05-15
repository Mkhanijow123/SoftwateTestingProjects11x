#1. The can't retrun --> non retrun
#means No argument/parameter then No return and there is No retrun key word

# def greet():
#     print("Hello")
#
# greet()

#2. No return Type and with Argument/Parameter
# def greet_by_name(name):
#     print("Hello", name)
#
# greet_by_name("MOnika")

#No retrun type and with default Argument

# def say_hello_default(name="Monika"):
#     print("Hello", name.upper())
#
# say_hello_default()

#multiple default arguments
# def say_hello_default(name="A", name2="B"):
#     print("Hello", name,name2)
#
# say_hello_default()
# say_hello_default(name="Monika",name2="Khanijow")

#argument + return value
def cal(a,b):
    return(a+b)
sum=cal(100,10)
print(sum)