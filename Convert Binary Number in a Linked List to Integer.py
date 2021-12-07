# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        string=""
        while head!=None:
            string+=str(head.val)
            head=head.next
        t=int(string,2)
        return t