# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Lewis
# Section:      521
# Assignment:   Lab 6b
# Date:         10 08 2021
#

x = int(input("Enter a positive integer to compute the Collatz sequence: "))
count = 0
print("Here is the Collatz sequence starting at " + str(x) + ":")
# Repeats the Collatz sequence until x becomes 1
while(x!=1):
    print(x, end=", ")
    if(x%2==0):
        x = int(x/2)
    else:
        x = int(3*x + 1)

    count += 1
print(x)
print("It took", count, "iterations to reach 1")