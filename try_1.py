from random import choice


def starting_draw_dealer(cards: list):
    starting_dealer_hand = []
    for _ in range(2):
        dealer_choice = choice(cards)
        cards.remove(dealer_choice)
        starting_dealer_hand.append(dealer_choice)
    print(f"Карты в руке дилера: ['{starting_dealer_hand[0]}', ??]")
    return starting_dealer_hand


def starting_draw_player(cards: list):
    starting_player_hand = []
    for _ in range(2):
        player_choice = choice(cards)
        cards.remove(player_choice)
        starting_player_hand.append(player_choice)
    print(f'Карты в руке игрока: {starting_player_hand}')
    return starting_player_hand


def calc_cards(hand: list):
    calc_hand = []
    for card in hand:
        if card in ['J', 'Q', 'K']:
            calc_hand.append(10)
        elif card == "A":
            calc_hand.append(11)
        else:
            calc_hand.append(card)
    print(calc_hand)
    return calc_hand


def check_blackjack(hand: list, player: str):
    card_hand = hand.copy()
    if sum(hand) == 21 and player == "Dealer":
        print(f'Карты в руке дилера: {card_hand}')
        print(f'21!!! {player} wins the game!')
        return True
    if sum(hand) == 21 and player == "Player":
        print(f'21!!! {player} wins the game!')
        return
    return False


cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
         6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
         "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K",
         "A", "A", "A", "A"]
player_count = 0
dealer_count = 0


dealer_hand = starting_draw_dealer(cards)
calc_dealer_hand = calc_cards(dealer_hand)

if not check_blackjack(calc_dealer_hand, "Dealer"):
    player_hand = starting_draw_player(cards)
    calc_player_hand = calc_cards(player_hand)

    if not check_blackjack(calc_player_hand, 'Player'):
        pass
