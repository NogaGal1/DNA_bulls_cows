import random


def create_quartet():
    #Creates a random DNA sequence of four nucleotides
    letters = "ACTG"
    quartet = ""

    for i in range(4):
        quartet += random.choice(letters)

    return quartet


def find_bulls(rand_str, guessed_str):
    #Finds the number of Bulls and creates two substrings:
    #sub_rand - characters from the random string that were not Bulls.
    #sub_guessed - characters from the guessed string that were not Bulls.
    bulls = 0
    sub_rand = ""
    sub_guessed = ""

    for i in range(4):
        if rand_str[i] == guessed_str[i]:
            bulls += 1
        else:
            sub_rand += rand_str[i]
            sub_guessed += guessed_str[i]

    return bulls, sub_rand, sub_guessed


def find_cows(sub_rand, sub_guessed):
    #Counts the number of correct letters in incorrect positions
    cows = 0

    for letter in sub_guessed:
        if letter in sub_rand:
            cows += 1
            position = sub_rand.index(letter)
            sub_rand = sub_rand[:position] + sub_rand[position + 1:]

    return cows


###main###

rand_str = create_quartet()
attempts = 0
guessed_str = ""

results_file = open("results/results.txt", "w")

while guessed_str != rand_str:

    guessed_str = input(
        "Please try to guess a four DNA combination composed from A,T,C,G ? "
    ).upper()

    attempts += 1

    bulls, sub_rand, sub_guessed = find_bulls(rand_str, guessed_str)
    cows = find_cows(sub_rand, sub_guessed)

    print("Bulls=" + str(bulls))
    print("Cows=" + str(cows))

    results_file.write("Guess: " + guessed_str + "\n")
    results_file.write("Bulls=" + str(bulls) + "\n")
    results_file.write("Cows=" + str(cows) + "\n\n")

results_file.write(
    "You guessed after " + str(attempts) + " attempts\n")

print("You guessed after " + str(attempts) + " attempts")

results_file.close()