
## Problem2 (https://leetcode.com/problems/remove-nth-node-from-end-of-list/)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def find_length(self, root):
        temp = root
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        return count
    
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length of the linkedlist
        length = self.find_length(head)
        
        #find the number of iterations required
        count = length - n
        
        #take prev and current node
        prev = None
        temp = head
        
        #while iterations still remain
        while count > 0:
            prev = temp
            temp = temp.next
            count -= 1

        #if the node is the first element 
        if prev is None:
            #change the position of the head
            head = head.next
            del temp
            return head
        
        prev.next = temp.next
        del temp
        return head
    
    