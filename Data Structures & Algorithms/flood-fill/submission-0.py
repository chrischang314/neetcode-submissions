class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startcolor = image[sr][sc]
        rows, cols = len(image), len(image[0])
        queue = deque([(sr, sc)])
        visited = set()
        while queue:
            for i in range(len(queue)):
                pixel = queue.popleft()
                r, c = pixel[0], pixel[1]
                visited.add(pixel)
                image[r][c] = color
                if r + 1 < rows and image[r + 1][c] == startcolor and (r + 1, c) not in visited:
                    queue.append((r + 1, c))
                if c + 1 < cols and image[r][c + 1] == startcolor and (r, c + 1) not in visited:
                    queue.append((r, c + 1))
                if r - 1 >= 0 and image[r - 1][c] == startcolor and (r - 1, c) not in visited:
                    queue.append((r - 1, c))
                if c - 1 >= 0 and image[r][c - 1] == startcolor and (r, c - 1) not in visited:
                    queue.append((r, c - 1))
        return image
