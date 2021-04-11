"""It is a dice game against the computer. Duration of 3 rounds, the number of points will be the number of points
    fallen on the dice minus the doubled difference between the fallen amount and the predicted amount."""


import random
from tabulate import tabulate


def roll_the_dice():
    """Function represents roll the dice."""
    dice = random.randint(1, 6)
    return dice


def count_points(fell_points, predicted_points):
    """Function counts points of users and computers rolls."""
    return fell_points - abs(fell_points - predicted_points) * 2


def print_dice(number):
    """Function takes integer number and visualize into dice."""

    one = "---------\n" \
          "|       |\n" \
          "|   #   |\n" \
          "|       |\n" \
          "---------"

    two = "---------\n" \
          "|       |\n" \
          "| #   # |\n" \
          "|       |\n" \
          "---------"

    three = "---------\n" \
            "| #     |\n" \
            "|   #   |\n" \
            "|     # |\n" \
            "---------"

    four = "---------\n" \
           "| #   # |\n" \
           "|       |\n" \
           "| #   # |\n" \
           "---------"

    five = "---------\n" \
           "| #   # |\n" \
           "|   #   |\n" \
           "| #   # |\n" \
           "---------"

    six = "---------\n" \
          "| #   # |\n" \
          "| #   # |\n" \
          "| #   # |\n" \
          "---------"

    array_of_dices = [one, two, three, four, five, six]

    print(array_of_dices[number - 1])


def results(fell_points, number, points):
    """Printing result of each roll"""
    print("On the dice fell " + str(fell_points) + " points.")
    print("Result is " + str(fell_points) + "-" + "abs(" + str(fell_points) + "-" + str(number) + ")*2: " + str(
        points) + " points")


def print_spaces():
    """Function makes 4 spaces for readability."""
    print("\n" +
          "\n" +
          "\n" +
          "\n"
          )


def current_score(users_points, computer_points):
    """Printing computer and user results"""
    print_spaces()
    end_string = " It's a draw!"

    if users_points > computer_points:
        end_string = " User is ahead by " + str(users_points - computer_points) + " points!"

    elif computer_points > users_points:
        end_string = " Computer is ahead by " + str(computer_points - users_points) + " points!"

    print("---------- Current score ---------\n" 
          " User:       " + str(users_points) + " points\n" 
          " Computer:   " + str(computer_points) + " points\n" 
          "")
    print(end_string)
    print("----------------------------------")

    print_spaces()


def start_game(number):
    """Main function. It generates full game."""

    start_header = "---          Start game           ---"
    length = len(start_header)

    predicted_points = "Predict the points number (2..12):"
    second_row_length = len(predicted_points)

    spaces = (length - second_row_length - len(str(number))) * " "
    print(predicted_points + spaces + str(number))

    first_dice = roll_the_dice()
    second_dice = roll_the_dice()

    fell_points = first_dice + second_dice

    print_dice(first_dice)
    print_dice(second_dice)

    points = count_points(fell_points, number)

    results(fell_points, number, points)

    # Computer's part
    computers_predicted = random.randint(2, 12)
    print()
    print("Computer predicted " + str(computers_predicted) + " points.")
    print("Computer rolls the dice:")

    computer_first_dice = roll_the_dice()
    computer_second_dice = roll_the_dice()

    computer_fell_points = computer_first_dice + computer_second_dice

    print_dice(computer_first_dice)
    print_dice(computer_second_dice)

    computer_points = count_points(computer_fell_points, computers_predicted)

    results(computer_fell_points, computers_predicted, computer_points)

    return number, fell_points, points, computers_predicted, computer_fell_points, computer_points


do_want_to_play = True

while do_want_to_play:
    table = []
    previous_user_result = 0
    previous_computer_result = 0
    count_of_round = 1

    while count_of_round != 4:
        number = input("ENTER THE NUMBER: ")
        if not number.isdigit():
            print("Please, enter integer numbers!")
            continue
        else:
            number = int(number)

        if number < 2 or number > 12:
            print("ENTER CORRECT NUMBERS BETWEEN 2 AND 12")
            continue

        start = "---          Start game           ---"
        if count_of_round == 1:
            print(start)
        user_predicted, user_dice, user_result, computer_predicted, computer_dice, computer_result = start_game(number)

        new_user_result = user_result + previous_user_result
        new_computer_result = computer_result + previous_computer_result

        previous_user_result = new_user_result
        previous_computer_result = new_computer_result

        current_score(new_user_result, new_computer_result)

        round_table = tabulate([[None],
                                ["-" + str(count_of_round) + "-"],
                                [None]], tablefmt="simple")

        user_table = tabulate([["Predicted:", user_predicted],
                               ["Dice:", user_dice],
                               ["Results:", user_result]], tablefmt="simple")

        computer_table = tabulate([["Predicted:", computer_predicted],
                                   ["Dice:", computer_dice],
                                   ["Results:", computer_result]], tablefmt="simple")

        row = [round_table, user_table, computer_table]
        table.append(row)

        count_of_round += 1

    table.append([tabulate([["TOTAL", " "]], tablefmt="simple"),
                  tabulate([["POINTS", previous_user_result]], tablefmt="simple"),
                  tabulate([["POINTS", previous_computer_result]], tablefmt="simple")])

    headers = ["Round", "User", "Computer"]

    table = tabulate(table, headers, tablefmt="pretty", colalign=("grid",), )
    print("---------------- Finish game --------------")
    print(table)
    print()

    if previous_user_result > previous_computer_result:
        print("User wins " + str(previous_user_result - previous_computer_result) + " points more.")
        print("Congratulation!")

    elif previous_computer_result > previous_user_result:
        print("Computer wins " + str(previous_computer_result - previous_user_result) + " points more.")

    else:
        print(" It's a draw!")

    print_spaces()
    flag = input("Do you want to play ones more? (Y/N) ")
    if flag.upper() != "Y":
        do_want_to_play = False
