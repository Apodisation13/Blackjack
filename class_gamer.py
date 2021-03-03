from calculate_hand import calc_cards
from random import choice
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep


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


class Player(Participant):
    def __init__(self, deck, root):
        super().__init__(deck)
        # self.hand = ["aceclub", "10club"] # тестирование на фиксированную руку
        # self.calc_score(self.hand) # тестирование на фиксированную руку

        self.x_coord = 50  # начальная позиция карт игрока
        self.y_coord = 330
        self.number = 0  # номер карты в руке игрока

        self.show_card_in_hand(self.x_coord, self.y_coord, self.number)
        root.update()
        sleep(2)
        self.show_card_in_hand(self.x_coord, self.y_coord, self.number)

        self.player_result = Label()

        self.show_score()



    def show_score(self):
        if self.score[1]:
            if max(self.score) != 21:
                self.player_result = Label(text=f"Ваш результат: {self.score[0]}/{self.score[1]}", bg="green")
            else:
                self.player_result = Label(text= "21!!!!!! BLACKJACK!!!", bg="orange")
        else:
            if max(self.score) != 21:
                self.player_result = Label(text=f"Ваш результат: {self.score[0]}", bg="green")
            else:
                self.player_result = Label(text="21!!!!!! BLACKJACK!!!", bg="orange")

        self.player_result.place(x=50, y=270, width=300, height=50)
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

    # def check_score(self, dealer_result):
    #     if max(self.score) > 21:
    #         messagebox.showerror("ВЫ ПРОИГРАЛИ!", "Busted!")
    #     elif max(self.score) == 21:
    #         messagebox.showinfo("ВЫИГРЫШ!!!", "21!!!!!! BLACKJACK!!!")


class Dealer(Participant):
    def __init__(self, deck, root):
        super().__init__(deck)
        self.hand = ["2diamond", "2hearts"] # тестирование на фиксированную руку
        self.calc_score(self.hand) # тестирование на фиксированную руку

        self.x_coord = 50  # начальная позиция карт дилера
        self.y_coord = 10
        self.number = 0  # номер карты в руке дилера

        self.hidden = Label()

        self.open_card(self.number)
        self.hidden_card()

        self.dealer_result = Label()

    def start_bj(self, player, root):
        if max(player.score) != 21 and max(self.score) == 21:
            self.open_hidden(root)

    def s(self, card_image, x_coord, y_coord):
        card_image = card_image.resize((150, 170), Image.ANTIALIAS)
        card_image = ImageTk.PhotoImage(card_image)
        card = Label(image=card_image)
        card.image = card_image
        self.hidden = card
        card.place(x=x_coord, y=y_coord)
        self.x_coord += 170
        self.number += 1

    def open_card(self, number):
        card_image = Image.open(f'D:/Python Projects/blackjack/cardsimages/{self.hand[number]}.jpg')
        self.s(card_image, self.x_coord, self.y_coord)

    def hidden_card(self):
        card_image = Image.open(f'D:/Python Projects/blackjack/cardsimages/cardback.jpg')
        self.s(card_image, self.x_coord, self.y_coord)

    def open_hidden(self, root):
        root.update()
        sleep(2)
        self.hidden.destroy()
        self.number = 1
        self.x_coord = 50+170
        self.open_card(self.number)

    def show_dealer_result(self):
        if self.score[1]:
            if max(self.score) != 21:
                self.dealer_result = Label(text=f"Результат дилера: {self.score[0]}/{self.score[1]}", bg="grey")
            else:
                self.dealer_result = Label(text="21!!!!!! BLACKJACK!!!", bg="red")
        else:
            if max(self.score) != 21:
                self.dealer_result = Label(text=f"Результат дилера: {self.score[0]}", bg="grey")
            else:
                self.dealer_result = Label(text="21!!!!!! BLACKJACK!!!", bg="red")

        self.dealer_result.place(x=50, y=200, width=300, height=50)
        self.dealer_result.config(font=("Courier", 16))

    def dealer_AI(self, deck, player, root):
        self.open_hidden(root)
        self.show_dealer_result()
        if max(player.score) > 21:
            return
        while max(self.score) < max(player.score):
            self.hit(deck)
            root.update()
            sleep(2)

    def hit(self, deck):
        super().hit(deck)
        # self.hand.append(5) # для тестирования любой карты
        self.calc_score(self.hand)
        self.open_card(self.number)
        self.show_dealer_result()
