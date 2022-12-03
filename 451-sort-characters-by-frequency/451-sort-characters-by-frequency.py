class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        ans = []
        for i in count:
            ans.append([count[i], i])
            
        ans.sort(reverse=True)
        res = ""
        for i in ans:
            res += i[1]*i[0]
            
        return res