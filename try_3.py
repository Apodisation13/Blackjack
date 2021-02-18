from random import choice
from calc_card import calc_cards


def starting_draw_dealer(cards: list):
    """начальный дро дилера"""
    starting_dealer_hand = []
    for _ in range(2):
        dealer_choice = choice(cards)
        cards.remove(dealer_choice)
        starting_dealer_hand.append(dealer_choice)
    print(f"Карты в руке дилера: ['{starting_dealer_hand[0]}', ??]")
    print(starting_dealer_hand)
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
    return hand


def check_score(result: tuple):
    print(f'Результат игрока {result[0]}')
    if result[1]:
        if result[1] == 21:
            print("BLACKJACK!!!")
            return result[1]
        print(f'Результат игрока {result[0]}/{result[1]}')
    else:
        if result[0] > 21:
            print("\033[31m{}\033[0m".format("BUSTED! You lose the game!"))
        elif result[0] == 21:
            print("BLACKJACK!!!")
    return result[0]


cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
         6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
         "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K",
         "A", "A", "A", "A"]


dealer_hand = starting_draw_dealer(cards)
player_hand = starting_draw_player(cards)
player_result = calc_cards(player_hand, first_draw=True)
dealer_result = calc_cards(dealer_hand, first_draw=True)

if player_result[1]:
    print(f'Результат игрока {player_result[0]}/{player_result[1]}')
else:
    print(f'Результат игрока {player_result[0]}')

if dealer_result[0] == 21 and player_result[0] != 21:
    print("\033[31m{}\033[0m".format(f'{dealer_hand} - BLACKJACK!!! Dealer wins, you lose!'))
elif player_result[0] == 21 and dealer_result[0] != 21:
    print("\033[32m{}\033[0m".format('BLACKJACK!!! You win the game!'))
elif player_result[0] == 21 and dealer_result[0] == 21:
    print("НИЧЬЯ! НУ НИЧЕГО СЕБЕ...")
else:

    print("\nВы можете ввести: hit/h чтобы взять ещё карту, "
              "stand/s чтобы остановиться, double/d чтобы удвоить ставку и взять одну карту")

    while True:
        command = input("\nВведите команду: ")

        if command.lower() in ["hit", 'h']:
            hit(cards, player_hand)
            player_result = calc_cards(player_hand, first_draw=False)
            print(f'Карты в руке игрока: {player_hand}')
            player_result = check_score(player_result)
            if player_result >= 21:
                break
