def calc_cards(hand: list, first_draw: bool):

    calc_hand = []
    result = 0
    result_ace = 0
    ace = False

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
        elif card == "A" and first_draw:
            calc_hand.append(11)

    # print("сумма руки без туза", sum(calc_hand))

    if ace_count > 0 and not first_draw:
        ace = True
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

    if ace:
        result_ace += sum(calc_hand)
        # print("Результат с тузами", result_ace)
        if result_ace > 21:
            result_ace = 0

    result += sum(calc_hand)
    return result, result_ace
