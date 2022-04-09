import random
def play():
    user = input("Choose one 'r'for rock, 'p'for paper ,'s'for scissors\n" )
    computer = random.choice(['r','p','s']) #randomly chooses something from a list
    if user == computer:
        return "tie"
    if is_win(computer,user):
        return "You win"
    return "You lose"        
def is_win(opponent,player):
    if (player == 'r' and opponent =='s') or (player == 'p' and opponent == 'r') or (player == 's' and opponent=='p') :
        return True       
print(play())    
   