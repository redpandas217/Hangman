import random
words = ["Ryan Reynolds", "Watermelon", "Cookie Dough Ice Cream", "Golden Retriever", "Milky Way", "Biomedical Engineering", "Abby is a Band Kid", "Mia is a Nerd"]
answer = random.choice(words)
answerlower = answer.lower()
spaceless = answerlower.split(" ")
print("Hi, Jerry needs your help and will die if you are unable to save him. Guess letters in order to save Jerry!")
print("   ( )   ")
print("  / | /         <-- This is Jerry ")
print("    |   ")
print("   | |")
for word in spaceless:
    letters = sum(char.isalpha() for char in word)
    i = 0
    while i < letters:
        print("_", end=" ")
        i = i + 1
    print(" ", end="     ")
tallies = 0
choice_list = []
answer_not_correct = True
while tallies < 6 and answer_not_correct:
    choice = input("Choose a letter or guess the phrase:")
    choicelower = choice.lower()
    choice_list.append(choicelower)
    if sum(char.isalpha() for char in choicelower) == 0:
        print("You Are Bad at Directions")
    elif sum(char.isalpha() for char in choicelower) > 1:
        if (choicelower == answerlower):
            print("Correct! YOU SAVED JERRY #GirlBoss")
            answer_not_correct = False
        elif (choicelower != answerlower and tallies == 5):
            print("Game Over, You Have Failed to Save Jerry")
        else:
            print("Wrong Answer")
            tallies = tallies + 1
            if tallies == 1:
                print("   ( )   ")
                print("   ")
                print("       ")
                print("     ")
            if tallies == 2:
                print("   ( )   ")
                print("    |  ")
                print("    |   ")
                print("      ")
            if tallies == 3:
                print("   ( )   ")
                print("    | / ")
                print("    |   ")
                print("      ")
            if tallies == 4:
                print("   ( )   ")
                print("  / | / ")
                print("    |   ")
                print("      ")
            if tallies == 5:
                print("   ( )   ")
                print("  / | / ")
                print("    |   ")
                print("   | |  ")
            print("You Have " + str(tallies) + " Tallies out of 6")
    elif sum(char.isalpha() for char in choicelower) == 1:
        if choicelower in answerlower:
            print("Correct! #GirlBoss")
            i = 0
            for word in spaceless:
                letters = sum(char.isalpha() for char in word)
                while i < letters:
                    if word[i] in choice_list:
                        print(word[i], end=" ")
                        i = i + 1
                    elif word[i] != choicelower:
                        print("_", end=" ")
                        i = i + 1
                i = 0
                print(" ", end="     ")
        else:
            print("Wrong Answer")
            tallies = tallies + 1
            if tallies == 1:
                print("   ( )   ")
                print("   ")
                print("       ")
                print("     ")
            if tallies == 2:
                print("   ( )   ")
                print("    |  ")
                print("    |   ")
                print("      ")
            if tallies == 3:
                print("   ( )   ")
                print("    | / ")
                print("    |   ")
                print("      ")
            if tallies == 4:
                print("   ( )   ")
                print("  / | / ")
                print("    |   ")
                print("      ")
            if tallies == 5:
                print("   ( )   ")
                print("  / | / ")
                print("    |   ")
                print("   | |  ")
            print("You Have " + str(tallies) + " Tallies out of 6")
