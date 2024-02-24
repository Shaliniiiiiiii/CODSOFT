



####ROCK PAPER SCISSORS GAME #####

###   TASK 4  #####


import random


print("ROCK PAPER SCISSORS GAME")


def play():

    player=str(input("r for Rock, p for paper , s for scissors : ")).lower()
    
    choose=[ "r" ,  "p",  "s" ]
    
    computer = random.choice(choose)
    
    print(f' your choice { player }   <=>  oppenet {computer }')
    
    if (player == computer):
        print ("game is in tie")
        
    elif ((player == 'r' and computer == ' s  ' ) or (player =='p' and computer =='r') or (player == 's' and computer == 'p')):
        print("you won the game")
        
    else:
        print("good try better luxt next time")
        
        
play()
    
