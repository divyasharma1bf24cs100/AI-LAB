def dls(state, goal, depth, visited):
    if state == goal:
        return True
    if depth == 0:
        return False
    visited.add(state)  
    zero = state.index(0)
    row, col = zero // 3, zero % 3
    moves = []
    if row > 0: moves.append(zero - 3)
    if row < 2: moves.append(zero + 3)
    if col > 0: moves.append(zero - 1)
    if col < 2: moves.append(zero + 1)
    for new_zero in moves:
        new_state = list(state)
        new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
        new_state = tuple(new_state)
        if new_state not in visited:
            if dls(new_state, goal, depth - 1, visited):
                return True
    visited.remove(state) 
    return False
def ids(start, goal):
    depth = 0
    while True:
        visited = set()
        if dls(start, goal, depth, visited):
            return f"Success at depth {depth}"
        depth += 1
start = (1, 2, 3, 
        4, 0, 6, 
        7, 5, 8)
goal = (1, 2, 3, 
        4, 5, 6, 
        7, 8, 0)
print("IDS:", ids(start, goal))

