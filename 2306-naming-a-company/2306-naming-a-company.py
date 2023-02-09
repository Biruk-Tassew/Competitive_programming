class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        seen = set(ideas)
        freq = Counter()
        letters = {x[0] for x in ideas}
        for idea in ideas: 
            for ch in letters: 
                if ch + idea[1:] not in seen: freq[idea[0], ch] += 1 
        ans = 0 
        for idea in ideas: 
            for ch in letters: 
                if ch + idea[1:] not in seen: ans += freq[ch, idea[0]]
        return ans 