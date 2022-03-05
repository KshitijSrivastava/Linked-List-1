
## Problem1 (https://leetcode.com/problems/reverse-linked-list/)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def rev(head, prev):
            if head is None:
                return prev
            
            nxt = head.next
            head.next = prev
            return rev(nxt, head)
            
        return rev(head, None)
    
    #iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        
        temp = head
        
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            
            
        return prev
    