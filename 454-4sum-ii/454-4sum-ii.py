class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        Cnt1, Cnt2, ans = Counter(), Counter(), 0
        for a, b in product(nums1, nums2):
            Cnt1[a + b] += 1
            
        for c, d in product(nums3, nums4):
            Cnt2[c + d] += 1
            
        for val in Cnt1:
            if -val in Cnt2:
                ans += Cnt1[val]*Cnt2[-val]
                
        return ans