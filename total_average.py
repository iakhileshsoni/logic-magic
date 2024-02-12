# Accept marks of 3 Subjects then find total and average of that

phy     =   int(input("Enter marks of Physics : "))
che     =   int(input("Enter marks of Physics : "))
math    =   int(input("Enter marks of Physics : "))

total   =   phy + che + math
average =   total / 3

print("Total of the given Subject's mark is : {} and Average is : {}".format(total, average))
