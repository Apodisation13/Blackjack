from tkinter import *
from tkinter import messagebox


class Money:
    def __init__(self, money):
        self.money = money

        self.wallet = Label()
        self.bet = Label()

    def check_correct_value(self, entry):
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

    def show_wallet(self):
        self.wallet = Label(text=f'Ваш кошелёк: {self.money}', font=("Courier", 12), bg='green')
        self.wallet.place(x=750, y=40)

    def can_bet(self, bet):
        if bet > self.money:
            messagebox.showwarning("Ошибка ставки",
                                   f'Вы не можете поставить {bet}, у вас есть только {self.money}')
            return False
        return True

    def place_bet(self, bet):
        self.wallet.config(text=f'Ваш кошелёк: {self.money}-{bet}', bg='grey')
        self.money -= bet
        self.bet = Label(text=f'Ваша ставка: {bet}', font=("Courier", 12), bg='grey')
        self.bet.place(x=750, y=70)

    def win(self, bet):
        self.money += bet

    def lose(self, bet):
        self.money -= bet
        if self.money < 0:
            self.money = 0

    def end_game(self, root, wallet_label):
        if self.money == 0:
            wallet_label.config(bg="red")
            messagebox.showerror("БАНКРОТ!", "Вы проиграли все деньги...")
            root.destroy()
            return True
        return False

    def payment(self, bet, winner: str, double_status: bool, starting_blackjack_status: bool):
        if winner == "player":
            if starting_blackjack_status or double_status:
                self.win(bet * 2)
            else:
                self.win(bet)
        elif winner == "dealer":
            if double_status:
                self.lose(bet * 2)
            else:
                self.lose(bet)
        else:
            self.show_wallet()

    def starting_winner(self, p_score: tuple, d_score: tuple):
        winner = ''
        if max(p_score) == 21:
            messagebox.showinfo("ВЫИГРЫШ!!!", "21!!!!!! BLACKJACK!!!")
            winner = "player"
            return True, winner
        elif max(d_score) == 21:
            messagebox.showerror("ВЫ ПРОИГРАЛИ!!!", "21!!! BLACKJACK!!!")
            winner = "dealer"
            return True, winner
        return False, winner