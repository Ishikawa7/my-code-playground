'''
Here are the requirements:
    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...
'''
import random
import math
from os import system
import time

colors = ('heart', 'diamonds', 'spades', 'clubs')
names = (
    'ACE',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'JACK',
    'QUEEN',
    'KING')


class Card:

    def __init__(self, name, color, value1, value2=0):
        self.name = name
        self.color = color
        self.value1 = value1
        if self.value1 == 1:
            self.value2 = 11

    def __str__(self):
        return self.name + ' of ' + self.color


class Deck:

    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.deck = [Card(names[value - 1], color, sorted((1, value, 10))[1])
                     for value in range(1, 14) for color in colors]

    def draw(self):
        return self.deck.pop(random.randrange(len(self.deck)))

    def __str__(self):
        string = ''
        for card in self.deck:
            string = string + '\n' + card.__str__()
        return string


class Hand:

    def __init__(self):
        self.hand = []
        self.sum = 0

    def add(self, card):
        self.hand.append(card)
        self.calculate_sum()

    def calculate_sum(self):
        sums = [0]
        for card in self.hand:
            next_sums = []
            if card.name == "ACE":
                for sum in sums:
                    next_sums.append(sum + card.value1)
                    next_sums.append(sum + card.value2)
            else:
                for sum in sums:
                    next_sums.append(sum + card.value1)
            sums = next_sums
        sums.append(21)
        sums.sort()
        index_of_21 = sums.index(21)
        if index_of_21 == 0:
            self.sum = sums[sums.index(21) + 1]
        else:
            self.sum = sums[sums.index(21) - 1]

    def reset(self):
        self.hand.clear()
        self.sum = 0

    def __str__(self):
        string = ''
        for card in self.hand:
            string = string + '--' + card.__str__()
        string = string + '|| ({})'.format(self.sum)
        if self.sum == 21:
            string = string + ' !!!BLACK JACK!!!'
        return string


class MoneyBalance:

    def __init__(self, initial_deposit):
        self.balance = initial_deposit

    def change_balance(self, ammount):
        self.balance += ammount

    def __str__(self):
        return self.balance


class Player:

    def __init__(self, initial_deposit=100):
        self.money = MoneyBalance(initial_deposit)
        self.my_hand = Hand()
        self.my_bet = 0

    def bet(self, desired_bet):
        if self.money.balance - desired_bet < 0 or desired_bet < 1:
            return False
        self.my_bet = desired_bet
        return True

    def clear_hand(self):
        self.my_bet = 0
        self.my_hand.reset()


class Dealer:

    def __init__(self):
        self.dealer_hand = Hand()
        self.dealer_deck = Deck()

    def display_initial_hand(self):
        return '?COVERERD CARD?' + '--' + self.dealer_hand.hand[1].__str__()

    def make_move(self, player_sum):
        '''
        @Simple one on one stategy
        '''
        if self.dealer_hand.sum >= player_sum:
            return 'stay'
        else:
            self.dealer_hand.add(dealer.dealer_deck.draw())
            return 'hit'

    def shuffle_if_necessary(self):
        if len(self.dealer_deck.deck) < 26:
            self.dealer_deck.shuffle()

    def clear_hand(self):
        self.dealer_hand.reset()


def play_hand(player, dealer):
    '''
    INPUT player and dealer (with their current status)
    OUTPUT True=player win || False=player lose || None=draw
    '''
    def display_cover():
        # display hands (cover card)
        system('clear')
        print('DEALER-->{}'.format(dealer.display_initial_hand()))
        print("PLAYER(deposit {})--> BET:{}||{}".format(player.money.balance,
                                                        player.my_bet, player.my_hand))

    def display_uncover():
        # display hands (all uncovered)
        system('clear')
        print('DEALER-->{}'.format(dealer.dealer_hand))
        print("PLAYER(deposit {})--> BET:{}||{}".format(player.money.balance,
                                                        player.my_bet, player.my_hand))

    # 0 player bet
    system('clear')
    print('Nice! Your deposit tot = {}'.format(player.money.balance))
    while not player.bet(int(input('Chose your bet: '))):
        print('Invalid bet')
    # 1 set up the hand (two card for dealer and player)
    player.my_hand.add(dealer.dealer_deck.draw())
    player.my_hand.add(dealer.dealer_deck.draw())
    dealer.dealer_hand.add(dealer.dealer_deck.draw())
    dealer.dealer_hand.add(dealer.dealer_deck.draw())
    # 2 player turn
    while player.my_hand.sum <= 21:
        display_cover()
        choiche = input('Your turn (hit or stay): ')
        if choiche == 'hit':
            time.sleep(1)
            player.my_hand.add(dealer.dealer_deck.draw())
            continue
        elif choiche == 'stay':
            break
        else:
            print('Invalid command, retry')
            continue
    else:
        display_cover()
        print('YOU BUST!')
        return False
    # 3 dealer turn
    while dealer.dealer_hand.sum <= 21:
        display_uncover()
        time.sleep(2)
        if dealer.make_move(player.my_hand.sum) == 'stay':
            print('Dealer stay')
            break
        print('Dealer hit')
        time.sleep(1)
    else:
        print('DEALER BUST!')
        display_uncover()
        return True
    # 4 decretate winner (false player lose, true player win, none draw)
    if dealer.dealer_hand.sum > player.my_hand.sum:
        return False
    elif dealer.dealer_hand.sum < player.my_hand.sum:
        return True
    else:
        return None


# GAME MENU
if __name__ == "__main__":
    choice = '-'
    while choice != 'end':
        print("\nCommands: 'start' to start a new game --- 'end' to end the game")
        choice = input('Input choice: ')
        if choice == 'end':
            break
        elif choice == 'start':
            # decide initial deposit
            initial_deposit = 0
            while initial_deposit < 1:
                try:
                    initial_deposit = int(input('Insert initial deposit: '))
                except BaseException:
                    print('Initial deposit not valid, insert again')
                    continue
            dealer = Dealer()
            player = Player(initial_deposit)
            while True:
                # launch the hand
                result_of_the_hand = play_hand(player, dealer)
                # decretate the winner / win-lose bet
                if result_of_the_hand is None:
                    print('DRAW!')
                else:
                    if result_of_the_hand:
                        print('YOU WIN!')
                        player.money.change_balance(player.my_bet)
                    else:
                        print('YOU LOSE!')
                        player.money.change_balance(-player.my_bet)
                # dealer shuffle if necessary and clear hands
                dealer.clear_hand()
                player.clear_hand()
                dealer.shuffle_if_necessary()
                player_balance = player.money.balance
                print('Your deposit {} '.format(player_balance))
                # continue to play?
                if player_balance < 1:
                    print('Insufficent money!! GET OUT OF HERE')
                    break
                elif input('Do you want to continue? Y/N ').lower() == 'y':
                    continue
                else:
                    break
        else:
            print('Invalid input, retry')
