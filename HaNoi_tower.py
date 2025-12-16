from typing import List, Tuple

A, B, C = 0, 1, 2
PEG_NAMES = {0: 'A', 1: 'B', 2: 'C'}

State = Tuple[int, ...]


def get_top_disks(state: State, n: int):
    top = {A: None, B: None, C: None}
    for disk in range(n):
        peg = state[disk]
        if top[peg] is None:
            top[peg] = disk
    return top


def get_successors(state: State, n: int):
    successors = []
    top = get_top_disks(state, n)

    for src in [A, B, C]:
        if top[src] is None:
            continue

        disk = top[src]
        for dst in [A, B, C]:
            if src == dst:
                continue

            if top[dst] is None or disk < top[dst]:
                new_state = list(state)
                new_state[disk] = dst
                successors.append(
                    (tuple(new_state),
                     f"Move disk {disk + 1} from {PEG_NAMES[src]} to {PEG_NAMES[dst]}.")
                )

    return successors


def dls(state: State, goal: State, n: int, depth: int, path, visited):
    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(state)

    for next_state, action in get_successors(state, n):
        if next_state not in visited:
            result = dls(next_state, goal, n, depth - 1,
                         path + [action], visited)
            if result is not None:
                return result

    visited.remove(state)
    return None


def iddfs(n: int) -> List[str]:
    start = tuple([A] * n)
    goal = tuple([C] * n)

    depth = 0
    while True:
        visited = set()
        result = dls(start, goal, n, depth, [], visited)
        if result is not None:
            return result
        depth += 1


# ===== MAIN =====
if __name__ == "__main__":
    n = int(input().strip())
    moves = iddfs(n)
    for move in moves:
        print(move)
