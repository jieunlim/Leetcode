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
