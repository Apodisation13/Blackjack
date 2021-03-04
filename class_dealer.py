from class_participant import Participant
from tkinter import *
from PIL import Image, ImageTk
from time import sleep


class Dealer(Participant):
    def __init__(self, deck, root):
        super().__init__(deck)
        # self.hand = ["4diamond", "7hearts"] # тестирование на фиксированную руку
        # self.calc_score(self.hand) # тестирование на фиксированную руку

        self.x_coord = 50  # начальная позиция карт дилера
        self.y_coord = 10
        self.number = 0  # номер карты в руке дилера

        self.hidden = Label()  # скрытую карту нужно сохранить отдельно, чтобы потом открывать её

        self.open_card(self.number)  # выполняем метод открыть карту
        root.update()  # вот именно в такой последовательности, как ни странно...
        sleep(2)
        self.hidden_card()  # выполняем метод скрытой карты

        self.dealer_result = Label()  # Поле с результатом дилера

    def start_bj(self, player, money, root):
        if max(self.score) == 21 and max(player.score) != 21:
            self.open_hidden(root)
            player.player_result.config(bg="grey")
            money.wallet.config(bg="red")
            money.bet.config(bg="red")

    def s(self, card_image, x_coord, y_coord):
        card_image = card_image.resize((150, 170), Image.ANTIALIAS)
        card_image = ImageTk.PhotoImage(card_image)
        card = Label(image=card_image)
        card.image = card_image  # ВОТ ЭТО САМАЯ ВАЖНАЯ СТРОЧКА, чтобы изображения не тёрлись
        self.hidden = card  # вторая карта (скрытая) сохранилась в отдельный атрибут
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
        self.show_dealer_result()
        self.hidden.destroy()
        self.number = 1
        self.x_coord = 50+170
        self.open_card(self.number)
        self.show_dealer_result()

    def show_dealer_result(self):
        if self.score[1]:  # если в руке дилера есть хоть один туз
            if max(self.score) != 21:
                self.dealer_result = Label(text=f"Результат дилера: {self.score[0]}/{self.score[1]}", bg="grey")
            else:
                self.dealer_result = Label(text="21!!! BLACKJACK у дилера!!!", bg="red")
        else:
            if max(self.score) != 21:
                self.dealer_result = Label(text=f"Результат дилера: {self.score[0]}", bg="grey")
            else:
                self.dealer_result = Label(text="21!!! BLACKJACK у дилера!!!", bg="red")

        self.dealer_result.place(x=50, y=200, width=380, height=50)
        self.dealer_result.config(font=("Courier", 16))

    def dealer_AI(self, deck, player, root):
        self.open_hidden(root)
        # if max(player.score) > 21:  # если игрок перебрал 21 хитами, чтоб не играл тут
        #     return
        if max(player.score) <= 11 and max(player.score) == max(self.score):
            self.hit(deck, root)
        # костыль - если у игрока 11 или меньше, то при равенстве очков дилеру не страшно рискнуть и взять карту
        # потому что при любой карте 21 он не переберёт
        while max(self.score) < max(player.score):
            self.hit(deck, root)
        self.dealer_result.config(text=f"Результат дилера: {max(self.score)}", bg="grey")

    def hit(self, deck, root):
        super().hit(deck)  # для тестирования фиксированного хита эту строку закомментить
        # self.hand.append("10club") # для тестирования любой карты
        if max(self.score) < 21:
            root.update()  # вот именно в такой последовательности, как ни странно...
            sleep(2)
        self.calc_score(self.hand)
        self.open_card(self.number)
        self.show_dealer_result()
