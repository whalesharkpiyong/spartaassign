import random

list = ['rock','scissor', 'paper']
com = random.choice(list)
print(com)

count_win = 0
count_lose = 0
count_tie = 0
number_of_games = 0

while number_of_games == 0:
    print("Let's start rock scissor paper game.")
    user= str(input("Rock, scissor, paper!:  ").lower())

    if user not in list:
        print("Enter among rock, scissor and paper.")
    else:
        if com == user: 
            print('비겼습니다.')
            count_tie += 1
        elif (com == 'rock' and user == 'scissor') or (com =='scissor' and  user == 'paper') or (com =='paper' and user=='rock'):
            print('졌습니다.')
            count_lose += 1
        else:
            print('이겼습니다.')
            count_win += 1
    number_of_games += int(input("Enter 0 for more games, 1 to end the game: "))
else: 
    print("The game is ended.")
    print('You won ', count_win , 'times')
    print('You lost ', count_lose , 'times')
    print('You tied ', count_tie , 'times')


    
