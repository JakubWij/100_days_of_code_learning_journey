import art
from game_data import data
import random


# function that draws random dict from gamedata dictionary
def random_dictionary():
    return random.choice(data)


# compare 2 followers and chose higher
def followers_comparison(dictionary_a, dictionary_b):
    """takes both dict and returns the winner"""
    if dictionary_a["follower_count"] > dictionary_b["follower_count"]:
        return "a"
    elif dictionary_a["follower_count"] == dictionary_b["follower_count"]:
        return "0"
    else:
        return "b"


def main_body():
    """print statements and compare strings"""
    print(art.logo)
    print(f"Compare A: {dict_1['name']}, a {dict_1['description']}, from {dict_1['country']}.{dict_1['follower_count']}")
    print(art.vs)
    print(f"Against B: {dict_2['name']}, a {dict_2['description']}, from {dict_2['country']}.{dict_2['follower_count']}")


# clear = lambda: os.system('clear')
dict_1 = random_dictionary()
score_counter = 0

while True:
    # save all the data for person 1 and 2
    dict_2 = random_dictionary()
    main_body()
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    outcome = followers_comparison(dict_1, dict_2)
    if choice == outcome:
        score_counter += 1
        print(f"You'r right. Your current score {score_counter}")
    elif outcome == "0":
        print("Both accounts have the same amount of followers")
    else:
        print(f"Sorry, that's wrong. Final score: {score_counter}")
        break

    dict_1 = dict_2

