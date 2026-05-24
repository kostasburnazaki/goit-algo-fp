import random
import pandas as pd
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(num_rolls=100000):
    # Підрахунок частоти кожної суми від 2 до 12
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sum_counts[total] += 1
        
    # Розрахунок ймовірностей у відсотках
    mc_probabilities = {k: (v / num_rolls) * 100 for k, v in sum_counts.items()}
    return mc_probabilities

# Аналітичні ймовірності математичного розрахунку
analytical_probabilities = {
    2: 1/36*100, 3: 2/36*100, 4: 3/36*100, 5: 4/36*100, 6: 5/36*100,
    7: 6/36*100, 8: 5/36*100, 9: 4/36*100, 10: 3/36*100, 11: 2/36*100, 12: 1/36*100
}

# Демонстрація
def main():
    print("\n--- Завдання 7 (Метод Монте-Карло) ---")
    rolls = 100000
    mc_results = monte_carlo_dice_simulation(rolls)

    # Формування порівняльної таблиці через Pandas
    df = pd.DataFrame({
        "Сума": list(mc_results.keys()),
        "Монте-Карло (%)": [round(v, 2) for v in mc_results.values()],
        "Аналітична (%)": [round(analytical_probabilities[k], 2) for k in mc_results.keys()]
    })
    print(df.to_string(index=False))

    # Побудова графіка порівняння
    plt.figure(figsize=(10, 5))
    plt.plot(df["Сума"], df["Монте-Карло (%)"], 'ro-', label=f'Монте-Карло ({rolls} кидків)')
    plt.plot(df["Сума"], df["Аналітична (%)"], 'bx--', label='Аналітичний розрахунок')
    plt.xlabel('Сума очок')
    plt.ylabel('Ймовірність (%)')
    plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()