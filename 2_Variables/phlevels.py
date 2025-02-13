import random
ph = random.randint(0,14)

print(ph)

if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")