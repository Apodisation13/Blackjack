from calc_card import calc_cards
from random import choice
from try_3 import cards_default
from winner import check_winner, check_starting_bj


class Participant:
    def __init__(self, deck):
        self.hand = []
        for _ in range(2):
            draw = choice(deck)
            deck.remove(draw)
            self.hand.append(draw)
        self.winner = ''
        self.score = ()
        self.calc_score(self.hand)

    def calc_score(self, hand):
        self.score = calc_cards(hand)

    def hit(self, deck):
        """кто-то берет 1 карту"""
        draw = choice(deck)
        deck.remove(draw)
        self.hand.append(draw)
        print(f'hit {draw}')

    def stand(self):
        pass



class Player(Participant):
    def __init__(self):
        super().__init__(cards_default)
        # self.hand = [2, "A"] # тестирование на фиксированную руку
        # self.calc_score(self.hand) #
        self.show_cards(self.hand)
        self.show_score()

    def show_cards(self, hand):
        print(f'Карты в руке игрока: {hand}')

    def show_score(self):
        if self.score[1]:
            print(f'Результат игрока {self.score[0]}/{self.score[1]}')
        else:
            print(f'Результат игрока {self.score[0]}')

    def hit(self, deck):
        super().hit(deck)
        self.show_cards(self.hand)
        self.calc_score(self.hand)
        self.show_score()


class Dealer(Participant):
    def __init__(self):
        super().__init__(cards_default)
        # self.hand = [2, "A"] # тестирование на фиксированную руку
        # self.calc_score(self.hand) #
        print(f"Карты в руке дилера: ['{self.hand[0]}', ??]")
        # print(f"Карты в руке дилера: {self.hand}") # показать полную руку дилера


    def show_hand_and_score(self, hand):
        if self.score[1]:
            print(f'Карты дилера {hand}, результат {self.score[0]}/{self.score[1]}')
        else:
            print(f'Карты дилера {hand}, результат {self.score[0]}')

    def hit(self, deck):
        super().hit(deck)
        self.calc_score(self.hand)
        self.show_hand_and_score(self.hand)

    def dealer_AI(self, deck):
        pass


player = Player()
dealer = Dealer()

starting_bj = check_starting_bj(player.score, dealer.score, dealer.hand)
if starting_bj[1]:
    player.hit(cards_default)
    check_winner(player.score, dealer.score, player.hand, dealer.hand)