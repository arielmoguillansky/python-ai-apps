from art import logo
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def compare(u_score, pc_score):
    if pc_score == 21:
        return "Computer got blackjack. You lose!"
    elif u_score == 21:
        return "You got blackjack. You win!"
    elif u_score > 21:
        return "Busted. You lose!"
    elif pc_score > 21:
        return "Opponent went over. You win!"
    elif u_score > pc_score:
        return "You win!"
    elif u_score == pc_score:
        return "It's a draw!"
    else:
        return "You lose!"

def get_cards(iterations):
    cards = []
    for _ in range(iterations):
        cards.append(random.choice(deck))
    return cards if iterations > 1 else cards[0]


def get_score(cards):
    get_sum = sum(cards)
    while get_sum > 21 and 11 in cards:
        ace_index = cards.index(11)
        cards[ace_index] = 1
        get_sum = sum(cards)
    return get_sum

while start_game == 'y':
    print(logo)
    user_cards = get_cards(2)
    computer_cards = get_cards(2)
    user_score = get_score(user_cards)
    pc_score = get_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    while user_score < 21:
        continue_playing = input("Type 'y' to get another card, type 'n' to pass: ")
        if continue_playing == 'n':
            break
        user_cards.append(get_cards(1))
        user_score = get_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

    while pc_score < 17:
        computer_cards.append(get_cards(1))
        pc_score = get_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score {pc_score}")
    print("----------------------------------------------------------------")
    print(compare(user_score, pc_score))

    start_game = input("Do you want to play a new game? Type 'y' or 'n': ")
    print("\n" * 100)


