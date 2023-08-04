def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n  # Keep track of visited boxes
    stack = [0]  # Start with box 0 (which is unlocked)

    while stack:
        box = stack.pop()
        visited[box] = True

        for key in boxes[box]:
            if not visited[key]:
                stack.append(key)

    return all(visited)
