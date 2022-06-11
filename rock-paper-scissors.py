import random
print('This  is simple python version of the popular game \n"Rock Paper Scissors" \nTake Note that You are playing against the computer')
rock_paper_scissors = ["Rock" , "Scissors" ,"Paper"]
name = input('What is your name\n')

while True:
    selection = int(input(f'Hello {name} , enter 1 for Rock , 2 for paper , 3 for scissors\n'))
    if (selection > 0 and selection <4):
        break
selection = rock_paper_scissors[selection -1]

computer_guess = random.randrange(0 ,3)
computer_guess = rock_paper_scissors[computer_guess]
print(f'{name} selected {selection} , while computer selected {computer_guess}')

if selection == computer_guess:
    print('it is a tie')
elif selection == "Rock":
    print(f'{name} wins Computer lose')
elif (selection == "Scissors" and computer_guess== "Paper"):
    print(f'{name} wins Computer lose')
elif (selection== "Paper"):
    print('Computer wins')
else: print('Computer wins')



input('Press enter to exit')


