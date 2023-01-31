class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score = sorted([(ages[i], scores[i]) for i in range(len(ages))])

        dp = [tup[1] for tup in age_score]

        for i in range(len(ages)-1,-1,-1):
            x = age_score[i][1]
            maxi=0
            for j in range(i+1,len(age_score)):
                y = age_score[j][1]
                if y>=x:
                    maxi = max(maxi,dp[j])
            dp[i]=x+maxi

        return max(dp)