class Solution:
    def candy(self, ratings: List[int]) -> int:
        cur_max = 1
        count = [1]

        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index-1]:
                cur_max += 1
                count.append(cur_max)
            else:
                count.append(1)
                cur_max = 1

        for index in range(len(ratings)-2, -1, -1):
            if ratings[index] > ratings[index+1] and count[index] < count[index+1]+1:
                count[index] = count[index+1]+1

        return sum(count)