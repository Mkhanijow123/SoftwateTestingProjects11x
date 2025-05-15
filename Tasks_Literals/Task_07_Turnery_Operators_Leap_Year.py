# Leap Year calculate


leap_year = int(input("Enter a year\n"))


def check_leap_year():
    if (leap_year % 4 == 0) or (leap_year % 400== 0):

           print("its a leap year")
    else:
             print("Not a leap year")

check_leap_year()
