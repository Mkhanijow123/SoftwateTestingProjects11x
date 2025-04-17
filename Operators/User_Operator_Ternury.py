# program if   age > 18 -allowed to vote
#else  -Not allowed

user_age =(int(input("Enter a age \n")))

# if user_age>=18 :
#     print("Yes you can go goa and vote")
# else:
#     print("You are not allowed ")


# Ternaury mode
# Never user turnery way also no one line code
# print("Yes you can go goa and vote" if user_age >= 18 else print(" You are not allowed"))

#Ternury mode 2 # Input added here as well
# Bad practice never write this way
print("Yes you can go goa and vote" if  (int(input("Enter a age \n")))  >= 18 else print(" You are not allowed"))