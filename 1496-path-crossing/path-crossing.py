class Solution:
    def isPathCrossing(self, path: str) -> bool:
        init = [0, 0]
        visited = {(0, 0)}

        directions = {
            'E': (1, 0),
            'W': (-1, 0),
            'N': (0, 1),
            'S': (0, -1)
        }

        for ch in path:
            dx, dy = directions[ch]
            init[0] += dx
            init[1] += dy

            if tuple(init) in visited:
                return True

            visited.add(tuple(init))

        return False
