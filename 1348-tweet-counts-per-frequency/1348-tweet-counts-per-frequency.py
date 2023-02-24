class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        interval = 0
        if freq == "minute":
            interval = 60
        elif freq == "hour":
            interval = 60**2
        elif freq == "day":
            interval = 60**2 * 24
            
        res_len = (endTime - startTime)// interval + 1
        res = [0]*res_len
            
        for tweetTime in self.tweets[tweetName]:
            if startTime <= tweetTime <= endTime:
                res[(tweetTime-startTime)//interval] += 1
                
        return res
                


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)