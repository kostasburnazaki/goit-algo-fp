items = {
    "pizza": {"cost": 50, "calories": 300},
    "burger": {"cost": 20, "calories": 150},
    "cola": {"cost": 15, "calories": 90},
    "salad": {"cost": 25, "calories": 120},
    "fries": {"cost": 30, "calories": 200}
}

# 1. Жадібний алгоритм (Максимізація Калорії / Вартість)
def greedy_algorithm(menu, budget):
    # Сортуємо страви за питомою калорійністю на 1 грошову одиницю
    sorted_items = sorted(menu.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for name, info in sorted_items:
        if budget >= info["cost"]:
            budget -= info["cost"]
            total_calories += info["calories"]
            selected_items.append(name)
            
    return selected_items, total_calories

# 2. Динамічне програмування (Класичний 0/1 Рюкзак)
def dynamic_programming(menu, budget):
    item_list = list(menu.items())
    n = len(item_list)
    
    # Таблиця DP: рядки — предмети, стовпчики — проміжний бюджет від 0 до budget
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, info = item_list[i-1]
        cost = info["cost"]
        calories = info["calories"]
        
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b - cost] + calories)
            else:
                dp[i][b] = dp[i-1][b]
                
    # Відновлення обраного набору страв
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i-1][b]:
            name, info = item_list[i-1]
            selected_items.append(name)
            b -= info["cost"]
            
    return selected_items[::-1], dp[n][budget]

# Демонстрація
def main():
    print("\n--- Завдання 6 (Оптимізація меню) ---")
    test_budget = 60
    print(f"Бюджет: {test_budget}")

    greedy_res, greedy_cal = greedy_algorithm(items, test_budget)
    print(f"[Жадібний підхід]: Обрано страви {greedy_res} | Загальна калорійність: {greedy_cal}")

    dp_res, dp_cal = dynamic_programming(items, test_budget)
    print(f"[Динамічне програмування]: Обрано страви {dp_res} | Загальна калорійність: {dp_cal}")


if __name__ == "__main__":
    main()