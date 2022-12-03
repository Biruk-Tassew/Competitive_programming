class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        bucket = [[] for _ in range(len(s)+1)]
        for i in count:
            bucket[count[i]].append(i)
            
        ans = ""
        for i in range(len(s), -1, -1):
            for j in bucket[i]:
                ans += j*i
                
        return ans