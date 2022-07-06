class Solution:
    def countVowels(self, word: str) -> int:
        outPut = []
        
        for i in range(len(word)):
            if word[i] in 'aeiou':
                outPut.append((i+1)*(len(word)-i))
                              
        return sum(outPut)
