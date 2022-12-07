class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        return self.solve(sorted(sums))
    def solve(self, sums):
        if len(sums)==1:
            return []
        
        num = sums[-1] - sums[-2]
        left = []
        right = []
        count = Counter(sums)
        present = False
        
        for sum_ in sums:
            cur_sum = sum_ - num
            
            if count[sum_] > 0 and count[cur_sum] > 0:
                count[sum_] -= 1
                count[cur_sum] -= 1
                left.append(cur_sum)
                right.append(sum_)
                if not cur_sum:
                    present = True
                    
        if present:
            return [num]+self.solve(left)
        else:
            return [-num]+self.solve(right)