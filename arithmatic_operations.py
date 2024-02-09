
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

# Addition of numbers
sum = num1 + num2
print("Sum of {} and {} is : {}".format(num1, num2, sum))
print()


# Subtraction of numbers
if num1 > num2:
    sub = num1 - num2
elif num1 < num2:
    sub = num2 - num1
else:
    sub = num1 - num2 # or simply sub = 0

print("Subtraction of {} and {} is : {}".format(num1, num2, sub))
print()


# Multiplication of numbers
mul = num1 * num2
print("Multiplication of {} and {} is : {}".format(num1, num2, mul))
print()


# Division of numbers
if num1 > num2 and (num1 or num2 != 0):
    div = num1/num2
elif num1 < num2  and (num1 or num2 != 0):
    div = num2/num1
elif num1 == num2:
    div = num1/num2 # or div = 1
print("Division of {} and {} is : {}".format(num1, num2, div))
