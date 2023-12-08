def main():
    winnings = 0
    card_values = {
        "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, 
        "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13
    }
    hands_data = []

    with open('sample-input.txt', 'r') as file:
        for line in file:
            hand_and_bid = line.strip().split()
            hand = list(hand_and_bid[0])
            bid = int(hand_and_bid[1])
            score = sum(card_values[card] for card in hand) # the score of the hand, disregarding kind
            card_freq = {card: hand.count(card) for card in hand} # counts how many times card appears in hand, makes it a dictionary
            kind_of_hand = kind(card_freq)
            hands_data.append((kind_of_hand, score, hand, bid)) # gathers this data as a tuple

    # sorts, ascending (rev=false), first by [0] (kind) then [1] (score) of each tuple in the list
    sorted_hands = sorted(hands_data, key=lambda x: (x[0], -x[1]), reverse=False)

    # assigning ranks
    for rank, hand_data in enumerate(sorted_hands, 1):
        print(f"Rank {rank}: Kind {hand_data[0]}, Score {hand_data[1]}, Hand {hand_data[2]}, Bid {hand_data[3]}")
        winnings += rank * hand_data[3]
        print(winnings)
        print('')

def kind(card_freq):
    freq_values = list(card_freq.values())

    if 5 in freq_values:
        return 7  # five of a kind
    elif 4 in freq_values:
        return 6  # four of a kind
    elif 3 in freq_values:
        if 2 in freq_values:
            return 5  # full house
        else:
            return 4  # three of a kind
    elif freq_values.count(2) == 2:
        return 3  # two pair
    elif 2 in freq_values:
        return 2  # one pair
    else:
        return 1  # high card

main()