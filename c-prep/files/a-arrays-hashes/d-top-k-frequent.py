"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

"""
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(0, len(nums) + 1)]

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for elem, count in counts.items():
            buckets[count].append(elem)

        res = []
        for idx in range(len(buckets) - 1, 0, -1):
            for val in buckets[idx]:
                res.append(val)
                if len(res) == k:
                    return res
        