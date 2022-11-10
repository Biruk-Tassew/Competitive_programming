class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre_sum = [cardPoints[0]]
        for i in range(1, len(cardPoints)):
            pre_sum.append(pre_sum[i-1]+cardPoints[i])
            
        whole_sum = pre_sum[-1]
        left = 0
        right = len(cardPoints)-k-1
        max_pts = 0
        
        while right < len(cardPoints):
            if not left:
                max_pts = max(max_pts, whole_sum-pre_sum[right])
            else:
                max_pts = max(max_pts, whole_sum-(pre_sum[right]-pre_sum[left-1]))
            left += 1
            right += 1
            
        return max_pts