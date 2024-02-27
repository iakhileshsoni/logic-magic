# add a stream of numbers inputted by the user and stop adding as soon as user press q

sum = 0

while True:

    number = input("Enter a number or press q to exit : ")

    if number ==  'q':
        break
    try:
        number = int(number)
        sum += number
        print(f"Given number total is : {sum}")
    except ValueError:
        print("Invalid input. Please enter a valid number or q to exit.")

print(f"Sum of total provided numbers is : {sum}")

