# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #T: O(n)
        #S: O(1) and call stack
        if not l1: return l2
        if not l2: return l1
        
        dummy = ListNode()
        
        if l1.val<l2.val:
            dummy.next = l1
            dummy.next.next = self.mergeTwoLists(l1.next, l2)
        else:
            dummy.next = l2
            dummy.next.next = self.mergeTwoLists(l1, l2.next)
            
        return dummy.next
    def mergeTwoLists2 (self, l1: ListNode, l2: ListNode) -> ListNode:
        #T: O(n)
        #S: O(1)
         if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = cur = ListNode()
        
        while l1 and l2:
            if l1.val<l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next
        

flist1 = ListNode(1)
flist2 = ListNode(3)
flist3 = ListNode(5)

slist1 = ListNode(2)
slist2 = ListNode(4)
slist3 = ListNode(6)

flist1.next = flist2
flist2.next = flist3

slist1.next = slist2
slist2.next = slist3

obj = Solution()
rtn = obj.mergeTwoLists2(flist1, slist1)

while rtn:
    print(rtn.val)
    rtn = rtn.next
