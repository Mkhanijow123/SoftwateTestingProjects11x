#Grade Calculate:
#Write a program that calcluates and displays the letter grade
#for a given numerical score (e.g , A , B , C, D or F)
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D :60-69
# E :0-59

score =int(input("Enter a score\n"))

if score>=90 and score<=100:
    print("A")
elif score >=80 and score <=89:
    print("B")
elif score >=70 and score <=79:
    print("C")
elif  score >=60 and score <=69:
    print("D")
elif score >=0 and score <=59:
    print("you are fail")
elif score >100:
    print("You are a genius !!")
else:
    print(" none is above, you can't get any score")


#Logic Bulding Formula

# 1-> user input -> score or marks ->int
#2-> o/p ->str -> A or B...

# score >=90 and score <=100- > "A"
#score >=80 and score <=89-> "B"
