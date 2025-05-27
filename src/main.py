import random


def generation(diff_range):
    # numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # secret_code = random.choices(numbers, k=4)
    # # return [int(x) for x in secret_code]

    if diff_range == 5:
        numbers = ["0", "1", "2", "3", "4", "5"]
        secret_code = random.choices(numbers, k=4)
        return [int(x) for x in secret_code]
    if diff_range == 7:
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7"]
        secret_code = random.choices(numbers, k=4)
        return [int(x) for x in secret_code]
    if diff_range == 9:
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        secret_code = random.choices(numbers, k=4)
        return [int(x) for x in secret_code]


def detection(secret_code):
    print(f"{secret_code}")
    attempts = 10
    for num in range(1, 11):
        # for invalid attempts
        while True:
            # this is like a trial and error block which basically tells like try all the method and if hits the error go to except
            # it also has stuff like else and finally
            # except is just a nice way to show the error instead of those 100 lines of random code so the user doesnt feel like something big happened
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
        white_pegs = 0

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

        # g_rem_copy = guess_rem #this does not copy the list
        # instead of this, in python there is a inbuilt function named .copy()
        # or use g_rem_copy = list(guess_rem)
        # or use the SLICING METHOD which is the fasted and the most useful that is g_rem_copy = guess_rem[:]

        g_rem_copy = list(guess_rem)
        secret_code_rem_copy = list(secret_code_rem)

        # for white pegs
        # for white pegs we will only use the used list as there can be a crossover of elements

        # for i in range(
        #     len(g_rem_copy)  # this does not work as you are modifying the same list
        # ):
        #     for j in range(len(secret_code_rem_copy)):
        #         if guess_rem[i] == secret_code_rem[j]:
        #             white_pegs += 1
        #             guess_rem.remove(guess_rem[i])
        #             secret_code_rem.remove(secret_code_rem[j])

        for i in range(len(g_rem_copy)):
            for j in range(len(secret_code_rem_copy)):
                if g_rem_copy[i] == secret_code_rem_copy[j]:
                    white_pegs += 1
                    g_rem_copy[i] = None
                    secret_code_rem_copy[j] = None
                    break

        print(f"{red_pegs} R , {white_pegs} W")

        if red_pegs == 4:
            print("You Guessed the code.")
        elif num == attempts:
            print("Attempts over.")
            print(f"Secret code was {secret_code}")


def board():
    # ┌ ┬ ┬ ┐ ─
    print("┌─────┬───┬───┬───┬───┐")

    # ─ ┤ ├ ┼
    for x in range(0, 10):
        print("│     │   │   │   │   │")
        print("│     │   │   │   │   │")

        print("├─────┼───┼───┼───┼───┤")

    # └ ┴ ┘ ─

    print("│     │   │   │   │   │")
    print("│     │   │   │   │   │")
    print("└─────┴───┴───┴───┴───┘")

def menu():
    print("Welcome to MasterMind.")
    print("Choose your difficulty.")
    print("1. Easy(0-5)")
    print("2. Medium(0-7)")
    print("3. Hard(0-9)")
    diff_range = 0
    while True:  # match case will only work if you have python 3.10+
        # suggested to use if else for wider compatibility
        choice = input("Enter your Choice: ")
        match choice:
            case "1":
                diff_range = 5
                break
            case "2":
                diff_range = 7
                break
            case "3":
                diff_range = 9
                break
            case _:
                print("Enter from 1, 2, 3 only")

    secret_code = generation(diff_range)
    detection(secret_code)


if __name__ == "__main__":
    menu()
