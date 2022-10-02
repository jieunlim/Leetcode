# Time: O(L1 + L2), Space: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2: return 
        elif not list1 or not list2: return list1 or list2
        
       
        dummy = cur = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        
        return dummy.next
                
            

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 or list2:
            if list1 and list2 :
                if list1.val < list2.val:
                    cur.next = list1
                    cur = list1
                    list1 = list1.next
                else :
                    cur.next = list2
                    cur = list2
                    list2 = list2.next
            else:
                
                if list1:
                    cur.next = list1
                    cur = list1
                    list1 = list1.next
                elif list2:
                    cur.next = list2
                    cur = list2
                    list2 = list2.next

        return dummy.next



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
      
#23 ** Heap
#Time: O(nlogk), Space: O(1) #O(2) for heap

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        
        if not list1 and not list2: return 
        elif not list1 or not list2: return list1 or list2
        
        heappush(heap, (list1.val, 0, list1))
        heappush(heap, (list2.val, 1, list2))
        
        dummy = cur = ListNode()
        while heap:
            val, idx, node = heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next: heappush(heap, (node.next.val, idx, node.next))
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
