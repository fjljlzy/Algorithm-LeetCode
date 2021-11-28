'''
1 2 3 4 5
5 4 3 2 1
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 迭代写法，较为简单基础
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
      
      
# 递归写法：
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 写递归第一步，确定跳出循环条件
        if not head or not head.next:
            return head
        last_node = self.reverseList(head.next)
        # 把大问题切分成小问题
        head.next.next = head
        head.next = None
        return last_node
