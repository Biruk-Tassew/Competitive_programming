class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a = Counter(s)["a"]
        count_b = 0
        
        min_del = count_a
        for i in s:
            if i == "a":
                count_a -= 1
            if i == "b":
                count_b += 1
                
            min_del = min(min_del, count_a+count_b)
            
        return min_del
                