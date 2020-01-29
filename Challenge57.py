import random

__Card_Numbers__ = ['Ace', 'King', 'Queen', 'Jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']
__Card_House__ = ['Hearts', 'Clubs', 'Diamonds', 'Spades']


def generate_cards():
    __Cards__ = []
    for points in range(len(__Card_Numbers__)):
        for signs in range(len(__Card_House__)):
            __Cards__.append(f"{__Card_Numbers__[points]} Of { __Card_House__[signs]}")
    return __Cards__


def get_base_cards():
    __Cards__ = generate_cards()
    random.shuffle(__Cards__)
    random.shuffle(__Cards__)
    _temp_cards_player = []
    for i in range(2):
        _temp_cards_player.append(__Cards__[i])
        __Cards__.pop(i)
    _temp_cards_computer = []
    for i in range(2):
        _temp_cards_computer.append(__Cards__[i])
        __Cards__.pop(i)
    return _temp_cards_player, _temp_cards_computer, __Cards__


def get_score(cards_, compare_):
    Score = 0
    for i in range(len(cards_)):
        temp__ = cards_[i].split(" ")
        _number, _null, _house = temp__
        if _number in ['Ace', 'King', 'Queen', 'Jack']:
            if _number == 'Ace':
                if (compare_ + 11) > 21:
                    _number = 1
                else:
                    _number = 11
            else:
                _number = 10

        else:
            _number = int(_number)
        Score += _number
    return Score


class Hand:
    def __init__(self, cards_):
        self.cards = cards_
        self.score = get_score(cards_, 0)

    def show_hand(self, **kwargs):
        dealer = kwargs.get('dealer', False)
        if dealer:
            print('Dealers Hand:\n')
            for card in self.cards:
                print(card)
            print(f'Total Score: {self.score}')
        else:
            print('Your Hand:\n')
            for card in self.cards:
                print(card)
            print(f'Total Score: {self.score}')

    def add_card(self, deck_):
        self.cards.append(deck_[0])
        temp_ = deck_[0]
        deck_.pop(0)
        return deck_, temp_


def get_choice(player, deck_):
    player.show_hand()
    score = player.score
    Break = False
    while not Break:
        Choice = input("Hit? y/n ")
        if Choice.lower() == "y":
            deck_, drawn_card_ = player.add_card(deck_)
            print(f"You drew {drawn_card_}.\n\n")
            score = get_score(player.cards, player.score)
            player.score = score
            if score > 21:
                return True, deck_, score
            else:
                player.show_hand()
        elif Choice.lower() == "n":
            return False, deck_, score


def run_dealer(computer, deck_, player):
    computer.show_hand(dealer=True)
    Above = False
    while not Above:
        if computer.score > player.score:
            return False, deck_, computer.score
        elif (computer.score == player.score) and (computer.score == 21):
            return False, deck_, computer.score
        elif computer.score == 21:
            return False, deck_, computer.score
        elif (computer.score <= player.score) or (computer.score < 16):
            deck_, drawn_card_ = computer.add_card(deck_)
            print(f"Computer drew: {drawn_card_}")
            score = get_score(computer.cards, computer.score)
            computer.score = score

        if computer.score > 21:
            return True, deck_, computer.score


def play():
    _player_cards, _computer_cards, _deck = get_base_cards()
    Player = Hand(_player_cards)
    Computer = Hand(_computer_cards)
    _bust, _deck, _score = get_choice(Player, _deck)
    if _bust:
        print(f"You went bust!, with a score of {_score}. Better luck next time! ")
    else:
        print(f"Your final score: {_score}, dealer's turn...")
        _bust_comp, _deck, _score_comp = run_dealer(Computer, _deck, Player)
        if _bust_comp:
            print(f"The dealer has gone bust, with a score of: {_score_comp}.")
            print(f"You win!")
        else:
            if _score_comp == _score:
                print("Its a draw")
            else:
                print(f"The dealer has got a score of: {_score_comp}, you loose.")

play()
