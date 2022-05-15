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
