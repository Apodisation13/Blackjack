from tkinter import *
from tkinter import messagebox
from class_gamer import Player, Dealer
from deck import deck


def check_correct_value(entry):
    """проверка что начальные деньги или ставка это число больше 0"""
    try:
        int(entry.get())
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Вводить только целые положительные числа!")
        return False
    else:
        if int(entry.get()) > 0:
            return True
        messagebox.showwarning("Ошибка ввода", "Отрицательное или 0 ввести нельзя")
        return False


def show_wallet():
    global wallet
    wallet = Label(text=f'Ваш кошелёк: {money}', font=("Courier", 12), bg='green')
    wallet.place(x=750, y=40)


def process_money():
    if check_correct_value(data1):
        global money
        money = data1.get()
        show_wallet()
        data1.destroy()
        label1.destroy()
        button1.destroy()
        input_bet()


def input_bet():

    def process_bet():
        if check_correct_value(data_bet):
            global bet, money
            bet = data_bet.get()
            if int(bet) > int(money):
                messagebox.showwarning("Ошибка ставки", f'Вы не можете поставить {bet}, у вас есть только {money}')
            else:
                label_bet.destroy()
                data_bet.destroy()
                button_bet.destroy()
                wallet.config(text=f'Ваш кошелёк: {money}-{bet}', bg='grey')
                money = int(money) - int(bet)
                game()

    global money
    if int(money) > 0:
        label_bet = Label(text="Введите ставку: ", font='30')
        label_bet.place(x=470, y=240)
        data_bet = Entry(font="70", justify="center")  # justify - текст по центру
        data_bet.place(x=463, y=270, width=135, height=50)
        button_bet = Button(text="Начать раунд", bg="green",
                            padx="30", pady='20', font="16", command=process_bet)
        button_bet.place(x=450, y=330)
    else:
        root.destroy()


def game():

    def new_round():
        for each in root.place_slaves():
            each.destroy()
        show_wallet()
        if money > 0:
            input_bet()
        else:
            messagebox.showerror("БАНКРОТ!", "Вы проиграли все деньги...")
            root.destroy()

    def hit():
        player.hit(deck_in_round)
        if max(player.score) > 21:

            wallet.config(bg="red", text=f'Ваш кошелёк: {money}')
            player.player_result.config(bg="red")
            messagebox.showerror("ВЫ ПРОИГРАЛИ!", "Busted! Счёт больше 21         ")
            new_round()

    deck_in_round = deck.copy()
    player = Player(deck_in_round)
    dealer = Dealer(deck_in_round)

    hit = Button(text="HIT", bg="yellow", font=20, command=hit)
    hit.place(x=50, y=530, width=150, height=50)
    stand = Button(text="STAND", bg="green", font="16", command=process_money)
    stand.place(x=250, y=530, width=150, height=50)
    double_down = Button(text="Double-Down", bg="red", font="16", command=process_money)
    double_down.place(x=450, y=530, width=150, height=50)

    r = Button(text="new round", bg="yellow", font=20, command=new_round)
    r.place(x=900, y=500, width=100, height=50)

    root.mainloop()


root = Tk()
root.geometry('1000x600+50+100')  # обязательно так, через пробел нельзя
root.resizable(False, False)  # забл

# root_im = ImageTk.PhotoImage(Image.open("D:/Python Projects/blackjack/cardsimages/bj.png"))
# label = Label(image=root_im)
# label.place(x=0, y=0, height=600, width=1000)

label1 = Label(text="Введите сумму: ", font='70')
label1.place(x=470, y=240)

data1 = Entry(font="70", justify="center")  # justify - текст по центру
data1.place(x=463, y=270, width=135, height=50)
money = data1.get()

button_image = PhotoImage(file='D:/Python Projects/blackjack/cardsimages/play_button.png')
button1 = Button(text="Играть", bg="green", font="16", command=process_money, image=button_image)
# 1: вводим деньги и идём на кнопку играть
button1.place(x=430, y=330, width=200, height=70)

root.mainloop()
