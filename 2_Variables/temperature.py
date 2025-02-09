#Operators
#+, -, *, /, %, **(exponentiation), //(floor division)
score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1
print(score)        # Output: 1

# Exponentiation
a = 2 ** 3  # a will be 8 (2*2*2)
b = 5 ** 2  # b will be 25 (5*5)
c = 9 ** 0.5 # c will be 3.0 (square root of 9)

# Floor division
x = 10 // 3  # x will be 3
y = 7 // 2   # y will be 3
z = -5 // 2  # z will be -3

# Order of operations
# 1. Parentheses
# 2. Exponentiation
# 3. Multiplication and Division
# 4. Addition and Subtraction
result = 4 * (5 + 3)  # result is 32

# look at the below code that calculates a 20% tip by calculating the total and then multiplying by a float
pizza = 2.99
coke = 0.99

total = pizza + coke

tip = total * 0.2

print(tip) # Output: 0.796

# Another easy way to write this using parantheses
tip = (pizza + coke) * 0.2

#calculate the temperature of Brooklyn given in Fahrenheit to Celsius
fahrenheit = 31
celsius = (fahrenheit -32)/1.8
print(celsius) # Output: -0.5555555555555556