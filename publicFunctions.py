def availableActions(self, state):
    row, col = state
    candidates = [
        ("up", (row - 1, col)),
        ("down", (row + 1, col)),
        ("left", (row, col - 1)),
        ("right", (row, col + 1))
    ]
    result = []
    for action, (r, c) in candidates:
        if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
            result.append((action, (r, c)))
    return result

def heu(self, node):
    (r1, c1) = node
    (r2, c2) = self.goal
    return abs(r2 - r1) + abs (c2 - c1)