import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

assets = [rock, paper, scissor]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))
computer_choice = random.randint(0, 2)

if user_choice > 2:
    print("Invalid Input!")
else:
    print(f"You choose: {assets[user_choice]}")
print(f"Computer chose: {assets[computer_choice]}")

if user_choice == 0:
    if computer_choice == 0:
        print("It's a draw.")
    elif computer_choice == 1:
        print("You loose!")
    else:
        print("You Win!")
elif user_choice == 1:
    if computer_choice == 1:
        print("It's a draw.")
    elif computer_choice == 2:
        print("You loose!")
    else:
        print("You Win!")
elif user_choice == 2:
    if computer_choice == 2:
        print("It's a draw.")
    elif computer_choice == 0:
        print("You loose!")
    else:
        print("You Win!")
