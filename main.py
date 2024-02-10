import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_choice = []
computer_choice = []

for number in range(0, 2):
    your_choice.append(random.choice(cards))
    computer_choice.append(random.choice(cards))


def calculate_score(choice):
    score = sum(choice)
    if 11 in choice and score > 21:
        choice.remove(11)
        choice.append(1)
        score -= 10
    return score

your_score = calculate_score(your_choice)
computer_score = calculate_score(computer_choice)

print(f"one of computer card: {computer_choice[0]}")
print(f"your cards is: {your_choice} and your score is: {your_score}")

# print ("hit ", "stand")

while your_score < 21:
    draw_card = input("If you want an extra card, type 'hit'. Type 'stand' to stop: ")
    if draw_card == "hit":
        extra_card = random.choice(cards)
        your_choice.append(extra_card)
        your_score += extra_card
        print(f"Your cards are: {your_choice} and your score is: {your_score}")
        if your_score > 21:
            print("You bust!")
            break
    else:
        break

# Computer's turn
while computer_score < 17:
    extra_card_computer = random.choice(cards)
    computer_choice.append(extra_card_computer)
    computer_score += extra_card_computer


print(f"Your final score: {your_score}, Computer's final score: {computer_score}")


# Determine the winner
if your_score > 21:
    print("You bust! You lose.")
elif computer_score > 21 or your_score > computer_score:
    print("You win!")
elif computer_score > your_score:
    print("Computer wins!")
else:
    print("It's a tie.")


# should_continue = True
# while should_continue:
#     if computer_score < 17:
#         extra_card_computer = random.choice(cards)
#         computer_choice.append(extra_card_computer)
#         computer_score += extra_card_computer
#         print(
#             f"computer cards is :{computer_choice} and the score is :{computer_score}"
#         )
#         if computer_score > 21:
#             print("you win")
#             should_continue = False
#         elif your_score < computer_score:
#             print("you lose")
#             should_continue = False
#     if computer_score >= 17 and your_score > computer_score:
#         print("you win")
#         should_continue = False
