class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        outPut = [0]*len(nums)
        deque = collections.deque([0])
        outPut[0] = nums[0]
        print(outPut)
        for i in range(1, len(nums)):
            outPut[i] = nums[i] + outPut[deque[0]]
            while deque and outPut[i] >= outPut[deque[-1]]:
                deque.pop()
            while deque and i - deque[0] >= k:
                deque.popleft()
            deque.append(i)
        print(outPut)
        return outPut[-1]
