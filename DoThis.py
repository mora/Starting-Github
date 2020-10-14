#hacktoberfest-accepted


# in this file, print your name and ask the user for two numbers,
# then print the larger between the two:  
# pi to the power of the first number 
# or the square root of the second number.
# then commit and push it back up to github.


import math
print("My name is Ujjwal.")

a, b = input("Enter two Number separated by space ").split()

print("The larger is ", end="")


pi = math.pi
power = pow(int(a), pi)
root = math.sqrt(int(b))

#print("The first number to the power pi = ", power)
#print("The square root of the second number = ", root)

if power>root:
    print(power)
else:
    print(root)
