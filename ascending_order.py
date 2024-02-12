# Take 3 numbers and print them in ascending order

# Method-1 Using if_else statement

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        x, y, z = num1, num2, num3
    else:
        x, y, z = num1, num3, num2

elif num2 < num1 and num2 < num3:
    if num1 < num3:
        x, y, z = num2, num1, num3
    else:
        x, y, z = num2, num3, num1

else:
    if num1 < num2:
        x, y, z = num3, num1, num2
    else:
        x, y, z = num3, num2, num1

# print("Numbers in ascending order are : ", x, y, z)


# Method-2 Using sort() in List

list1 = [num1, num2, num3]
list1.sort()

print("Numbers in Ascending order are : ", " ".join(map(str, list1)))


"""
In Python, map() is a built-in function that applies a specified function to each item in an iterable (like a list) and returns an iterator that yields the results.

In this case, map(str, list1) is converting each element in list1 to a string using the str function. It's essentially equivalent to a list comprehension, but in this context, it returns an iterator instead of a list.

"""