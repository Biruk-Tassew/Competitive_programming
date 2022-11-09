class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}
        
class Solution:
    def wordBreak(self, st: str, wordDict: List[str]):
        wordDict = set(wordDict)
        curr = []
        ans = []
        def backtrack(s, e):
            if e == len(st):
                if st[s:e] in wordDict:
                    curr.append(st[s:e+1])
                    ans.append(" ".join(curr))
                    curr.pop()
                return
            if e > len(st): return
            
            if st[s:e] in wordDict:
                curr.append(st[s:e])
                backtrack(e, e+1)
                curr.pop()
                
            backtrack(s, e+1)
        backtrack(0, 1)
        return ans
            