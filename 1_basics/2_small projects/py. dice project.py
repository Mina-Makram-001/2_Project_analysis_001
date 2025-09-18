#py. dice project


import random

dice_faces = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

dice=[]
total=0

num_of_dice=int(input("how many dice ? : "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

#for die in range(num_of_dice):    
#    for line in dice_faces.get(dice[die]):
#        print(line)

for line in range(5):
    for die in dice:
        print(dice_faces.get(die)[line], end=" ")
    print()
    


for die in dice:
    total+=die
print(f"total : {total}")

