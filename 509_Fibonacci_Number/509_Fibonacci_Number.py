class Solution:
    def fib(self, n: int) -> int:
        def calcFib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return calcFib(n-1) + calcFib(n-2)
            
        return calcFib(n)
        
