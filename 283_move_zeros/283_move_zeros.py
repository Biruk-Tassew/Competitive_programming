#283_move_zeros

class Solution:

    def moveZeroes(self, nums: list[int]) -> None:

        for i in nums:

            if not i:

                nums.remove(i)

                nums.append(i)

nums = [3, 1, 0,2, 0, 3, 4, 0]

sol = Solution()

sol.moveZeroes(nums)

print(nums)

