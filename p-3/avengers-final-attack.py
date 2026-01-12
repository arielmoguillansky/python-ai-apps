print(r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⠿⠿⠛⣻⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⠀⠀⠀⣰⣿⣿⣿⠟⣿⣿⣿⣿⢿⣿⣷⣦⠀⠀⠀⠀
⠀⠀⢠⣾⣿⡟⠁⠀⠀⠀⠀⠀⣰⣿⣿⣿⡟⠀⣿⣿⣿⣿⠀⠈⢻⣿⣷⡄⠀⠀
⠀⢠⣿⣿⠏⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡟⠀⠀⣿⣿⣿⣿⠀⠀⠀⠹⣿⣿⡄⠀
⢀⣿⣿⠏⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⠁⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠸⣿⣿⡄
⣸⣿⡟⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠃⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⢻⣿⣇
⣿⣿⡇⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠇⠀⠀⠀⠀⣈⠻⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿
⣿⣿⡇⠀⠀⠀⠀⢠⣿⣿⣿⣿⣯⣤⣤⣤⣤⣤⣿⣶⣌⠻⠀⠀⠀⠀⠀⢸⣿⣿
⢻⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⣸⣿⡟
⠘⣿⣿⡄⠀⢠⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⢿⣿⣿⠟⢋⠀⠀⠀⠀⢠⣿⣿⠃
⠀⠹⣿⡿⢀⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠸⠋⣡⣴⣿⠀⠀⠀⣠⣿⣿⠏⠀
⠀⠀⠙⢁⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠀⢀⣴⣿⣿⠋⠀⠀
⠀⠀⢀⣾⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⠟⠁⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⠏⣰⣿⣶⣦⣤⣤⣤⣤⣤⣤⣴⣶⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀
⢀⣾⣿⣿⣿⣿⡟⠀⠈⠙⠛⠻⠿⠿⠿⠿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
''')
print("--- AVENGERS: THE FINAL STAND ---")
print("You are Tony Stark (Iron Man). Thanos is approaching the Gauntlet!")

choice1 = input("Thanos throws a moon at you! Do you use 'Thrusters' to dodge or 'Shield' to block? ").lower()
if choice1 == "thrusters":
    # Step 2: The Attack
    choice2 = input("You're in range. Do you fire the 'Unibeam' or deploy 'Drones'? ").lower()
    if choice2 == "unibeam":
        # Step 3: The Strategy
        print("Thanos is dazed, but you're low on power.")
        choice3 = input("Do you 'Wait' for backup from Captain Marvel or 'Attack' him alone? ").lower()
        if choice3 == "wait":
            # Step 4: The Heist
            print("Captain Marvel distracts him!")
            choice4 = input("Do you try to 'Punch' the Gauntlet or use 'Nanotech' to slide the stones off? ").lower()
            if choice4 == "nanotech":
                # Step 5: The Ending
                print("You have the stones in your suit. Thanos looks at you.")
                choice5 = input("What is your final line? 'I am Inevitable' or 'I am Iron Man'? ").lower()
                if choice5 == "i am iron man":
                    print("SNAP! You defeated Thanos and saved the universe. You are a legend.")
                else:
                    print("Thanos takes the stones back. 'I am... Inevitable.' *Snap*")
            else:
                print("Thanos is too strong! He headbutts you into a mountain. Game Over.")
        else:
            print("Thanos grabs you by the throat. 'All that for a drop of blood.' Game Over.")
    else:
        print("Thanos uses the Space Stone to crush your drones and then you. Game Over.")
else:
    print("The Shield shattered under the weight. You've been crushed. Game Over.")