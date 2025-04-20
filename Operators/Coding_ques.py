import math

#write python to calculate the area of a circle its radius using formula
#*** area
#        steps 1 :
# i/o
#input --> r-> data type -->float
# pi =3.14
# power -> pow or **

#Step 2:
#rough logic - area =3.14 * pow(r,2)


radius =float(input("Enter a radius \n"))
# print(radius)
# area =3.14 * (radius **2)
# print("area of the circle is :" ,area)
# # print(f"area of the circle is : {area}")

# math.pi we can import math another way
print(math.pi)
area =math.pi * (radius **2)
print("area of the circle is :" ,area)

