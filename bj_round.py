from class_gamer import Player, Dealer
from winner import check_starting_bj, check_winner
from calc_card import cards_default


def bj_round():
    player = Player()
    dealer = Dealer()

    starting_bj = check_starting_bj(player.score, dealer.score, dealer.hand)
    if not starting_bj[1]:
        return starting_bj[0] # если победитель выявился на этапе первоначальной раздачи
    else:
        while True:
            print("\nВы можете ввести: hit/h чтобы взять ещё карту, "
                  "stand/s чтобы остановиться, double/d чтобы удвоить ставку и взять одну карту")

            command = input("\nВведите команду: ")

            if command.lower() == "h":

                player.hit(cards_default)
                if max(player.score) > 21:
                    break
                elif max(player.score) == 21:
                    print("\033[32m{}\033[0m".format('BLACKJACK!!!'))
                    dealer.dealer_AI(cards_default, player)
                    break

            elif command.lower() == "s":
                dealer.dealer_AI(cards_default, player)
                break

            elif command.lower() == 'd':
                player.hit(cards_default)
                dealer.dealer_AI(cards_default, player)
                break

        winner = check_winner(player.score, dealer.score, player.hand, dealer.hand)

    return winner


winner = bj_round()
