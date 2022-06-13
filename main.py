import random


def select(): 
        return input('please select R or P or S ')
options = ['R', 'P', 'S']

def player():

    def game():
      

      selection = select()
        
      if selection in options:
        return selection
      else:
        print('invalid option')
        game()
              
              

    return game()

def cpu():
    return random.choice(options)

def init():

    player1 = player()
    cpu0 = cpu()
     

    def move_format(option):
        if option == 'R':
            return 'rock)'
        elif option == 'P':
            return 'paper)'
        elif option == 'S':
            return 'scissors)'

    player_move = move_format(player1)
    cpu_move = move_format(cpu0) 

    print('Player (' + str(player_move) + ': CPU (' + str(cpu_move) )

    if player1 == 'S' and cpu0 == 'P':
      print('Player is the Winner!!!')
      init()
      
    elif cpu0 == 'S' and player1 == 'P':
      print('CPU is the Winner!!!')
      init()
    elif player1 == 'P' and cpu0 == 'R':
      print('Player is the Winner!!!')
      init()
    elif cpu0 == 'P' and player1 == 'R':
      print('CPU is the Winner!!!')
      init()
    elif player1 == 'R' and cpu0 == 'S':
      print('Player is the Winner!!!')
      init()
    elif cpu0 == 'R' and player1 == 'S':
      print('CPU is the Winner!!!')
      init()
    elif cpu0 == 'S' and player1 == 'S':
      print('it is a tie !!!')
      init()
    elif cpu0 == 'P' and player1 == 'P':
      print('it is a tie !!!')
      init()
    elif cpu0 == 'R' and player1 == 'R':
      print('it is a tie !!!')
      init()

init()