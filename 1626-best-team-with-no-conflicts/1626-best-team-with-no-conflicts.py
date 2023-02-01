class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score = sorted([(ages[i], scores[i]) for i in range(len(ages))])
        res = 0
        dp = [tup[1] for tup in age_score]

        for i in range(len(ages)-1,-1,-1):
            cur_max = 0
            for j in range(i+1,len(age_score)):
                if age_score[j][1] >= age_score[i][1]:
                    cur_max = max(cur_max,dp[j])
            dp[i] = cur_max + age_score[i][1]
            res = max(res, dp[i])
            
        return res