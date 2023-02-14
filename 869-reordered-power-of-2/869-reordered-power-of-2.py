class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = []
        for i in range(30):
            temp_num = str(2**i)
            count.append(Counter(temp_num))
            
            
        return Counter(str(n)) in count