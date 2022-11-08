class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        uni_tog = 0
        for i in nums:
            uni_tog ^= i
            
        right_most_one = 0
        while True:
            if uni_tog & 1:
                break
                
            uni_tog >>= 1
            right_most_one += 1
            
        num_one = 0
        num_two = 0
        for i in nums:
            if i & (1 << right_most_one):
                num_one ^= i
            else:
                num_two ^= i
                
        return [num_one, num_two]