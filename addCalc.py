# A simple addition calculator

# This is used to input your numbers
number1 = input("Enter the first number ")
number2 = input("Enter the second number ")

# This converts the inputs to floats
numberf1 = float(number1)
numberf2 = float(number2)

# This performs the addition
result = numberf1 + numberf2

# This displays the result
print(f"The result of {numberf1} + {numberf2} is: {result}")
