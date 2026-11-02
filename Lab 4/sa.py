import math
import random
def cost(state):
    attacks = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks
def simulated_annealing():
    current = [random.randint(0, 7) for _ in range(8)]
    T = 100.0  
    while T > 0.001 and cost(current) > 0:
        neighbour = list(current)
        col = random.randint(0, 7)
        neighbour[col] = random.randint(0, 7)
        delta_E = cost(current) - cost(neighbour)
        if delta_E > 0 or random.random() < math.exp(delta_E / T):
            current = neighbour
        T *= 0.99
    return current
solution = simulated_annealing()
print("Queen positions (row per column):", solution)
print("Attacking pairs left:", cost(solution))
