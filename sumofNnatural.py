def sumofNnatural(num1):
    result = (num1 * (num1 + 1))
    result = result / 2
    return result

number1 = float(input("Enter the number"))

if number1 <= 0:
    print("Enter a valid number")
else:
    result_new = sumofNnatural(number1)
    print("Sum of N natural numbers :", result_new) 
