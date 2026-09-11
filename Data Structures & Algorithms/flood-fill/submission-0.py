class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        visited = deepcopy(image)
        rows = len(visited)
        cols = len(visited[0])
        initial_color = visited[sr][sc]
        queue= deque()
        queue.append((sr,sc))
        while len(queue) != 0:
            i,j = queue.popleft()
            visited[i][j]=color
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i=i+x
                new_j=j+y
                if new_i<0 or new_i >= (rows) or new_j<0 or new_j>=cols:
                    continue
                if visited[new_i][new_j] != initial_color:
                    continue
                queue.append((new_i,new_j))
        return visited
        