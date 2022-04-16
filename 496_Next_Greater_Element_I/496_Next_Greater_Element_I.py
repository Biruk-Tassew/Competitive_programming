class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        outPut = []
        for j in nums1:
            for i in nums2[nums2.index(j):]:
                if stack == []:
                    stack.append(i)
                    if i <= j and nums2.index(i) == len(nums2)-1:
                        outPut.append(-1)
                        stack = []
                        break
                    continue
                else:
                    if i > j:
                        outPut.append(i)
                        stack = []
                        break
                    elif i <= j and nums2.index(i) == len(nums2)-1:
                        outPut.append(-1)
                        stack = []
                        break
                        
        return outPut
