class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        
        cur_row, cur_col = rStart, cStart
        row_dir, col_dir = 0, 1
        cur_len = 0
        
        while len(res) < rows*cols:
            for i in range(cur_len//2 + 1):
                if 0 <= cur_row < rows and 0 <= cur_col < cols:
                    res.append((cur_row, cur_col))
                    
                cur_row += row_dir
                cur_col += col_dir
                
            row_dir, col_dir = col_dir, -row_dir
            cur_len += 1
            
            
        return res
       
    
    
    
    
    
    