# Welcome Message 
print("Welcome to F.E.A.R. here you will begin your mandatory training.\n\nLet's get started...\n\n")

# Decision Trees 

userTrainingInputAccepted = 0
userWeaponsInputAccepted = 0 
userPhysicalInputAccepted = 0 
userMentalInputAccepted = 0

while userTrainingInputAccepted == 0: 

    print(f"Which of the following options would you like to begin with.\n1. Weapons Training\n2. Physical Training\n3. Mental Training\n\nEnter numbers 1 - 3 to make your selection.")

    userTrainingChoice = input("Selection: ").lower()
        
    if userTrainingChoice == "weapons training":
        while userWeaponsInputAccepted == 0: 
            userTrainingInputAccepted += 1
            print("\nWelcome to Weapons Training.\n\nSelect your weapon of choice.\n\n1. Explosives\n2. Handguns\n3. Long Range Rifles")

        
            userWeaponChoice = input("Select your weapon of choice").lower()

            if userWeaponChoice == "explosives":
                userWeaponsInputAccepted += 1
                explosivesChoice = input("CHOOSE QUICKLY: HOLD THE GRENADE OR THROW THE GRENADE").lower()

                if explosivesChoice == "hold the grenade":
                    print("Your commanding officer took the grenade away from you and threw it in the bush... moments later it explodes.\n\nYou almost killed your group.")
                elif explosivesChoice == "throw the grenade":
                    print("\nYou threw the grenade and blew up a Tesla. Nice Work!")
                else:
                    print("GAME OVER: You failed to make a proper choice and exploded.")


            elif userWeaponChoice == "handguns":
                userWeaponsInputAccepted += 1
                handgunsChoice = input("Choose your weapon:\n\n1. GLOCK\n2. 9mm").lower()

                if handgunsChoice == "glock":
                    userWeaponsInputAccepted += 1
                    print("GAME OVER: Your gun jammed in combat training and your were shot and killed.")
                elif handgunsChoice == "9mm":
                    print("You WIN:\nYou performed like Rambo and received a promotion to squad leader from your performance.")
                else: 
                    print("GAME OVER: You failed to select a proper weapon and took a knife to a gun fight. You were KIA")     


            elif userWeaponChoice == "long range rifles":
                userWeaponsInputAccepted += 1 
                longRifleChoice = input("Choose your weapon...\n\n1. AK-47\n2. Sniper Rifle\n")

                if longRifleChoice == "ak-47":
                    print("GAME OVER: \n\nYou could not control the recoil of the weapon and failed miserably.")
                elif longRifleChoice == "sniper rifle":
                    print("YOU WIN:\n\n You're a true marksman and will make our troop proud.")    
                else:
                    print("GAME OVER:\n\nYou failed to give a proper choice and were KIA.")


    elif userTrainingChoice == "physical training":

        userTrainingInputAccepted += 1
        print("\nWelcome to Physical Training.\n\nSelect your training from the options below.\n\n1. Jogging\n2. Weight Training\n3. Swimming")

        userPhysicalTrainingChoice = input("Select your Physical Training: ").lower()  



    elif userTrainingChoice == "mental training":

        userTrainingInputAccepted += 1
        print("Welcome to Mental Training.\n\nSelect your training from the list below.\n\n1. Hostage Negotiations\n2. Meditation\n3. Wellness")

        userMentalTrainingChoice = input("Select your Menatal Training:").lower()     


    else:
        print("Unknown Input: Please type in your selection again.\n\n")