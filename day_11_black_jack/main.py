import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\ |\\__,_|\\___|_|\_\\
      |  \\/ K|                            _/ |                
      '------'                           |__/    
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_random_card():
    return random.choice(cards)


def add_card(entity, card):
    entity["cards"].append(card)
    entity["score"] += card


computer_cards = {"score": 0, "cards": []}
user_cards = {"score": 0, "cards": []}

is_game_on = True

print(logo)

for i in range(0, 2):
    add_card(computer_cards, get_random_card())
    add_card(user_cards, get_random_card())

print(f"Your cards: {user_cards['cards']}, current score: {user_cards['score']}")
print(f"Computer's first card: {computer_cards['cards'][0]}")
while is_game_on:
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == "y":
        add_card(user_cards, get_random_card())
        if user_cards['score'] > 21:
            if 11 in user_cards['cards']:
                index = user_cards['cards'].index(11)
                user_cards['cards'][index] = 1
                user_cards['score'] -= 10
            else:
                is_game_on = False
        print(f"Your cards: {user_cards['cards']}, current score: {user_cards['score']}")
    else:
        while computer_cards['score'] < 17:
            add_card(computer_cards, get_random_card())
            if computer_cards['score'] > 21:
                if 11 in computer_cards['cards']:
                    index = computer_cards['cards'].index(11)
                    computer_cards['cards'][index] = 1
                    computer_cards['score'] -= 10
                else:
                    is_game_on = False
        is_game_on = False

print(f"Your final hand: {user_cards['cards']}, final score: {user_cards['score']}")
print(f"Computer's final hand: {computer_cards['cards']}, final score: {computer_cards['score']}")
if user_cards['score'] > 21:
    print("You went over. You loose 😭")
elif computer_cards['score'] > 21:
    print("Opponent went over. You win 😁")
elif user_cards['score'] == computer_cards["score"]:
    print("It's a draw! 🙃")
elif user_cards['score'] > computer_cards['score']:
    print("You win 😁")
else:
    print("You loose 😭")