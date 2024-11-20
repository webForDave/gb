def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    rounds = [r for r in range(number, number + 3)]
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return bool(number in rounds)

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    actual_average = sum(hand) / len(hand)

    # takes the average of the first and last number in the hand
    avg_first_and_last = (hand[0] + hand[-1]) / 2

    # returns the median of the hand
    def median(cards):
        middle_value = len(cards) // 2
        return cards[middle_value]
    # print(actual_average, avg_first_and_last, median(hand))

    return bool(avg_first_and_last == actual_average or median(hand) == actual_average)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_list = []
    odd_list = []
    for number in hand:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

    if len(even_list) == 0:
        even_list = odd_list
        avg_even = sum(even_list) / len(even_list)
    else:
        avg_even = sum(even_list) / len(even_list)

    if len(odd_list) == 0:
        odd_list = even_list
        avg_odd = sum(odd_list) / len(odd_list)
    else:
        avg_odd = sum(odd_list) / len(odd_list)


    return bool(avg_even == avg_odd)


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 11 * 2
    return hand


print(maybe_double_last([5, 9, 10]))
