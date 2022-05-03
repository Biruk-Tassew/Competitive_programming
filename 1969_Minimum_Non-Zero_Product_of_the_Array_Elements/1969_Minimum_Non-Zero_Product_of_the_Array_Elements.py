class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        tr = 10**9 + 7
        last = pow(2, p, tr)-1
        biggestPossible = last - 1
        biggestCount = pow(2, p-1)-1
       
        return (pow(biggestPossible, biggestCount, tr)*last)%tr
