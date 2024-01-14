#!/usr/bin/python3
'''   A method that determines if all the boxes can be opened.
      Prototype: def canUnlockAll(boxes)
      boxes is a list of lists
      A key with the same number as a box opens that box
      You can assume all keys will be positive integers
      There can be keys that do not have boxes
      The first box boxes[0] is unlocked
      Return True if all boxes can be opened, else return False
'''


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
