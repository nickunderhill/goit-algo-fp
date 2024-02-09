
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
COLOR_END = '\033[0m'


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_calories = 0
    selected_items = []

    for item in sorted_items:
        if budget >= item[1]["cost"]:
            budget -= item[1]["cost"]
            total_calories += item[1]["calories"]
            selected_items.append(item[0])

    return selected_items, total_calories


def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.keys())

    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            cost = items[item_list[i-1]]["cost"]
            calories = items[item_list[i-1]]["calories"]
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]

    w = budget
    n = len(items)
    selected_items = []

    while w >= 0 and n > 0:
        if dp[n][w] != dp[n-1][w]:
            selected_items.append(item_list[n-1])
            w -= items[item_list[n-1]]["cost"]
        n -= 1

    return selected_items[::-1], dp[len(items)][budget]


def print_result(alg_name, result, budget):
    print(GREEN, alg_name, "алгоритм обрав наступні продукти: на суму",
          budget,  COLOR_END)
    for item in result[0]:
        print(YELLOW, item, COLOR_END)
    print(YELLOW, "Всього калорій:", COLOR_END, RED, result[1], COLOR_END)


budget = 100
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
print("\n")
greedy_result = greedy_algorithm(items, budget)
print_result("Жадібний", greedy_result, budget)
print("\n")
dynamic_result = dynamic_programming(items, budget)
print_result("Динамінчий", dynamic_result, budget)
print("\n")
