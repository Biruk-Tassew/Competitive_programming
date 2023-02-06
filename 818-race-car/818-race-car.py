class Solution:
    def racecar(self, target: int) -> int:
        
        level = 0
        que = deque([(0, 1)])
        while que:
            for _ in range(len(que)):
                
                cur_pos, cur_speed = que.popleft()
                
                if cur_pos == target:
                    return level
                
                a_pos = cur_pos + cur_speed
                a_speed = cur_speed * 2 
                que.append((a_pos, a_speed))
                
                if (a_pos > target and a_speed > 0) or (a_pos < target and a_speed < 0):
                    r_speed = 1
                    if cur_speed >= 0:
                        r_speed = -1
                        
                    que.append((cur_pos, r_speed))
                
            level += 1