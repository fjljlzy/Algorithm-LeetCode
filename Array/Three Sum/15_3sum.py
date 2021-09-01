# 两种解法，第一种是用哈希集，第二种是用排序加双指针，都是非常精彩的写法。
class Solution:
    def threeSum(self, nums):
        def twosum(i, res, nums):
            seen = set()
            f, l = i+1, len(nums)
            while f < l:
                c = -nums[i]-nums[f]
                if c in seen :
                    res.append([nums[i], nums[f], c])
                    while f+1< l and nums[f]== nums[f+1]:
                        f+=1
                seen.add(nums[f])
                f+=1
                
                
        res =[]
        nums.sort()
        for i, p in enumerate(nums):
            if p > 0:
                break
            if i == 0 or nums[i-1]!=nums[i]:
                twosum(i, res, nums)
        return res

# class Solution:
#     def threeSum(self, nums):
#         res =[]
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i]>0:
#                 break
#             if i==0 or nums[i-1]!= nums[i]:
#                 self.twoSums(nums,res, i)
#         return res
    
#     def twoSums(self, num, res, i):
#         l = i+1
#         r =len(num)-1
#         while ( f < l):
            
#             s = num[i]+num[f]+num[l]
#             if s < 0:
#                 f +=1
#             elif s > 0:
#                 l -=1
#             else :
#                 res.append([num[i], num[f], num[l]])
#                 f+=1
#                 l-=1
#                 while f <l and num[f] == num[f-1]:
#                     f+=1
