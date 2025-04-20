#find the max between 3 numbers

num1=int(input("Enter a num1 \n"))
num2=int(input("Enter a num2 \n"))
num3=int(input("Enter a num3 \n"))

if num1>=num2:
    print(" num1 max")
elif  num2 > num1 and num2 > num3:
    print("num2 max")
elif num3 >num2 and num3> num1:
    print("num3 max ")
else:
    print("No max value available")
