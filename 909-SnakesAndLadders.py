from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def label_to_position(label):
            r, c = divmod(label-1, n) # label-1//n = r, label-1 % n = c
            print(f"label:{label}, r:{r}, c:{c}")
            if r % 2 == 0:
                print(f"{r % 2}, r:{n-1-r}, c:{c}")
                return n-1-r, c
            else:
                print(f"{r % 2}, r:{n-1-r}, c:{n-1-c}")
                return n-1-r, n-1-c
        
        
        
        n = len(board)
        seen = set()
        queue = collections.deque()
        queue.append((1,0))
        while queue:
            label, step = queue.popleft()
            r, c = label_to_position(label)
            if board[r][c] != -1:
                label = board[r][c]
            if label == n*n:
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n*n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step+1))
        return -1        
