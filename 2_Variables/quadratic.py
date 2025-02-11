#Quadratic Formula
#Quadratic equation is of the form ax^2 + bx + c = 0
#x = (-b +- ((b**2)-4*a*c)**0.5)/2*a
#where a, b, and c are coefficients

a = int(input("Enter the coefficient of x^2:"))
b = int(input("Enter the coefficient of x:"))
c = int(input("Enter the constant:"))
x1 = (-b + ((b**2) - 4*a*c)**0.5)/(2*a)
x2 = (-b - ((b**2) - 4*a*c)**0.5)/(2*a)
print(f"The solutions are {x1} and {x2}")
