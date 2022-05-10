class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        def calc(x, n):
            
            if n == 1:
                return x
            temp = calc(x, n//2)
            
            return temp * temp * (x if n % 2 else 1)
        temp = calc(x, abs(n))
        if n < 0:
            return 1/ temp
        return temp
