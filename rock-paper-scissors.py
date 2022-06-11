import random
### To introduce the game
print('This  is simple python version of the popular game \n"Rock Paper Scissors" \nTake Note that You are playing against the computer')
rock_paper_scissors = ["Rock" , "Scissors" ,"Paper"]
name = input('What is your name\n=>')

###### Function to take input from player , then convert the input to Rock , Paper or Scissors
def take_input():
    selection = input(f'Hello {name} \nEnter "R" for Rock , \n"P" for paper \n"S" for scissors\n')
    if (selection == 'R' or selection == 'r'):
        selection = "Rock"
    elif (selection == 'P' or selection == 'p'):
        selection= "Paper"
    elif (selection == 'S' or selection == 's'):
        selection = "Scissors"    
    return selection

####### Function to determine who wins or loses
def win_or_lose():    
    if selection == "Rock":
        print(f'{name} wins Computer lose')    
    elif (selection == "Scissors" and computer_guess== "Paper"):
        print(f'{name} wins Computer lose')   
    elif (selection== "Paper"):
        print('Computer wins')
    else: 
        print('Computer wins')


selection = take_input()

### Check if selection is valid
while True:
    if(selection in rock_paper_scissors):
        break
    selection = take_input()

#### Print players selection and computer's random guess
computer_guess = random.choice(["Rock" , "Scissors" ,"Paper"])
print(f'{name} selected {selection} , while computer selected {computer_guess}')
    
        
###Check if there is a tie
while (selection == computer_guess):
    print('it is a tie')
    computer_guess = random.choice(["Rock" , "Scissors" ,"Paper"])
    selection = take_input()
    print(f'{name} selected {selection} , while computer selected {computer_guess}')

##### initialise the function win_or_lose()
win_or_lose()
      
    

        



input('Press enter to exit')


