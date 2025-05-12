#problem 14: card game
import random

def shuffle(d):
    '''
    the shuffle function
    d is a list of 52 empty values
    '''
    #reset the to empty the value of each card of the deck
    for c in range(52):
        d[c] = ''
    #randomly insert each card in the deck
    for c in ['2','3','4','5','6','7','8','9','10','j','q','k','a']:
        for seed in range(4): #considers the seeds of the cards
            position = random.randint(0,51)
#            collision = 0
            while d[position] != "":
                position = random.randint(0,51)
#                collision+=1
            d[position] = c
#    print(f"I got {collision} collisions ")
    return d

NUM_CARDS = 52


def no_high(lst):
    """
    lst is a list of strings representing cards.

    Return True if there are no high cards in list, False otherwise.
    """
    if 'j' in lst:
        return False
    if 'q' in lst:
        return False
    if 'k' in lst:
        return False
    if 'a' in lst:
        return False
    return True


deck = ['' for i in range(52)]
deck = shuffle(deck)

score_a = 0
score_b = 0
player = input("what player starts the game, A or B? ")

remaining = 52
for i in range(NUM_CARDS):
    card = deck[i]
#    print(f"{player} take {card} and next 4 are {deck[i+1:i+5]}")
    points = 0
    remaining -= 1
    if card == 'j' and remaining >= 1 and no_high(deck[i+1:i+2]):
        points = 1
    elif card == 'q' and remaining >= 2 and no_high(deck[i+1:i+3]):
        points = 2
    elif card == 'k' and remaining >= 3 and no_high(deck[i+1:i+4]):
        points = 3
    elif card == 'a' and remaining >= 4 and no_high(deck[i+1:i+5]):
        points = 4

    if points > 0:
        print(f'Player {player} scores {points} point(s).')

    if player == 'A':
        score_a = score_a + points
        player = 'B'
    else:
        score_b = score_b + points
        player = 'A'

print(f'Player A: {score_a} point(s).')
print(f'Player B: {score_b} point(s).')
