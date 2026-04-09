class Twitter:
    # should hava two dict like following and follwer?
    # heap can use to getnewsfeed but every user have a deque?
    # in the deque like id, userid order by id so can get newest

    # post:
    # iterate follower get userid list, add in their own deque

    # getnewfeed:
    # heappop each one deque to get twtid
    # follow 
    # shit how to delete each user's deque if they follow


    # second solution
    # each user twi id is a list [1,3,4] for user a
    # post is just append
    # getfeed is check following dict, get usr lists, get fed
    # follow and unfollow just update two dict
    def __init__(self):
        self.timer = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [timer, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer -= 1 # 用负数，这样小顶堆弹出的就是最小负数（即最近时间）
        self.tweetMap[userId].append([self.timer, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # 关注的人 + 自己
        self.followMap[userId].add(userId)
        
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                # 存入：时间，推文ID，该用户的列表，以及下一条推文的索引
                minHeap.append([time, tweetId, followeeId, index - 1])
        
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                nextTime, nextTweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [nextTime, nextTweetId, followeeId, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)