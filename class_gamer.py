from calculate_hand import calc_cards
from random import choice
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class Participant:
    def __init__(self, deck):
        self.hand = []
        for _ in range(2):
            draw = choice(deck)
            deck.remove(draw)
            self.hand.append(draw)
        self.score = ()
        self.calc_score(self.hand)

    def calc_score(self, hand):
        self.score = calc_cards(hand)

    def hit(self, deck):
        """кто-то берет 1 карту"""
        draw = choice(deck)
        deck.remove(draw)
        self.hand.append(draw)

        # self.hand.append("aceclub")  # тест на нуж

    def check_score(self):
        if max(self.score) > 21:
            messagebox.showerror("ВЫ ПРОИГРАЛИ!", "Busted!")


class Player(Participant):
    def __init__(self, deck):
        super().__init__(deck)
        # self.hand = ["aceclub", "6club"] # тестирование на фиксированную руку
        # self.calc_score(self.hand) # тестирование на фиксированную руку

        self.show_score()

        self.x_coord = 50  # начальная позиция карт игрока
        self.y_coord = 330
        self.number = 0  # номер карты в руке игрока

        self.show_card_in_hand(self.x_coord, self.y_coord, self.number)
        self.show_card_in_hand(self.x_coord, self.y_coord, self.number)

        self.player_result = Label()

    def show_score(self):
        if self.score[1]:
            self.player_result = Label(text=f"Ваш результат: {self.score[0]}/{self.score[1]}", bg="green")
            self.player_result.place(x=50, y=250, width=300, height=50)
            self.player_result.config(font=("Courier", 16))
        else:
            self.player_result = Label(text=f"Ваш результат: {self.score[0]}", bg="green")
            self.player_result.place(x=50, y=250, width=300, height=50)
            self.player_result.config(font=("Courier", 16))

    def show_card_in_hand(self, x_coord, y_coord, number):
        card_image = Image.open(f'D:/Python Projects/blackjack/cardsimages/{self.hand[number]}.jpg')
        card_image = card_image.resize((150, 170), Image.ANTIALIAS)
        card_image = ImageTk.PhotoImage(card_image)
        card = Label(image=card_image)
        card.image = card_image
        card.place(x=x_coord, y=y_coord)
        self.x_coord += 170
        self.number += 1

    def hit(self, deck):
        super().hit(deck)
        # self.hand.append("acespade") # тестирование требуемой карты

        self.calc_score(self.hand)
        self.show_score()
        self.show_card_in_hand(self.x_coord, self.y_coord, self.number)
        # super().check_score()


class Dealer(Participant):
    def __init__(self, deck):
        super().__init__(deck)
        # self.hand = ["5diamond", "acehearts"] # тестирование на фиксированную руку
        # self.calc_score(self.hand) # тестирование на фиксированную руку

        self.x_coord = 50  # начальная позиция карт дилера
        self.y_coord = 10
        self.number = 0  # номер карты в руке дилера
        self.open_card(self.number)
        self.hidden_card()

    def s(self, card_image, x_coord, y_coord):
        card_image = card_image.resize((150, 170), Image.ANTIALIAS)
        card_image = ImageTk.PhotoImage(card_image)
        card = Label(image=card_image)
        card.image = card_image
        card.place(x=x_coord, y=y_coord)
        self.x_coord += 170
        self.number += 1

    def open_card(self, number):
        card_image = Image.open(f'D:/Python Projects/blackjack/cardsimages/{self.hand[number]}.jpg')
        self.s(card_image, self.x_coord, self.y_coord)

    def hidden_card(self):
        card_image = Image.open(f'D:/Python Projects/blackjack/cardsimages/cardback.jpg')
        self.s(card_image, self.x_coord, self.y_coord)



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
        if max(player.score) > 21:
            return
        while max(self.score) < max(player.score):
            self.hit(deck)
