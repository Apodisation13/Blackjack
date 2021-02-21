from random import choice
from calc_card import calc_cards
from class_money import Money


def starting_draw_dealer(cards: list):
    """начальный дро дилера"""
    starting_dealer_hand = []
    for _ in range(2):
        dealer_choice = choice(cards)
        cards.remove(dealer_choice)
        starting_dealer_hand.append(dealer_choice)
    print("-----------------------НОВЫЙ РАУНД-----------------------")
    print(f"Карты в руке дилера: ['{starting_dealer_hand[0]}', ??]")
    # print(starting_dealer_hand)
    return starting_dealer_hand


def starting_draw_player(cards: list):
    """начальный дро игрока"""
    starting_player_hand = []
    for _ in range(2):
        player_choice = choice(cards)
        cards.remove(player_choice)
        starting_player_hand.append(player_choice)
    print(f'Карты в руке игрока: {starting_player_hand}')
    return starting_player_hand


def hit(cards: list, hand: list):
    """кто-то берет 1 карту"""
    player_choice = choice(cards)
    cards.remove(player_choice)
    hand.append(player_choice)
    print(f'hit {player_choice}')


def check_score(result: tuple):
    if result[1]:
        if result[1] == 21:
            print("\033[32m{}\033[0m".format("BLACKJACK!!!"))
            return result[1]
        print(f'Результат игрока {result[0]}/{result[1]}')
    else:
        print(f'Результат игрока {result[0]}')
        if result[0] > 21:
            print("\033[31m{}\033[0m".format("BUSTED! You lose the game!"))
        elif result[0] == 21:
            print("\033[32m{}\033[0m".format("BLACKJACK!!!"))
    return result[0]


def check_starting_hand_blackjack(player, dealer, d_hand):
    if dealer == 21 and player != 21:
        print("\033[31m{}\033[0m".format(f'{d_hand} - BLACKJACK!!! Dealer wins, you lose!'))
        money.lose(bet)
    elif player == 21 and dealer != 21:
        print("\033[32m{}\033[0m".format('BLACKJACK!!! You win the game!'))
        money.win(bet * 2)
    elif player == 21 and dealer == 21:
        print("НИЧЬЯ! НУ НИЧЕГО СЕБЕ...")
    else:
        return True


def dealer_AI(dealer_score, player_score, dealer_hand, player_hand):
    """логика дилера - взять карту пока у него не столько же сколько у игрока"""
    print(f'\nКарты дилера: {dealer_hand} - {dealer_score}')
    while dealer_score < player_score:
        hit(cards, dealer_hand)
        d_result = calc_cards(dealer_hand)
        if d_result[1]:
            dealer_score = d_result[1]
            print(f'Карты в руке дилера: {dealer_hand} - {d_result[0]}/{d_result[1]}')
        else:
            dealer_score = d_result[0]
            print(f'Карты в руке дилера: {dealer_hand} - {dealer_score}')
    print(f'Игрок: {player_hand} - {player_score}, Дилер: {dealer_hand} - {dealer_score}')
    return dealer_score


def check_win(player_score, dealer_score, double_bet_status):
    if dealer_score > 21:
        print("\033[32m{}\033[0m".format("DEALER BUSTED! You win the game!"))
        if double_bet_status:
            money.win(bet * 2)
            return
        money.win(bet)
        return
    if dealer_score == 21:
        if player_score == 21:
            print("НИЧЬЯ! НУ НИЧЕГО СЕБЕ...")
            return
        print("\033[31m{}\033[0m".format("BLACKJACK! Dealer wins the game! You lose!"))
        if double_bet_status:
            money.lose(bet * 2)
            return
        money.lose(bet)
        return
    if dealer_score == player_score:
        print('НИЧЬЯ')
    if dealer_score > player_score:
        print("\033[31m{}\033[0m".format("Dealer wins the game! You lose!"))
        if double_bet_status:
            money.lose(bet * 2)
            return
        money.lose(bet)
    if dealer_score < player_score:
        print("\033[32m{}\033[0m".format("You win the game!"))
        if double_bet_status:
            money.win(bet * 2)
            return
        money.win(bet)


def game(cards: list):
    dealer_hand = starting_draw_dealer(cards)
    # dealer_hand = ["A", 2]
    # print(dealer_hand)
    player_hand = starting_draw_player(cards)
    # player_hand = ["A", 10]
    # print(player_hand)
    player_result = calc_cards(player_hand)
    dealer_result = calc_cards(dealer_hand)

    if player_result[1]:
        print(f'Результат игрока {player_result[0]}/{player_result[1]}')
    else:
        print(f'Результат игрока {player_result[0]}')

    if check_starting_hand_blackjack(max(player_result), max(dealer_result), dealer_hand):

        print("\nВы можете ввести: hit/h чтобы взять ещё карту, "
              "stand/s чтобы остановиться, double/d чтобы удвоить ставку и взять одну карту")

        double_block = False

        while True:
            if money.start_cash < 2 * bet:
                double_block = True

            command = input("\nВведите команду: ")

            if command.lower() in ["hit", 'h']:
                double_block = True
                hit(cards, player_hand)
                # player_hand.append(3)
                player_result = calc_cards(player_hand)
                # print(player_result)
                print(f'Карты в руке игрока: {player_hand}')
                player_score = check_score(player_result)
                # print(player_score)
                if player_score == 21:
                    dealer_score = dealer_AI(dealer_result[0], player_score, dealer_hand, player_hand)
                    check_win(player_score, dealer_score, double_bet_status=False)
                    break
                if player_score > 21:
                    money.lose(bet)
                    break

            elif command.lower() in ["stand", "s"]:
                dealer_score = dealer_AI(dealer_result[0], max(player_result), dealer_hand, player_hand)
                check_win(max(player_result), dealer_score, double_bet_status=False)
                break

            elif command.lower() in ["double", "d"] and not double_block:
                print(f'Вы поставили ещё {bet} рублей')
                hit(cards, player_hand)
                # player_hand.append("A")
                player_result = calc_cards(player_hand)
                player_score = max(player_result)
                print(f'Карты в руке игрока: {player_hand} - {player_score}')
                if player_score <= 21:
                    if player_score == 21:
                        print("\033[32m{}\033[0m".format("BLACKJACK!!!"))
                    dealer_score = dealer_AI(dealer_result[0], player_score, dealer_hand, player_hand)

                    check_win(player_score, dealer_score, double_bet_status=True)
                    break

                if player_score > 21:
                    print("\033[31m{}\033[0m".format("BUSTED! You lose the game!"))
                    money.lose(bet=bet * 2)
                    break

            else:
                print('Неправильная команда')


cards_default = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
                 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
                 "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K",
                 "A", "A", "A", "A"]
cards = cards_default.copy()

if __name__ == "__main__":
    money = Money()
    while money.start_cash != 0:
        try:
            bet = int(input("\nСдейлайте ставку: "))
            if bet <= 0:
                print("Вводить только числа БОЛЬШЕ НУЛЯ")
        except ValueError:
            print('Вводить только целые числа')
        else:
            if money.can_bet(bet):
                game(cards)
                money.show_wallet()
                cards = cards_default
