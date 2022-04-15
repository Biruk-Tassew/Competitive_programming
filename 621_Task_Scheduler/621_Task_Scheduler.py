class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        outPut = 0
        countDic = Counter(tasks)
        
        freqNo = max(countDic.values())
        freqNoSpace = (freqNo - 1)*(n + 1)
        noFreqNo = 0
        noFreqNo = sum(value == freqNo for value in countDic.values())
                
        outPut = max(freqNoSpace + noFreqNo, len(tasks))
        
        return outPut
