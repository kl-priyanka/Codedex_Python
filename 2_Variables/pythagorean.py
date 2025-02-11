username = input('Enter your name: ')

print(username)

age = int(input('What is your age? '))

print(age)

#pythagorean equation
#c = sqrt(a^2 + b^2)
#where c is the hypotenuse
#a is the length of a short side
#b is the length of the other short side

a = int(input("Enter the length of the first short side:"))
b = int(input("Enter the length of the second short side:"))
c=(a**2 + b**2)**0.5
print(f"The length of the hypotenuse is {c}")
