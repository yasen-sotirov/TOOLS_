


def calculate_winnings(stake, odds):
    if stake <= 0:
        return 0

    winnings = stake
    for odd in odds:
        winnings = winnings * odd

    return winnings - stake
