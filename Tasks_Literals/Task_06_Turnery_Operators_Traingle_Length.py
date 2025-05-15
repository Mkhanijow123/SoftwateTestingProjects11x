# Write a program that classifies a triangle based on the side lengths. Given three input values representing the lengths of the sides, Determine if the triangle is equilateral(all sides are equal)
# And isosceles(two sides are equal) or scalene(No sides are equal) Use the if-else statement classify the traingle.
# Task_06

side1 = float(input("Enter the length of side1:\n"))
side2 = float(input("Enter the length of side2: \n"))
side3 = float(input("Enter the length of side3: \n"))

if side1 == side2 == side3:
    print("All sides are equal - Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Two sides are equal - Isosceles triangle")
else:
    print("No sides are equal  - Scalene triangle")


# promod way:

