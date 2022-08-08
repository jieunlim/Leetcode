#O(#order + s) / O(s)  
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sol = []
        cnt = Counter(s)
        for c in order:
            if c in cnt:
                sol.append(c * cnt[c])
                del cnt[c]
        for c in cnt:
            sol.append(c * cnt[c])
        return ''.join(sol)
    
class Solution2:
    def customSortString(self, order: str, s: str) -> str:
        dic = {}
        cnt = Counter(s)
        in_ordered = ['']*len(s)
        not_in_ordered=['']*len(s)
        
        for i, ch in enumerate(order):
            dic[ch] = i
        
        for i, ch in enumerate(s):
            
            if ch in order:
                in_ordered[dic[ch]] = ch * cnt[ch]
            else: not_in_ordered.append(ch)
        
        return ''.join(in_ordered) + ''.join(not_in_ordered)
                
