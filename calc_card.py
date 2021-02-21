def calc_cards(hand: list):

    calc_hand = []
    result = 0
    result_ace = 0

    if hand == ["A", "A"]:
        # print("два туза в стартовой руке")
        return 12, 0

    ace_count = hand.count("A")
    # print("количество тузов", ace_count)

    for card in hand:
        if card in ['J', 'Q', 'K']:
            calc_hand.append(10)
        elif card != "A":
            calc_hand.append(card)

    # print("сумма руки без туза", sum(calc_hand))

    if ace_count == 1:
        result += ace_count
        result_ace += 11
    elif ace_count == 2:
        result += ace_count
        result_ace += 12
    elif ace_count == 3:
        result += ace_count
        result_ace += 13
    elif ace_count == 4:
        result += ace_count
        result_ace += 14

    if ace_count > 0:
        result_ace += sum(calc_hand)
        # print("Результат с тузами", result_ace)
        if result_ace > 21:
            result_ace = 0

    result += sum(calc_hand)
    return result, result_ace


cards_default = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
                 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
                 "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K",
                 "A", "A", "A", "A"]