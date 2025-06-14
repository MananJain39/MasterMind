import random


def generation(diff_range):
    return random.choices(range(1, diff_range + 1), k=4)


def detection(secret_code):
    attempts = 10
    history = []
    if_guessed = False
    for num in range(1, 11):
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
        white_pegs = 0
        guess_rem = []
        secret_code_rem = []

        for i in range(0, 4):
            if guess[i] == secret_code[i]:
                red_pegs += 1
            else:
                guess_rem.append(guess[i])
                secret_code_rem.append(secret_code[i])

        for i in range(len(guess_rem)):
            for j in range(len(secret_code_rem)):
                if guess_rem[i] == secret_code_rem[j]:
                    white_pegs += 1
                    guess_rem[i] = None
                    secret_code_rem[j] = None
                    break

        if red_pegs == 4:
            if_guessed = True

        history.append((guess, red_pegs, white_pegs))
        board(history, secret_code, if_guessed)

        if if_guessed:
            print("Congrats! You have guessed the code.")
            return
        elif num == attempts:
            print("Attempts over.")
            print(f"Secret code was {secret_code}")


def board(history, secret_code, if_guessed):
    print("┌─────┬───┬───┬───┬───┬───┬───┐")
    if if_guessed:
        print(
            f"│ CODE│ {secret_code[0]} │ {secret_code[1]} │ {secret_code[2]} │ {secret_code[3]} │ R │ W │ "
        )
    else:
        print("│ CODE│ X │ X │ X │ X │ R │ W │")
    for guess, red, white in history:
        print("├─────┼───┼───┼───┼───┼───┼───┤")

        print(
            f"│     │ {guess[0]} │ {guess[1]} │ {guess[2]} │ {guess[3]} │ {red} │ {white} │ "
        )
    print("└─────┴───┴───┴───┴───┴───┴───┘")


def menu():
    print("Welcome to MasterMind.")
    print("Choose your difficulty.")
    print("1. Easy(0-5)")
    print("2. Medium(0-7)")
    print("3. Hard(0-9)")
    diff_range = 0
    while True:
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
