# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Lewis
# Section:      521
# Assignment:   Lab 6b
# Date:         10 08 2021
#

x = int(input("Enter a four-digit integer: "))
xString = str(x)
xUp = ""
xDown = ""
count = 0
# Adds 0s to the front if x is less than 4 digits
if(len(xString)<4):
    while(len(xString)!=4):
        xString = "0" + xString
# Sorts the digits into ascending order
if(len(xString)==4 and not(xString[0]==xString[1]==xString[2]==xString[3])):
    while(int(xString)!=6174):
        if(int(xString)<1000):
            print(int(xString), end=" > ")
        else:
            print(xString, end=" > ")
        while(xString[0]>xString[1] or xString[1]>xString[2] or xString[2]>xString[3]):
            if(int(xString[0])>int(xString[1])):
                xString = xString[1] + xString[0] + xString[2] + xString[3]
            elif(int(xString[1])>int(xString[2])):
                xString = xString[0] + xString[2] + xString[1] + xString[3]
            elif(int(xString[2])>int(xString[3])):
                xString = xString[0] + xString[1] + xString[3] + xString[2]
        xUp = xString
        xDown = xUp[3] + xUp[2] + xUp[1] + xUp[0]
        xString = str(int(xDown)-int(xUp))
        while(len(xString)!=4):
            xString = "0" + xString
        count += 1
    print(xString)
    print(x, "reaches", xString, "via Kaprekar's routine in", count, "iterations")
else:
    print(xString, end=" > ")
    print("0")
    print(x, "reaches 0 via Kaprekar's routine in 1 iterations")
    
