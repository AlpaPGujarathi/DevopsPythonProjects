#Swappin two numbers without using third variable
#Author : Alpa Gujarathi

num1 = 30
num2 = 10

print("Before Swapping Numbers are : ", num1 , num2)
if  num1 > num2:
    num2 = num1 + num2
    num1 = num2 - num1
    num2 = num2 - num1
    print("Swap Numbers are : " ,num1 , num2)

elif num2 > num1:
    num1 = num2 + num1
    num2 = num1 - num2
    num1 = num1 - num2
    print("Swap Numbers are : ", num1 , num2)
    