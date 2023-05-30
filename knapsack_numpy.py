import numpy as np
class Knapsack_Challange_Edition:
    def __init__(self, values, weights, capacity, stock) -> None:
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.stock = stock
    
    def run(self):
        n = len(self.values)
        K = np.zeros((n + 1, self.capacity + 1), dtype=np.int32)

        for i in range(1, n + 1):
            for j in range(1, self.capacity + 1):
                max_value = 0
                for k in range(min(self.stock[i - 1], j // self.weights[i - 1]) + 1):
                    max_value = max(max_value, self.values[i - 1] * k + K[i - 1, j - self.weights[i - 1] * k])
                K[i, j] = max_value

        selected_items = []
        total_value = K[n, self.capacity]

        j = self.capacity
        for i in range(n, 0, -1):
            for k in range(min(self.stock[i - 1], j // self.weights[i - 1]), -1, -1):
                if K[i, j] == self.values[i - 1] * k + K[i - 1, j - self.weights[i - 1] * k]:
                    for _ in range(k):
                        selected_items.append(i - 1)
                    j -= self.weights[i - 1] * k
                    break

        return selected_items[::-1], total_value

buah = ('Apel', 'Jeruk', 'Pisang', 'Kiwi', 'Mangga')
calories = [91, 71, 105, 103, 96]
price = [2_360, 2_120, 1_890, 3_770, 2_870]
fund = 25_000
stock = [3, 3, 5, 10, 5]

challange = Knapsack_Challange_Edition(calories, price, fund, stock)
selected, total_calories = challange.run()
# print("Buah :", [buah[x] for x in selected])
# print("Total Calories:", total_calories)
# print("Pengeluaran:", sum([price[x] for x in selected]))

print(total_calories)