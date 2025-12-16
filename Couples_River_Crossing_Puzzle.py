from collections import deque
from itertools import combinations

# Định danh người
PEOPLE = ["Am", "Af", "Bm", "Bf", "Cm", "Cf"]

# Các cặp vợ chồng
COUPLES = {
    "Af": "Am",
    "Bf": "Bm",
    "Cf": "Cm"
}

# Trạng thái hợp lệ theo ĐÚNG luật đề bài
def is_valid(state):
    for side in [0, 1]:
        men = {p for i, p in enumerate(PEOPLE)
               if state[i] == side and p.endswith("m")}
        women = {p for i, p in enumerate(PEOPLE)
                 if state[i] == side and p.endswith("f")}

        for w in women:
            husband = COUPLES[w]
            # Nếu có đàn ông khác mà chồng không có mặt → sai
            if any(m != husband for m in men) and husband not in men:
                return False
    return True


# Sinh các trạng thái kế tiếp
def get_next_states(state):
    boat_side = state[6]
    candidates = [i for i in range(6) if state[i] == boat_side]

    next_states = []
    for r in [1, 2]:
        for combo in combinations(candidates, r):
            new_state = list(state)
            for i in combo:
                new_state[i] = 1 - boat_side
            new_state[6] = 1 - boat_side

            if is_valid(new_state):
                move = [PEOPLE[i] for i in combo]
                next_states.append((tuple(new_state), move))
    return next_states


# BFS tìm lời giải
def bfs():
    start = (0, 0, 0, 0, 0, 0, 0)
    goal = (1, 1, 1, 1, 1, 1, 1)

    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for next_state, move in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(state, move, next_state)]))


# In kết quả
def print_solution(path):
    for state, move, next_state in path:
        direction = "R" if next_state[6] == 1 else "L"
        print(f"Move: {' '.join(move)} -> {direction}")


# MAIN
if __name__ == "__main__":
    solution = bfs()
    print_solution(solution)
