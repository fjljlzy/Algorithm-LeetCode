from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, i in enumerate(nums):
            diff = target - i
            if diff in d:
                return [index, d[diff]]
            else:
                d[i] = index
                
if __name__ == '__main__':
    # begin
    s = Solution()
    print （s.twoSum([3, 2, 4], 6)）
