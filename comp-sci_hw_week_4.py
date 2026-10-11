import random   

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']
    return random.choice(cards)

def calculate_score(hand):
    score = 0
    ace_count = 0

    for card in hand:
        if card in ['J', 'K', 'Q']:
            score += 10
        elif card == 'A':
            ace_count += 1
            score += 11
        else:
            score += card
            
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
        
    return score

def play_blackjack():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print("Your hand: ", player_hand, "current score: ", player_score)
        print("Dealer's first card: ", dealer_hand[0])

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'h' to hit (get another card), type 'p' to pass: ")
            if should_continue == 'h':
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score < 17 and dealer_score != 21:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print("Your final hand: ", player_hand, "final score: ", player_score)
    print("Dealer's final hand: ", dealer_hand, "final score: ", dealer_score)

    if player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score == 21:
        return "Blackjack! You win!"
    elif dealer_score == 21:
        return "Dealer has Blackjack! You lose!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"
    
print(play_blackjack())
