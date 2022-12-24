class Solution:
    def numTilings(self, n: int) -> int:
        A = [0] * (n + 1)
        B = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            A[i] = (B[i - 2] + A[i - 1]) % int(1e9 + 7)
            B[i] = (B[i - 1] + B[i - 2] + A[i - 1] * 2) % int(1e9 + 7)
        
        return B[n]