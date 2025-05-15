#write a program that prints from 1-100.
# However for multiplies of 3 print "Frizz" instead of the number, and for multiples of 5, print "Buzz"
# For numbers that are multiples of both-3 and 5,print "FizzBuzz"(for, if loops)


for i in range(1,101):
        if i %3==0 and i % 5==0:
            print("Frizz")
        elif  i %3==0:
            print("Buzz")
        elif i %5==0:
            print("FizzBuzz")
        else:
            print(i)



