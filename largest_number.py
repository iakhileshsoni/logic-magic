num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))

# Check largest number
if num1 < num2:
    print("Largest number is : {}".format(num2))
else:
    print("Largest number is : {}".format(num1))


# less than 10, greater than 10 or equal to 10
num = int(input("Enter a first number : "))
if num < 10:
    print("Given number {} is less than 10".format(num))
elif num > 10:
    print("Given number {} is greater than 10".format(num))
else: 
    print("Given number {} is equal to 10".format(num))
