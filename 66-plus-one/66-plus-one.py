class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        for i in digits[::-1]:
            num *= 10 
            num += i
        num = str(num)[::-1][:-1]
        num = int(num) + 1
        return [i for i in str(num)]
            