import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_choice = []
computer_choice = []
for number in range(0, 2):
    card_chosen = random.choice(cards)

    your_choice.append(card_chosen)
    computer_choice.append(card_chosen)

your_score = your_choice[0] + your_choice[1]
computer_score = computer_choice[0] + your_choice[1]

print(computer_choice[0])
print(f"your cards is :{your_choice} and your score is :{your_score}")

# print ("hit ", "stand")

draw_card = input("if you want an extra card type 'hit' type 'stand' to stop: ")

while draw_card == "hit" and your_score <21:
  extra_card = random.choice(cards)
  your_choice.append(extra_card)
  your_score += extra_card
  print(f"your cards is :{your_choice} and your score is :{your_score}")
  if your_score > 21:
      print("you bust")
  else:
      draw_card = input("if you want an extra card type 'hit' type'stand' to stop: ")

# if draw_card == "stand":
#     print(f"computer cards is :{computer_choice} and your score is :{computer_score}")

