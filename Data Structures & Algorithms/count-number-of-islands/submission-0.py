class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        col = len(grid[0])

        visited = [[0 for _ in range(col)] for _ in range(rows)]

        no_of_island = 0

        def dfs(r, c):

            # Out of grid
            if r < 0 or r >= rows or c < 0 or c >= col:
                return

            # Water or already visited
            if visited[r][c] == 1 or grid[r][c] == "0":
                return

            # Mark visited
            visited[r][c] = 1

            # Up
            dfs(r - 1, c)

            # Down
            dfs(r + 1, c)

            # Left
            dfs(r, c - 1)

            # Right
            dfs(r, c + 1)

        # Visit every cell
        for r in range(rows):
            for c in range(col):

                # Found a new island
                if visited[r][c] == 0 and grid[r][c] == "1":

                    no_of_island += 1

                    # Explore entire island
                    dfs(r, c)

        return no_of_island