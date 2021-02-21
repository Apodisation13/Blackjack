def check_starting_bj(player_result, dealer_result, dealer_hand):
    winner = ''
    if max(player_result) == 21:
        print("\033[32m{}\033[0m".format('BLACKJACK!!! You win the game!'))
        winner = "player"
        return winner, False
    elif max(dealer_result) == 21:
        print("\033[31m{}\033[0m".format(f'{dealer_hand} - BLACKJACK!!! Dealer wins, you lose!'))
        winner = "dealer"
        return winner, False
    return winner, True


def check_winner(player_result, dealer_result, player_hand, dealer_hand):

    winner = ''
    if max(player_result) > 21:
        print("\033[31m{}\033[0m".format("BUSTED! You lose the game!"))
        winner = 'player'
        return winner
    else:
        print(f'Игрок: {player_hand} - {max(player_result)}, Дилер: {dealer_hand} - {max(dealer_result)}')
        if max(dealer_result) > 21:
            print("\033[32m{}\033[0m".format("DEALER BUSTED! You win the game!"))
            winner = 'dealer'
        elif max(player_result) == max(dealer_result):
            print("НИЧЬЯ")
        elif max(player_result) > max(dealer_result):
            if max(player_result) == 21:
                print("\033[32m{}\033[0m".format('BLACKJACK!!! You win the game!'))
            else:
                print("\033[32m{}\033[0m".format("You win the game!"))
            winner = 'player'
        elif max(dealer_result) > max(player_result):
            if max(dealer_result) == 21:
                print("\033[31m{}\033[0m".format(f'{dealer_hand} - BLACKJACK!!! Dealer wins, you lose!'))
            else:
                print("\033[31m{}\033[0m".format("Dealer wins the game! You lose!"))
            winner = 'dealer'
        return winner
