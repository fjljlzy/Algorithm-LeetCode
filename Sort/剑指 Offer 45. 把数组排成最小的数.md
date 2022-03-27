# 剑指 Offer 45. 把数组排成最小的数
```python3
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        n = len(nums)
        strs = [str(i) for i in nums]  # 转成字符串

        # # 冒泡排序
        # for i in range(0, n - 1):
        #     for j in range(i + 1, n):
        #         s1, s2 = strs[i] + strs[j], strs[j] + strs[i]
        #         if s1 > s2:
        #             strs[j], strs[i] = strs[i], strs[j]
        # ans = ''.join(strs)

        # quick sort
        def quicksort(strs, l, r):
            if l >= r:
                return strs
            pivot = l
            i, j = l, r
            while i < j:
                while i < j and strs[j] + strs[pivot] > strs[pivot] + strs[j]:
                    j -= 1
                while i < j and strs[i] + strs[pivot] <= strs[pivot] + strs[i]:
                    i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[pivot], strs[j] = strs[j], strs[pivot]
            quicksort(strs, l, j - 1)
            quicksort(strs, j + 1, r)

        quicksort(strs, 0, len(strs) - 1)
        return ''.join(strs)
```