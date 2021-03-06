class Money:
    def __init__(self):
        status = True
        while status:
            try:
                self.start_cash = int(input("Введите, сколько денег вы хотите взять с собой за стол: "))
                if self.start_cash <= 0:
                    print("Нельзя вводить отрицательное или ноль")
                    continue
                print(f'У вас при себе {self.start_cash} рублей, удачи в игре!')
                status = False
            except ValueError:
                print("Надо ввести только целое число")

    def show_wallet(self):
        print(f'У вас в игре {self.start_cash} рублей')

    def can_bet(self, bet):
        if bet > self.start_cash:
            print(f'Нельзя поставить {bet}, у вас есть только {self.start_cash}')
            return False
        return True

    def win(self, bet):
        self.start_cash += bet
        print(f'Вы выигрываете {bet * 2} рублей')

    def lose(self, bet):
        self.start_cash -= bet
        print(f'Вы проигрываете {bet} рублей')
        if self.start_cash == 0:
            print('БАНКРОТ!')


if __name__ == "__main__":
    money = Money()
    while money.start_cash != 0:
        command = input("Введите команду: ")

        if command == "s":
            money.show_wallet()
        elif command == "w":
            try:
                bet = int(input("Введите ставку: "))
            except ValueError:
                print('Вводить только целые числа')
            else:
                money.win(bet)
        elif command == "l":
            try:
                bet = int(input("Введите ставку: "))
            except ValueError:
                print('Вводить только целые числа')
            else:
                money.lose(bet)
