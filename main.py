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
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissor "))
if(choice==0):
  print(f"you chose {rock}")
elif(choice==1):
  print(f"you chose {paper}")
elif(choice==2):
  print(f"you chose {scissors}")

n= random.randint(0,2)
if(n==0):
  print(f"computer choose\n {rock}")
elif(n==1):
  print(f"computer choose\n {paper}")
elif(n==2):
  print(f"computer choose\n {scissors}")

if(choice==0 and n==0):
  print("Tie")
elif(choice==0 and n==1):
  print("Computer wins")
elif(choice==0 and n==2):
  print("You win")
elif(choice==1 and n==0):
  print("You win")
elif(choice==1 and n==1):
  print("Tie")
elif(choice==1 and n==2):
  print("Computer wins")
elif(choice==2 and n==0):
  print("Computer wins")
elif(choice==2 and n==1):
  print("You win")
elif(choice==2 and n==2):
  print("Tie")