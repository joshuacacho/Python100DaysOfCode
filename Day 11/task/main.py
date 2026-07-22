# blackjack game

from art import logo
import random
import sys

#cards array of possible values
    # cae can be 11 or 1 so not putting 1 within it
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def two_ace_deal(cards_dealt):
    """Special check if both random cards are 11 somehow"""
    ace_count = cards_dealt.count(11)
    if ace_count == 2:
        cards_dealt[0] = 1  # set one card to 1 otherwise the user busts immediately

    return cards_dealt

def add_cards(num1,num2):
    """Adds two numbers together"""
    return num1 + num2

def use_ace_value(current_card_score, list_to_append, card):
    """Checks to see if random card of ace is used and if so is it better to use 11 or 1 for its value"""
    if card == 11 and (current_card_score + card > 21):
        card = 1
        list_to_append.append(card)
        # update player score
        current_card_score = add_cards(current_card_score, card)
    else:
        # append the player card to total cards dealt so far
        list_to_append.append(card)
        current_card_score = add_cards(current_card_score, card)

    return current_card_score

def determine_winner(player_score, computer_score):
    """Determines Winner of Blackjack Game"""
    if computer_score >= 17 and computer_score <= 21:
        if player_score > computer_score:
            print("You win with a better score! 😁")
        elif player_score == computer_score:
            print("Draw! 🤝")
        else:
            print("You lose with a worse score! 😤")
    elif computer_score > 21:
        print("You win because the computer went over! 😁")
    elif computer_score == computer_score:
        print("Draw! 🤝")
    else:
        print("Bug")


# blackjack game
def blackjack():

    # this needs to be inside the blackjack() game to be used for recursion
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_game == "y":

        #print the logo out
        print(logo)

        # player 1 initial 2 random cards
        p_cards = random.choices(cards, k=2)

        #debug double aces where the values would be 11 and ensure one is 11
            #p_cards[0] = 11
            #p_cards[1] = 11

        #if both cards dealt are 11, 11 make one of them 1 as we dont have split function
        two_ace_deal(p_cards)
        p_current_score = add_cards(p_cards[0],p_cards[1])

        print(f"Your cards: {p_cards}, current score: {p_current_score}")

        # computer initial random cards
            # pull two cards for computer but only show one card
        c_cards = random.choices(cards, k=2)

        # if both cards dealt are 11, 11 make one of them 1 as we dont have split function
        two_ace_deal(c_cards)
        c_current_score = add_cards(c_cards[0], c_cards[1])
        print(f"Computer's first card: {c_cards[0]}")

        # ask user if they want another card or not
        p1_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        while p1_another_card == 'y':

            # give the player another card
            p_hit_me_card = random.choice(cards)  # 11 to test belie use_ace_value

            # if player card is ace and score would be > 21 (p_hit_me_card = 11) then set card to 1
            p_current_score = use_ace_value(p_current_score, p_cards, p_hit_me_card)

            # output player and computer totals
            print(f"Your cards: {p_cards}, current score: {p_current_score}")
            print(f"Computer's first card: {c_cards[0]}")

            if p_current_score > 21:
                print(f"Your final hand: {p_cards}, final score: {p_current_score}")
                print(f"Computer's final hand: {c_cards} is {c_current_score}")
                print(f"You went over. You lose 😭")
                # This is recursion! It starts a brand new blackjack game fresh.
                blackjack()

            p1_another_card = input("Type 'y' to get another card, type 'n' to pass: ")


        if p1_another_card == "n":

            # Dealer's Turn: Once all players have finished, the dealer reveals their face-down card.
            # The dealer must follow strict rules: they must hit until their cards total 17 or more.
            while c_current_score <= 21 :

                # no need to draw anymore cards
                if c_current_score >= 17 and c_current_score <= 21:
                    break

                c_hit_me_card = random.choice(cards) # 11 to test belie use_ace_value

                # if computer card is ace and score would be > 21 (p_hit_me_card = 11) then set card to 1
                c_current_score = use_ace_value(c_current_score, c_cards, c_hit_me_card)

            # here we flip both users cards up and show
            print(f"Your final hand: {p_cards}, final score: {p_current_score}")
            print(f"Computer's final hand: {c_cards} is {c_current_score}")

            # determine the winner of the game
                # based on the rules
            determine_winner(p_current_score, c_current_score)
            blackjack()

    if play_game == "n":
        # exit game
        sys.exit()


blackjack()


#
#
# # blackjack game
#
# from art import logo
# import random
# import sys
#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# def two_ace_deal(cards_dealt):
#     """Special check if both random cards are 11 somehow"""
#     ace_count = cards_dealt.count(11)
#     if ace_count == 2:
#         cards_dealt[0] = 1  # set one card to 1 otherwise the user busts immediately
#
#     return cards_dealt
#
# def add_cards(num1,num2):
#     """Adds two numbers together"""
#     return num1 + num2
#
# def use_ace_value(current_card_score, card):
#     if card == 11 and (current_card_score + card > 21):
#         card = 1
#
#     return card
#
# def determine_winner(player_score, computer_score):
#     """Determines Winner of Blackjack Game"""
#     if computer_score >= 17 and computer_score <= 21:
#         if player_score > computer_score:
#             print("You win! 😁")
#         elif player_score == computer_score:
#             print("Draw! 🤝")
#         else:
#             print("You lose! 😤")
#     elif computer_score > 21:
#         print("You win")
#     elif computer_score == computer_score:
#         print("Draw! 🤝")
#     else:
#         print("Bug")
#
#
# # blackjack game
# def blackjack():
#
#     # this needs to be inside the blackjack() game to be used for recursion
#     play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#
#     if play_game == "y":
#
#         #print the logo out
#         print(logo)
#
#         # player 1 initial 2 random cards
#         p_cards = random.choices(cards, k=2)
#
#         #debug double aces where the values would be 11 and ensure one is 11
#             # p_cards[0] = 5
#             # p_cards[1] = 11
#
#         #if both cards dealt are 11, 11 make one of them 1 as we dont have split function
#         two_ace_deal(p_cards)
#         p_current_score = add_cards(p_cards[0],p_cards[1])
#
#         print(f"Your cards: {p_cards}, current score: {p_current_score}")
#
#         # computer initial random cards
#             # pull two cards for computer but only show one card
#         c_cards = random.choices(cards, k=2)
#
#         # if both cards dealt are 11, 11 make one of them 1 as we dont have split function
#         two_ace_deal(c_cards)
#         c_current_score = add_cards(c_cards[0], c_cards[1])
#         print(f"Computer's first card: {c_cards[0]}")
#
#         # ask user if they want another card or not
#         p1_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
#
#         while p1_another_card == 'y':
#
#             # give the player another card
#             p_hit_me_card = random.choice(cards)
#             # append the player card to total cards dealt so far
#             p_cards.append(p_hit_me_card)
#             # update player score
#             p_current_score = add_cards(p_current_score, p_hit_me_card)
#
#             # output player and computer totals
#             print(f"Your cards: {p_cards}, current score: {p_current_score}")
#             print(f"Computer's first card: {c_cards[0]}")
#
#             if p_current_score > 21:
#                 print(f"Your final hand: {p_cards}, final score: {p_current_score}")
#                 print(f"Computer's final hand: {c_cards} is {c_current_score}")
#                 print(f"You went over. You lose 😭")
#                 # This is recursion! It starts a brand new blackjack game fresh.
#                 blackjack()
#
#             p1_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
#
#
#         if p1_another_card == "n":
#
#             # Dealer's Turn: Once all players have finished, the dealer reveals their face-down card.
#             # The dealer must follow strict rules: they must hit until their cards total 17 or more.
#             while c_current_score <= 21 :
#
#                 # no need to draw anymore cards
#                 if c_current_score >= 17 and c_current_score <= 21:
#                     break
#
#                 c_hit_me_card = random.choice(cards)
#                 # append the player card to total cards dealt so far
#                 c_cards.append(c_hit_me_card)
#                 # update player score
#                 c_current_score = add_cards(c_current_score, c_hit_me_card)
#
#             # here we flip both users cards up and show
#             print(f"Your final hand: {p_cards}, final score: {p_current_score}")
#             print(f"Computer's final hand: {c_cards} is {c_current_score}")
#
#             # determine the winner of the game
#                 # based on the rules
#             determine_winner(p_current_score, c_current_score)
#             blackjack()
#
#     if play_game == "n":
#         # exit game
#         sys.exit()
#
#
# blackjack()


