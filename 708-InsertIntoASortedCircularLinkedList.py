class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        
        prev, curr = head, head.next
        
        while prev.next != head:
          
            #1-(2)-3
            if prev.val <= node.val <= curr.val: break
              
            #3-(4)-1  / 3-(0)-1
            if prev.val > curr.val and (node.val > prev.val or node.val < curr.val): break
            
            prev, curr = prev.next, curr.next
            
        #insert node
        node.next = curr
        prev.next = node
        
        return head
