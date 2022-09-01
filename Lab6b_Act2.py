# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Lewis
# Section:      521
# Assignment:   Lab 6b
# Date:         10 08 2021
#

x = int(input("Enter an integer: "))
xSum = 0
xProduct = 1
# Sum
for i in range(1,x+1):
    xSum += i
print("The sum of all integers from 0 to", x, "is", xSum)
# Product
for j in range(2,x+1):
    xProduct *= j
print("The product of all integers from 1 to", x, "is", xProduct)