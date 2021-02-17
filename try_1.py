from random import choice


def starting_draw_dealer(cards: list):
    """начальный дро дилера"""
    starting_dealer_hand = []
    for _ in range(2):
        dealer_choice = choice(cards)
        cards.remove(dealer_choice)
        starting_dealer_hand.append(dealer_choice)
    print(f"Карты в руке дилера: ['{starting_dealer_hand[0]}', ??]")
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


def calc_cards(hand: list):
    """преобразовать карты в удобные для вычисления"""
    calc_hand = []
    for card in hand:
        if card in ['J', 'Q', 'K']:
            calc_hand.append(10)
        elif card == "A":
            calc_hand.append(11)
        else:
            calc_hand.append(card)
    # print(calc_hand)
    return calc_hand


def check_blackjack(hand: list, player: str):
    """проверить нет ли 21 в стартовой руке дилера или игрока"""
    card_hand = hand.copy()
    result = sum(hand)
    if result == 21:
        if player == "Dealer":
            print(f'Карты в руке дилера: {hand}')
            print("\033[31m{}\033[0m".format("BLACKJACK!!! Dealer wins, you lose!"))
            return True
        elif player == "Player":
            print("\033[32m{}\033[0m".format('BLACKJACK!!! You win the game!'))
            return True
    return False


def check_score(hand: list, player: str):
    """проверяем счёт"""
    result = sum(hand)
    # print(f"Ваш результат - {result}")
    if result > 21:
        if player == "Player":
            print("\033[31m{}\033[0m".format("BUSTED! You lose the game!"))
        elif player == "Dealer":
            print("\033[32m{}\033[0m".format('DEALER BUSTED! You win the game!'))
    elif result == 21:
        if player == "Player":
            print("\033[32m{}\033[0m".format('BLACKJACK!!!'))
        elif player == "Dealer":
            print("\033[31m{}\033[0m".format('BLACKJACK!!! Dealer wins, you lose!'))
    return result


def hit(cards: list, hand: list):
    """игрок берет карту"""
    player_choice = choice(cards)
    cards.remove(player_choice)
    hand.append(player_choice)
    print(hand)
    return hand


cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
         6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
         "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K",
         "A", "A", "A", "A"]


dealer_hand = starting_draw_dealer(cards)
calc_dealer_hand = calc_cards(dealer_hand)

if not check_blackjack(calc_dealer_hand, "Dealer"):

    player_hand = starting_draw_player(cards)
    calc_player_hand = calc_cards(player_hand)

    if not check_blackjack(calc_player_hand, 'Player'):
        print("\nВы можете ввести: hit/h чтобы взять ещё карту, "
              "stand/s чтобы остановиться\n")

        print(f'Ваш результат - {sum(calc_player_hand)}')

        while True:
            command = input("Введите команду: ")

            if command.lower() in ["hit", 'h']:
                player_hand = hit(cards, player_hand)
                calc_player_hand = calc_cards(player_hand)
                player_result = check_score(calc_player_hand, "Player")
                print(f'Ваш результат - {sum(calc_player_hand)}')
                if player_result >= 21:
                    break

            elif command.lower() in ["stand", "s"]:
                player_result = check_score(calc_player_hand, "Player")
                dealer_result = check_score(calc_dealer_hand, "Dealer")
                while dealer_result < player_result:
                    dealer_hand = hit(cards, dealer_hand)
                    calc_dealer_hand = calc_cards(dealer_hand)
                    dealer_result = check_score(calc_dealer_hand, "Dealer")
                print(f'Игрок: {player_hand} - {player_result}, Дилер: {dealer_hand} - {dealer_result}')
                if dealer_result >= 21:
                    break
                elif player_result == dealer_result:
                    print("НИЧЬЯ")
                elif player_result < dealer_result:
                    print("\033[31m{}\033[0m".format('Dealer wins, you lose!'))
                break
