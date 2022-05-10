class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        def predict(nums):
            print(nums[0], nums)
            if len(nums) == 1:
                print(nums[0])
                return nums[0]
            return max(nums[0]-predict(nums[1:]), 
                       nums[-1]-predict(nums[:-1]))
        score = predict(nums)
        print(score)
        return score >= 0
