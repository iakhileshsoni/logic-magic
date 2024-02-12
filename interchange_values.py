# Accept two numbers and interchange their values

num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))

# Method-1 Using third variable
# temp = num2
# num2 = num1
# num1 = temp

# Method-2 By swapping each other
num1, num2 = num2, num1

print("After interchange Number1 is : {} and Number2 is : {} ".format(num1, num2))