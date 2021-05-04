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
user_choice=int(input("Lets Play, Choose between the three, 0 For rock, 1 for paper, 2 for scissors \n"))
if user_choice > 2 or user_choice < 0 :
  print("Type a valid number to play")
else :
  game_list=[rock,paper,scissors]
  user_choice_choosen= game_list[user_choice]
  print(user_choice_choosen)
  computer_random=random.randint(0,2)
  computer_choice=game_list[computer_random]
  print("Computer Choose:")
  print(computer_choice)
  if user_choice_choosen == rock and computer_choice == paper :
    print("You lost")
  elif user_choice_choosen == paper and computer_choice == scissors :
    print("You lost")
  elif user_choice_choosen == scissors and computer_choice == rock :
    print("You lost")
  elif user_choice_choosen == computer_choice :
    print("Its draw")

  else :
    print("You won")
