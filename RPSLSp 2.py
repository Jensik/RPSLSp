import random

ROCK = 1
PAPER = 2
SCISSORS = 3
LIZARD = 4
SPOCK = 5

def get_player_input():
    player = raw_input('-> ROCK, PAPER, SCISSORS, LIZARD, SPOCK!\n')
    if str(player).upper() == 'ROCK':
        return 1
    elif str(player).upper() == 'PAPER':
        return 2
    elif str(player).upper() == 'SCISSORS':
        return 3
    elif str(player).upper() == 'LIZARD':
        return 4
    elif str(player).upper() == 'SPOCK':
        return 5

def get_cpu_input():
    return random.choice((ROCK,PAPER,SCISSORS,LIZARD,SPOCK))
    
def play_round():
    cpu = get_cpu_input()
    player = get_player_input()

    if (cpu == player):
        print 'CPU chose the same. You Tied'
        play_round()
    elif(cpu == 1)and(player in [2,5]):
        print'CPU chose ROCK. You Win'
        result = 'win'
    elif(cpu == 1)and(player in [3,4]):
        print'CPU chose ROCK. You Lose'
        result = 'lose'
    elif(cpu == 2)and(player in [3,4]):
        print'CPU chose PAPER. You Win'
        result = 'win'
    elif(cpu == 2)and(player in [1,5]):
        print'CPU chose PAPER. You Lose'
        result = 'lose'
    elif(cpu == 3)and(player in [1,5]):
        print'CPU chose SCISSORS. You Win'
        result = 'win'
    elif(cpu == 3)and(player in [2,4]):
        print'CPU chose SCISSORS. You Lose'
        result = 'lose'
    elif(cpu == 4)and(player in [3,1]):
        print'CPU chose LIZARD. You Win'
        result = 'win'
    elif(cpu == 4)and(player in [2,5]):
        print'CPU chose LIZARD. You Lose'
        result = 'lose'
    elif(cpu == 5)and(player in [2,4]):
        print'CPU chose SPOCK. You Win'
        result = 'win'
    elif(cpu == 5)and(player in [1,3]):
        print'CPU chose SPOCK. You Lose'
        result = 'lose'
    return result
    
def play_game():
    player_score = 0
    cpu_score = 0
    while player_score < 2 and cpu_score < 2:
        if 'win' == play_round():
            player_score += 1
        else:
            cpu_score += 1
    if player_score == 2:
        print'Player wins best of three! I totally let you win.'
    if cpu_score == 2:
        print'CPU wins best of three. Better luck next time.'

play_game()
