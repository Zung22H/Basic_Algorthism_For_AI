# Monkey and Banana Problem using DFS

# State: (monkey_position, box_position, monkey_height)

INITIAL_STATE = ("middle", "window", "floor")
GOAL_POSITION = "center"

visited = set()

def is_goal(state):
    monkey_pos, box_pos, height = state
    return monkey_pos == GOAL_POSITION and box_pos == GOAL_POSITION and height == "on_box"

def get_actions(state):
    monkey_pos, box_pos, height = state
    actions = []

    # Move
    if height == "floor":
        for pos in ["center","window", "middle"]:
            if pos != monkey_pos:
                actions.append(("Move to " + pos, (pos, box_pos, height)))

    # Push box
    if height == "floor" and monkey_pos == box_pos:
        for pos in ["center","window", "middle"]:
            if pos != box_pos:
                actions.append(("Push box to " + pos, (pos, pos, height)))

    # Climb box
    if height == "floor" and monkey_pos == box_pos:
        actions.append(("Climb box", (monkey_pos, box_pos, "on_box")))

    # Get banana
    if height == "on_box" and box_pos == GOAL_POSITION:
        actions.append(("Get banana", state))

    return actions

def dfs(state, path):
    if state in visited:
        return None

    visited.add(state)

    if is_goal(state):
        return path + ["Get banana"]

    for action, next_state in get_actions(state):
        result = dfs(next_state, path + [action])
        if result:
            return result

    return None

# Run DFS
solution = dfs(INITIAL_STATE, [])

# Output result
for step in solution:
    print(step)
