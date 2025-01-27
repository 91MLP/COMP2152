import random




diceOptions = list(range(1, 7))


weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']




def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")




combatStrength = get_valid_input("Enter your combat strength (1-6): ")
mCombatStrength = get_valid_input("Enter monster combat strength (1-6): ")


# Battle simulation: 10 rounds
for j in range(1, 21, 2):      
        heroRoll = random.choice(diceOptions)
        monsterRoll = random.choice(diceOptions)
   


        combatStrength += heroRoll
        mCombatStrength += monsterRoll
   


        weapon = weapons[heroRoll - 1]     


        if combatStrength > mCombatStrength:
            winner = "Hero"
        elif combatStrength < mCombatStrength:
            winner = "Monster"
        else:
            winner = "Draw"
   
  
            print(f"Round {j}:")
        print(f"Weapon: {weapon}")
        print(f"Hero Strength: {combatStrength}, Monster Strength: {mCombatStrength}")
        print(f"Round Winner: {winner}")
   
  
        if j == 11:
            print("Battle Truce! The battle ends here.")
            break



