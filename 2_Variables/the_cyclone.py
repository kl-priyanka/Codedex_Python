height = int(input("Enter your height in cms: "))
credits = int(input("Enter the number of credits you have: "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif credits >= 10:
    print("You are not tall enough to ride.")
elif height >= 137:
    print("You don't have enough credits")