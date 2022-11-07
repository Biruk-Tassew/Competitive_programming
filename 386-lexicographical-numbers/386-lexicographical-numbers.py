class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        s = list(map(str, [i for i in range(1, n+1)]))
                 
        return sorted(s)