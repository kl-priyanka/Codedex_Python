Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

dawn_dusk = int(input("Q1) Do you like dawn or Dusk? (1 for Dawn, 2 for Dusk): "))
if dawn_dusk == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif dawn_dusk == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print("Wrong input")
    
remember = int(input("Q2) When I'm dead, I want people to remember me as: (1) The Good (2) The Great (3) The Wise (4) The Bold): "))
if remember == 1:
    Hufflepuff = Hufflepuff + 2
elif remember == 2:
    Slytherin = Slytherin + 2
elif remember == 3:
    Ravenclaw = Ravenclaw + 2
elif remember == 4:
    Gryffindor = Gryffindor + 2
else:
    print("Wrong input")

instrument = int(input("Q3) Which kind of instrument most pleases your ear? (1) The Violin (2) The Trumpet (3) The Piano (4) The Drum): "))
if instrument == 1:
    Slytherin = Slytherin + 4
elif instrument == 2:
    Hufflepuff = Hufflepuff + 4
elif instrument == 3:
    Ravenclaw = Ravenclaw + 4
elif instrument == 4:
    Gryffindor = Gryffindor + 4
else:
    print("Wrong input")
    
print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

#print("Sorting Hat has chosen: ", max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin))