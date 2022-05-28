# T: O(Nk) k: len of string, n: len of strs
# S: O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        
        for w in strs:
            t = [0]*26
            for c in w:
                t[ord(c)-ord('a')]+=1
            dic[tuple(t)].append(w)
        
        return [val for key, val in dic.items()] # return dic.values()
      
# T: O(N * klogk) k: len of string, n: len of strs
# S: O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        
        for s in strs:
            dic[tuple(sorted(s))].append(s)
            
        
        return dic.values()
