def bfs(start, goal):
    queue = [start]
    visited = set()
    while queue:
        state = queue.pop(0)
        if state == goal:
            return "Success"
        if state not in visited:
            visited.add(state)
            zero = state.index(0)
            row = zero // 3
            col = zero % 3
            moves = []
            if row > 0:
                moves.append("UP")
            if row < 2:
                moves.append("DOWN")
            if col > 0:
                moves.append("LEFT")
            if col < 2:
                moves.append("RIGHT")
            for move in moves:
                new_state = list(state)
                if move == "UP":
                    new_zero = zero - 3
                elif move == "DOWN":
                    new_zero = zero + 3
                elif move == "LEFT":
                    new_zero = zero - 1
                else:
                    new_zero = zero + 1
                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]
                new_state = tuple(new_state)
                if new_state not in visited:
                    queue.append(new_state)
    return None
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
solution = bfs(start, goal)
print("Solution:", solution)
