from calc_card import calc_cards, cards_default
from random import choice


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


class Player(Participant):
    def __init__(self):
        super().__init__(cards_default)
        # self.hand = ["A", 6] # тестирование на фиксированную руку
        # self.calc_score(self.hand) # тестирование на фиксированную руку
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
        # self.hand.append(4) # тестирование требуемой карты
        self.show_cards(self.hand)
        self.calc_score(self.hand)
        self.show_score()


class Dealer(Participant):
    def __init__(self):
        super().__init__(cards_default)
        # self.hand = [5, "A"] # тестирование на фиксированную руку
        # self.calc_score(self.hand) # тестирование на фиксированную руку
        print(f"Карты в руке дилера: ['{self.hand[0]}', ??]")
        # print(f"Карты в руке дилера: {self.hand}") # показать полную руку дилера

    def show_hand_and_score(self, hand):
        if self.score[1]:
            print(f'Карты дилера {hand}, результат {self.score[0]}/{self.score[1]}')
        else:
            print(f'Карты дилера {hand}, результат {self.score[0]}')

    def hit(self, deck):
        super().hit(deck)
        # self.hand.append(5) # для тестирования любой карты
        self.calc_score(self.hand)
        self.show_hand_and_score(self.hand)

    def dealer_AI(self, deck, player):
        self.show_hand_and_score(self.hand)
        while max(self.score) < max(player.score):
            self.hit(deck)
