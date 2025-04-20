#Write a program to take a user age 21 and let him know if he can go to the club.

age=(int(input("Enter your age : \n")))

if age >= 21:
    print("Allowed to go to  the club")
elif type(age) != str:
    print("Not allowed")
else:
    print("Thanks for sharing your age")


# Logic building formula :
# User input i/p -->data type -->int
#o/p ->string -> user if he can go or not

#step 2 : Rough logic (Brute force)
#age > 21 "print can go "
#age < 21 "print can't go "

#step3 : write the logic

#step 4: check for the edge cases
#we should consider edge cases such as:
#Negetive ages or extremly high values  -> program will break
#Non Numeric input  -ABC
#Age which is valid >130

#step 5: Optimize the code
#Handle all the edges
