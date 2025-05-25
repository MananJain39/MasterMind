import random


def generation():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "9"]
    secret_code = random.sample(numbers, 4)
    return [int(x) for x in secret_code]


def detection():
    secret_code = generation()
    attempts = 10
    for num in range(1, 11):
        # for invalid attempts
        while True:
            try:

                guess = [
                    int(x)
                    for x in input("Enter your guess, (space generated): ").split()
                ]
                if len(guess) != 4 or not all(0 <= x <= 9 for x in guess):
                    print("Invalid attempt. Make sure there is space.")
                    continue
                break
            except ValueError:
                print("Enter numbers only.")
                continue

        red_pegs = 0

        guess_rem = (
            []
        )  # this is basically a empty list which we will use to store the un-used elements of guess
        secret_code_rem = []  # same as above

        # calculate the number of red pegs
        for i in range(0, 4):
            if (
                guess[i] == secret_code[i]
            ):  # check if the guess is matching the secret code or not
                red_pegs += 1
                # print( str(i) + "red peg")

            else:
                guess_rem.append(
                    guess[i]
                )  # this adds the unused element to the empty list we created
                secret_code_rem.append(secret_code[i])  # this is same as above

        print(f"{red_pegs} R")

        if red_pegs == 4:
            print("You Guessed the code.")
        elif num == attempts:
            print("Attempts over.")


detection()
