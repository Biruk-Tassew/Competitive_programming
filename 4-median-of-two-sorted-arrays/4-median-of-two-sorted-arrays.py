class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        big_mat = sorted(nums1+nums2)
        
        if len(big_mat)%2:
            return big_mat[len(big_mat)//2]
        else:
            return (big_mat[len(big_mat)//2] + big_mat[(len(big_mat)//2)-1])/2