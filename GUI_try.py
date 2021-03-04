from tkinter import *
from tkinter import messagebox
from class_dealer import Dealer
from class_player import Player
from class_money import Money
from deck import deck
from time import sleep
# from PIL import Image, ImageTk


def process_money():

    global money
    money = Money(data1.get())

    if money.check_correct_value(data1):
        money.money = int(money.money)
        money.show_wallet()

        data1.destroy()
        label1.destroy()
        button1.destroy()

        input_bet()


def input_bet():

    def process_bet():

        global money, bet
        if money.check_correct_value(data_bet):
            bet = data_bet.get()
            bet = int(bet)
            if money.can_bet(bet):

                label_bet.destroy()
                data_bet.destroy()
                button_bet.destroy()

                money.place_bet(bet)
                game()

    label_bet = Label(text="Введите ставку: ", font='30')
    label_bet.place(x=470, y=240)
    data_bet = Entry(font="70", justify="center")  # justify - текст по центру
    data_bet.place(x=463, y=270, width=135, height=50)  # ВВОД СТАВКИ

    button_bet = Button(text="Начать раунд", bg="green",
                        padx="30", pady='20', font="16", command=process_bet)
    button_bet.place(x=450, y=330)


def game():

    def new_round():
        for each in root.place_slaves():
            each.destroy()
        money.show_wallet()
        if money.end_game(root, money.wallet):
            return
        input_bet()

    def hit():
        double_down_button.destroy()
        root.update()
        sleep(1)
        player.hit(deck_in_round)

        status = money.hit_value(player)
        if status:
            new_round()
        if max(player.score) == 21:
            stand()

    def stand():
        hit_button.destroy()
        double_down_button.destroy()
        stand_button.destroy()

        player.player_result.config(text=f"Ваш результат: {max(player.score)}", bg="grey")

        dealer.dealer_AI(deck_in_round, player, root)

        money.check_winner(bet, player, dealer)
        new_round()

    deck_in_round = deck.copy()
    player = Player(deck_in_round, root)
    dealer = Dealer(deck_in_round, root)

    dealer.start_bj(player, root)
    starting_bj = money.starting_winner(player.score, dealer.score)[0]

    if not starting_bj:

        hit_button = Button(text="HIT", bg="cyan", font=20, command=hit)
        hit_button.place(x=50, y=530, width=150, height=50)
        stand_button = Button(text="STAND", bg="cyan", font="16", command=stand)
        stand_button.place(x=250, y=530, width=150, height=50)
        double_down_button = Button(text="Double-Down", bg="cyan", font="16", command=process_money)
        double_down_button.place(x=450, y=530, width=150, height=50)
    else:
        new_round()
    # r = Button(text="new round", bg="yellow", font=20, command=new_round)
    # r.place(x=900, y=500, width=100, height=50)


root = Tk()
root.geometry('1000x600+400+100')  # обязательно так, через пробел нельзя
root.resizable(False, False)  # заблокировать фуллскрин

# root_im = ImageTk.PhotoImage(Image.open("D:/Python Projects/blackjack/cardsimages/bj.png"))
# label = Label(image=root_im)
# label.place(x=0, y=0, height=600, width=1000)

label1 = Label(text="Введите сумму: ", font='70')
label1.place(x=470, y=240)

data1 = Entry(font="70", justify="center")  # justify - текст по центру
data1.place(x=463, y=270, width=135, height=50)
# money = data1.get()

button_image = PhotoImage(file='D:/Python Projects/blackjack/cardsimages/play_button.png')
button1 = Button(text="Играть", bg="green", font="16", command=process_money, image=button_image)
# 1: вводим деньги и идём на кнопку играть
button1.place(x=430, y=330, width=200, height=70)

root.mainloop()
