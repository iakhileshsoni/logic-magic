num = int(input("Enter a number : "))

if num < 0:
    print("Given number {} is negative".format(num))
elif num > 0:
    print("Given number {} is positive".format(num))
else:
    print("Given number is zero")