'''
二分查找 首先难的是寻找思路，其次难的是正确的写边界条件。
[4,5,6,7,0,1,2]
0

l = 0, r = 6
mid = 3 value = 7
because value > target
thus 
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

