from class_participant import Participant
from tkinter import *
from PIL import Image, ImageTk
from time import sleep


class Player(Participant):
    def __init__(self, deck, root):
        super().__init__(deck)
        # self.hand = ["aceclub", "4club"]  # тестирование на фиксированную руку
        # self.calc_score(self.hand)  # тестирование на фиксированную руку

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
        self.player_result.config(font=("Courier", 16))
        if self.score[1]:
            if max(self.score) == 21:
                self.player_result.config(text="21!!!!!! BLACKJACK!!!", bg="orange")
            else:
                self.player_result.config(text=f"Ваш результат: {self.score[0]}/{self.score[1]}", bg="green")
        else:
            if max(self.score) == 21:
                self.player_result.config(text="21!!!!!! BLACKJACK!!!", bg="orange")

            else:
                self.player_result.config(text=f"Ваш результат: {self.score[0]}", bg="green")

        self.player_result.place(x=50, y=270, width=380, height=50)

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
        # self.hand.append("6spade") # тестирование требуемой карты

        self.calc_score(self.hand)
        self.show_score()
        self.show_card_in_hand(self.x_coord, self.y_coord, self.number)
        # super().check_score()
