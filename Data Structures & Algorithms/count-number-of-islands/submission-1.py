from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        no_of_island = 0

        for r in range(rows):
            for c in range(cols):

                # Found a NEW island
                if grid[r][c] == "1" and visited[r][c] == 0:

                    no_of_island += 1

                    queue = deque()
                    queue.append((r, c))
                    visited[r][c] = 1

                    while queue:

                        i, j = queue.popleft()

                        direction = [
                            (0, 1),
                            (1, 0),
                            (-1, 0),
                            (0, -1)
                        ]

                        for dr, dc in direction:

                            new_i = i + dr
                            new_j = j + dc

                            # Outside grid
                            if not (0 <= new_i < rows and 0 <= new_j < cols):
                                continue

                            # Water
                            if grid[new_i][new_j] == "0":
                                continue

                            # Already visited
                            if visited[new_i][new_j] == 1:
                                continue

                            # New land belonging to same island
                            visited[new_i][new_j] = 1
                            queue.append((new_i, new_j))

        return no_of_island
        