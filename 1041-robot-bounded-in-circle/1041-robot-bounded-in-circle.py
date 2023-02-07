class Solution:
    def isRobotBounded(self, instructions: str) -> bool:  
        x_move, y_move, direction, flag = self.move(instructions)
        if not(x_move or y_move) or direction != "N":
            return True
        return False
    
    def move(self, instructions):
        x_move = 0
        y_move = 0
        directions = ["N", "W", "S", "E"]
        direction = "N"
        dir_idx = 0
        flag = 0
        
        for inst in instructions:
            if inst == "G":
                if direction == "N":
                    y_move += 1
                elif direction == "S":
                    y_move -= 1
                elif direction == "E":
                    x_move += 1
                else:
                    x_move -= 1
            else:
                if inst == "L":
                    dir_idx += 1
                    dir_idx %= 4
                else:
                    if not dir_idx:
                        dir_idx = 3
                    else:
                        dir_idx -= 1
                direction = directions[dir_idx]
                
        return [x_move, y_move, direction, flag]
                