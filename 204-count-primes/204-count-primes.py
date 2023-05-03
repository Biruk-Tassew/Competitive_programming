class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        seen = set()
        count = 2
        i = 2
        while i**2 <= n:
            if i not in seen:
                for j in range(i**2, n, i):
                    if j not in seen:
                        seen.add(j)
                        count += 1
            i += 1
            
        return n - count