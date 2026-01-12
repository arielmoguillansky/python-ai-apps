import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice != 1 and user_choice != 2 and user_choice != 0:
    print("Wrong value.")
    exit()

ai_choice = random.randint(0,2)
choices = [rock, paper, scissors]
print(f"You choose: {choices[user_choice]}")
print(f"AI choose: {choices[ai_choice]}")

if user_choice == 0:
    if ai_choice == 0:
        print("Its a draw!")
    elif ai_choice == 1:
        print("AI wins!")
    else:
        print("YOU win!")
elif user_choice == 1:
    if ai_choice == 0:
        print("YOU win!")
    elif ai_choice == 1:
        print("Its a draw!")
    else:
        print("AI wins!")
else:
    if ai_choice == 0:
        print("AI wins!")
    elif ai_choice == 1:
        print("YOU win!")
    else:
        print("Its a draw!")
