import numpy as np
import random

GREEN = '\033[32m'
COLOR_END = '\033[0m'


def monte_carlo_dice_throw(num_throws=10000):

    outcomes = {i: 0 for i in range(2, 13)}

    for _ in range(num_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        outcomes[total] += 1

    probabilities = {sum_value: count /
                     num_throws for sum_value, count in outcomes.items()}

    return probabilities


def print_results(given, experiment):
    header = f"| {'Сума':<20} | {'Ймовірність':<15} | {'Монте-Крало':<15} | {'Різниця':<15} |"
    separator = "| " + "-"*20 + " | " + "-" * \
        15 + " | " + "-"*15 + " | " + "-"*15 + " |"
    row_template = "| {sum:<20} | {prob:^15.4f} | {mt:^15.4f} | {diff:^15.4f} |"

    print(header)
    print(separator)
    for key, value in given.items():
        exp_value = experiment[key] * 100
        diff = value - exp_value
        print(row_template.format(sum=key, prob=value, mt=exp_value, diff=diff))


# Ймовірності з умов завдання
given_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}
# Ймовірності з експерименту Монте-Карло
num_experiments = 1000000
mt_probabilities = monte_carlo_dice_throw(num_experiments)
print(f'{GREEN}Порівняльна таблиця ймовірностей випадіння суми кубиків на \nоснові {num_experiments} еспериментів:{COLOR_END}')
print_results(given_probabilities, mt_probabilities)
