class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: # DFS
        
        if (image[sr][sc] == color):
            return image
        
        start_color = image[sr][sc]
        stack = [(sr, sc)]
        
        while stack:
            row, col = stack.pop()
            image[row][col] = color
            
            if row+1 >= 0 and row+1 < len(image) and image[row+1][col]==start_color:
                stack.append((row+1, col))
            if col+1 >= 0 and col+1 < len(image[0]) and image[row][col+1]==start_color:
                stack.append((row, col+1))
            if row-1 >= 0 and row-1 < len(image) and image[row-1][col]==start_color:
                stack.append((row-1, col))  
            if col-1 >= 0 and col-1 < len(image[0]) and image[row][col-1]==start_color:
                stack.append((row, col-1))
                
        return image
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: # BFS
        
        if image[sr][sc]==color:
            return image
        
        starting_color = image[sr][sc]
        queue = deque([(sr,sc)])
        
        while queue:
            row, col = queue.popleft()
            image[row][col] = color

            if 0 <= row+1 < len(image) and image[row+1][col] == starting_color:
                queue.append((row+1, col))
            if 0 <= row-1 < len(image) and image[row-1][col] ==starting_color:
                queue.append((row-1, col))
            if 0 <= col+1 < len(image[0]) and image[row][col+1] == starting_color:
                queue.append((row, col+1))
            if 0 <= col-1 < len(image[0]) and image[row][col-1] == starting_color:
                queue.append((row, col-1))

        return image
           
               
