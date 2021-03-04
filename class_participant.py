from calculate_hand import calc_cards
from random import choice


class Participant:
    def __init__(self, deck):
        self.hand = []
        for _ in range(2):
            draw = choice(deck)
            deck.remove(draw)
            self.hand.append(draw)
        self.score = ()
        self.calc_score(self.hand)
        self.winner = ""

    def calc_score(self, hand):
        self.score = calc_cards(hand)

    def hit(self, deck):
        """кто-то берет 1 карту"""
        draw = choice(deck)
        deck.remove(draw)
        self.hand.append(draw)

        # self.hand.append("aceclub")  # тест на нуж
