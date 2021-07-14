#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)
        self.post_num = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((self.post_num, tweetId))
        self.post_num += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = list()
        res += self.tweets[userId]
        for user in self.users[userId]:
            res += self.tweets[user]
        res.sort(reverse=True)

        if len(res) > 10:
            return list(map(lambda x:x[1], res[0:10]))
        return list(map(lambda x:x[1], res))



    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.users[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        val = self.users[followerId]
        if followeeId in val:
            self.users[followerId].remove(followeeId)

