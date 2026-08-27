class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list) # userId -> (count, tweetId)
        self.time = 0
        self.followMap = defaultdict(set) # userId -> set(followeeId)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.tweetMap[userId][:]
        for followeeId in self.followMap[userId]:
            tweets.extend(self.tweetMap[followeeId])
        tweets.sort(reverse=True, key=lambda x: x[0])
        res = []
        for i in range(10):
            if i < len(tweets):
                res.append(tweets[i][1])
            else:
                break
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
