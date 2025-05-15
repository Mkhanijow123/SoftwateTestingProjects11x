# creat a program to sum of
# three number from  the user input
# if user doesn't enter any number use default as 100,200,300


# No return type only defualt value
a = (int(input("Enter a number")))
b = (int(input("Enter a number")))
c = (int(input("Enter a number")))

def _num(num1=100, num2=200, num3=300):

    return (num1 + num2 + num3)

result=_num(a, b, c)
print (result)

result2 =_num()
print(result2)

result3=_num(num1=100, num2=600,num3=800)
print(result3)