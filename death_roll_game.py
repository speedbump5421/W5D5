import random
import time

print("")
print("*" * 47)
print("*** ☠️ Hello and Welcome to The Death Roll ☠️ ***")
print("*" * 47)
print("")
print("")
print("*" * 38)
print("*** Here are the rules to the game ***")
print("*" * 38)
print("")
print("*" * 68)
# print("This game requires two players.")
print("Player one will select the amount to bet.")
print("This amount can be any number from 10 and above.")
print("Then Player one will roll from 1 - the number they selected")
print("Next Player two will roll from 1 - the number Player one just rolled")
print("Plyers will continue back and forth until one Player rolls a 1")
print("The player that rolls a 1 loses.")
print("*" * 68)
print("")

while True:

    play = input("Would you like to play? y or n?")
    if play == "y" or play == "Y":
        print("Awesome, let play!")
        break
    if play == "n" or play == "N":
        print("To bad, this could have been fun.")
        print("")
    else:
        print("Pelase select Y or N")


while True:
    bet = input("Player One, how much would you like to bet? ")
    try:
        bet = int(bet)
        if bet < 10:
            print("Sorry, try again with a higher bet. It needs to be 10 or higher.")
        else:
            print("")
            print("*" * 35)
            print("   You have bet", bet, "good luck!")
            print("*" * 35)
            print("")
            break  # Exit the loop once a valid bet is entered
    except ValueError:
        print("Invalid input. Please enter a number.")


while True:

    p1 = random.randint(1, bet)
    print("Player One rolled a", p1)
    print("")

    time.sleep(2)

    if p1 == 1:
        print("*" * 55)
        print(" Player One rolled a 1 that means player One has lost.\n             The winner is Player Two!")
        print("*" * 55)
        break

    bet = p1

    p2 = random.randint(1, p1)
    print("Player Two rolled a", p2)
    print("")

    time.sleep(2)

    if p2 == 1:
        print("*" * 55)
        print(" Player Two has rolled a 1 that means player Two lost.\n             The winner is Player One!")
        print("*" * 55)
        break
    bet = p2
