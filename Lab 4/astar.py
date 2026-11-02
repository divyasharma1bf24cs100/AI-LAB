import heapq
INITIAL_STATE = ((2, 8, 3), (1, 6, 4), (0, 7, 5))
GOAL_STATE = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
def manhattan_distance(state):
    goal_pos = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        8: (1, 0), 0: (1, 1), 4: (1, 2),
        7: (2, 0), 6: (2, 1), 5: (2, 2)
    }
    h = 0
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                tr, tc = goal_pos[val]
                h += abs(r - tr) + abs(c - tc)
    return h
def get_neighbors(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                br, bc = r, c
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = br + dr, bc + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            grid = [list(row) for row in state]
            grid[br][bc], grid[nr][nc] = grid[nr][nc], grid[br][bc]
            neighbors.append(tuple(tuple(row) for row in grid))
    return neighbors
def a_star(start, goal):
    pq = [(manhattan_distance(start), 0, start, [start])]
    visited = {start: 0}
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal:
            return path, g
        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                new_f = new_g + manhattan_distance(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
path, cost = a_star(INITIAL_STATE, GOAL_STATE)
print(f"Total Moves / Depth (g): {cost}\n")
for step, board in enumerate(path):
    print(f"Step {step}:")
    for row in board:
        print(row)
    print()
