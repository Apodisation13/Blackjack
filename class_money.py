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
        self.money -= bet
        self.wallet.config(text=f'Ваш кошелёк: {self.money}', bg='grey')
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
                self.win(bet * 2)
        elif winner == "dealer":
            if double_status:
                self.lose(bet * 2)
        else:
            self.win(bet)
            self.show_wallet()

    def starting_bj_winner(self, player, dealer, bet, root):
        if max(player.score) == 21:
            self.bet.config(bg='green')
            self.wallet.config(bg="green", text=f'Ваш кошелёк: {self.money}+{bet}+{bet}+{bet}')
            messagebox.showwarning("ВЫИГРЫШ!!!", "21!!!!!! BLACKJACK!!!")
            self.win(bet * 3)  # удвоили выигрыш, ну вернее 3:1
            return True
        elif max(dealer.score) == 21:
            dealer.open_hidden(root)
            player.player_result.config(bg="grey")
            self.wallet.config(bg="red")
            self.bet.config(bg="red")
            messagebox.showerror("ВЫ ПРОИГРАЛИ!!!", "21!!! BLACKJACK!!!")
            return True
        return False

    def check_winner(self, bet, player, dealer):  # , player_hand, dealer_hand):
        winner = ''
        if max(dealer.score) > 21:
            self.bet.config(bg='green')
            self.wallet.config(bg="green", text=f'Ваш кошелёк: {self.money} + {bet} + {bet}')
            player.player_result.config(bg="green")
            dealer.dealer_result.config(bg="blue")
            if max(player.score) == 21:
                player.player_result.config(bg="yellow")
                messagebox.showwarning("ВЫИГРЫШ!!!", "Dealer busted! You have 21!!! You win the game!")
            else:
                messagebox.showinfo("ВЫИГРЫШ!!!", "DEALER BUSTED! You win the game!")
            winner = 'player'
            return True, winner
        elif max(player.score) == max(dealer.score):
            player.player_result.config(bg='grey')
            self.wallet.config(bg="green", text=f'Ваш кошелёк: {self.money} + {bet}')
            if max(player.score) == max(dealer.score) == 21:
                dealer.dealer_result.config(text="BLACKJACK...")
                messagebox.showinfo("НИЧЬЯ", "Ничья... НУ НИЧЕГО СЕБЕ...      ")
            else:
                messagebox.showinfo("НИЧЬЯ", "Ничья...      ")
            return True, winner
        elif max(player.score) > max(dealer.score):
            player.player_result.config(bg="green")
            winner = 'player'
        elif max(player.score) < max(dealer.score):
            self.bet.config(bg='red')
            self.wallet.config(bg="red")
            if max(dealer.score) == 21:
                dealer.dealer_result.config(text="21!!! BLACKJACK!!!", bg="red")
                messagebox.showerror("ВЫ ПРОИГРАЛИ!!!", "21!!! BLACKJACK!!!")
            else:
                dealer.dealer_result.config(bg="red")
                messagebox.showerror("ВЫ ПРОИГРАЛИ!", "Вы проиграли - у дилера очков больше")
            winner = 'dealer'
        return False, winner

    def hit_bust(self, player):
        if max(player.score) > 21:
            self.wallet.config(bg="red", text=f'Ваш кошелёк: {self.money}')
            self.bet.config(bg='red')
            player.player_result.config(bg="red")
            messagebox.showerror("ВЫ ПРОИГРАЛИ!", "Busted! Счёт больше 21         ")
            return True
        return False
