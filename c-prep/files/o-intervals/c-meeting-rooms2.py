"""
253. Meeting Rooms II - Explanation
Problem Link

Description
Given an array of meeting time interval objects consisting of start and end times
 [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of 
 days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
"""
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))
        
        time.sort(key=lambda x: (x[0], x[1]))
        
        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res
