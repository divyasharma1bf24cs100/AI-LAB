def get_cost(state):
    attacks = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks
def get_successors(state):
    successors = []
    for i in range(4):
        for j in range(i + 1, 4):
            neighbor = list(state)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            successors.append(neighbor)
    return successors
def hill_climbing(initial_state):
    current = initial_state
    while True:
        best_neighbor = min(get_successors(current), key=get_cost)
        if get_cost(best_neighbor) >= get_cost(current):
            return current
        current = best_neighbor
initial_state = [3, 1, 2, 0]
solution = hill_climbing(initial_state)
print("Solution State:", solution)
print("Attacking pairs left:", get_cost(solution))
