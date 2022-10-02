# Divide and Conquer Iterative: O(n log k) / O(1)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2lists(l1, l2):
            dummy = cur = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next
            
            
        if not lists: return
        if len(lists)==1: return lists[0]
        m = len(lists)//2
        l = self.mergeKLists(lists[:m])
        r = self.mergeKLists(lists[m:])
        return merge2lists(l, r)
        
        
        
        
# Heap: O(n log k), k = # of linked lists / Space: O(n) for heap : Q21
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return
        heap = []
        for i, list in enumerate(lists):
            if list:
                heappush(heap, (list.val, i, list))
                
        dummy = cur = ListNode()
        while heap:
            val, idx, node = heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next: heappush(heap, (node.next.val, idx, node.next))
            
        return dummy.next
