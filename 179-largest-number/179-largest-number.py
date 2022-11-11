class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        res = ""
        string_nums = [str(i) for i in nums]
        
        while string_nums:
            max_num = ""
            for i in string_nums:
                if not max_num:
                    max_num = i
                elif i + max_num > max_num + i:
                    max_num = i
                    
            res += max_num
            string_nums.remove(max_num)
            
        if res[0] == "0":
            return "0"
            
        return res