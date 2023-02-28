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

#Write your code below this line 👇
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
options = [rock, paper, scissors]
if choice<=2 and choice>=0:
    print(options[choice])
    computer_choice = random.randint(0,2)
    print("Computer choose:\n")
    print(options[computer_choice])
    if choice==0 and computer_choice == 0:
        print("It's a draw")
    elif choice==0 and computer_choice == 1:
        print("Computer wins!")
    elif choice==0 and computer_choice == 2:
        print("You win!")
    elif choice==1 and computer_choice==0:
        print("You win!")
    elif choice==1 and computer_choice == 1:
        print("It's a draw")
    elif choice==1 and computer_choice == 2:
        print("Computer wins!")
    elif choice==2 and computer_choice == 0:
        print("Computer wins!")
    elif choice==2 and computer_choice==1:
        print("You win!")
    elif choice==2 and computer_choice == 2:
        print("It's a draw")
else:
    print("You choose a wrong number! You loose!")