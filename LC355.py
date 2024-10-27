import heapq
from collections import defaultdict
from copy import copy
from typing import List

class Twitter:
    def __init__(self):
        heap_list = [(0, 0, 0)]
        heapq.heapify(heap_list)
        self.tweets = heap_list
        self.current_tweet_age = 0
        self.follow_relationships = defaultdict(list)
    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, (-self.current_tweet_age, tweetId, userId))
        self.current_tweet_age += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_to_display = []
        heap_copy = copy(self.tweets)
        followees = self.follow_relationships[userId]
        while len(tweets_to_display) < 10  and len(heap_copy) > 0:
            tweet = heapq.heappop(heap_copy)
            if followees.count(tweet[2]) > 0 or tweet[2] == userId:
                tweets_to_display.append(tweet[1])

        return tweets_to_display
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_relationships[followerId].append(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.follow_relationships[followerId].count(followeeId) > 0:
            self.follow_relationships[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)