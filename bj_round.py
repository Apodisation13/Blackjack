from class_gamer import Player, Dealer
from winner import check_starting_bj, check_winner
from calc_card import deck
from class_money import Money


def bj_round(money, bet):
    player = Player(deck)
    dealer = Dealer(deck)

    starting_bj = check_starting_bj(player.score, dealer.score, dealer.hand)
    if not starting_bj[1]:
        return starting_bj[0], False, starting_bj[2]  # если победитель выявился на этапе первоначальной раздачи
    else:

        double_block = False
        double_status = False

        while True:
            if money.start_cash < 2 * bet:
                double_block = True

            print("\nВы можете ввести: hit/h чтобы взять ещё карту, "
                  "stand/s чтобы остановиться, double/d чтобы удвоить ставку и взять одну карту")

            command = input("\nВведите команду: ")

            if command.lower() == "h":
                double_block = True
                player.hit(deck)
                if max(player.score) > 21:
                    break
                elif max(player.score) == 21:
                    print("\033[32m{}\033[0m".format('BLACKJACK!!!'))
                    dealer.dealer_AI(deck, player)
                    break

            elif command.lower() == "s":
                dealer.dealer_AI(deck, player)
                break

            elif command.lower() == 'd' and not double_block:
                player.hit(deck)
                dealer.dealer_AI(deck, player)
                double_status = True
                break

            else:
                print("Неправильная команда")

        winner = check_winner(player.score, dealer.score, player.hand, dealer.hand)

    return winner, double_status, starting_bj[2]


# bj_round() # тестирование одного раунда без денег: нужно убрать аргументы money и bet из параметров
# а ниже функция это уже с деньгами
def game():
    print(len(deck))
    copy_deck = deck.copy()
    money = Money()
    while money.start_cash != 0:
        bet = money.place_bet()
        if money.can_bet(bet):
            print("\n-----------------------НОВЫЙ РАУНД-----------------------")
            winner, double_status, starting_blackjack_status = bj_round(money, bet)
            print(winner, double_status, starting_blackjack_status)
            money.payment(bet, winner, double_status, starting_blackjack_status)
            print(len(copy_deck))