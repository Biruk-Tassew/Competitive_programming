class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
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
               
