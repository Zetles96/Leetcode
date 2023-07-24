# https://leetcode.com/problems/two-sum/
# Algo: Hash Table
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for n in range(len(nums)):
            if target - nums[n] in hash_map:
                return [hash_map[target - nums[n]], n]
            else:
                hash_map[nums[n]] = n