
name = input("Welcome to GC mini golf! What is your name? ")
holes_to_play = int(input(f"Hi, {name}! Would you like to play 3 or 6 holes? "))

total_putts = 0

for hole in range(1, holes_to_play + 1):

    putts = int(input(f"How many putts for hole {hole}? (par:3) "))


    total_putts += putts


total_par = holes_to_play * 3


score_vs_par = total_putts - total_par

if score_vs_par > 0:
        print(f"Nice try, {name}... Your total score was: +{score_vs_par}.")
elif score_vs_par < 0:
        print(f"Great job, {name}! Your total score was: {score_vs_par}.")
else:
        print(f"Good game, {name}. Your total score was: {score_vs_par}.")





