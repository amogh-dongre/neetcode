# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow , fast = head , head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first_half , second_half = head , prev

        while second_half:
            tmpf , tmps = first_half.next , second_half.next
            first_half.next = second_half
            second_half.next = tmpf
            first_half , second_half = tmpf , tmps

        