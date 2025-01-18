#Define a new array called weapons and add 6 different weapon names in the array,
#with increasing levels of weapon strength. Use Fist, Knife, Club, Gun, Bomb, Nuclear bomb
#Roll the dice (1-6) to choose which weapon you must use.
#Save the roll in a variable called weaponRoll.
#Add your weaponRoll to the hero's combat strength
#Use this variable as an index into the weapons array and print out the name of the hero's weapon.
# Define the following condition:
#If weaponRoll is less than or equal to 2, print out "You rolled a weak weapon, friend".
#But if weaponRoll is less than or equal to 4, print out "Your weapon is meh"
#Else, print out "Nice weapon, friend! "
#If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
#Add error handling on all inputs eg. if input is not int, print an error message and halt
import random
weapon = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
WeaponRoll = random.randrange(1,6)

while True:
    try:
        WeaponNumber = int(input("Enter a number from 1 to 6"))
        if WeaponNumber <1 or WeaponNumber >6 :
            print("Error: Input must be between 1 and 6")
        else:
            value = weapon[WeaponNumber-1]
            print(value)
            if WeaponNumber <=2:
                print("You rolled a weak weapon, friend")
            elif WeaponNumber <=4:
                print("Your Weapon is meh")
            else:
                print("Nice Weapon, friend")
                if value != "fist":
                    print("Thank goodness you didn't roll the Fist...")
    except ValueError:
        print("Error: Input must be an integer")
        exit()








    