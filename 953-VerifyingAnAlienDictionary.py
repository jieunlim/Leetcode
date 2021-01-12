class Solution:
    def isAlienSorted(self, words, order):
        dic = {ch:i for i, ch in enumerate(order) }
        for a, b in zip(words, words[1:]):  
            if len(a)>len(b) and a[:len(b)] == b: return False
            for s1, s2 in zip(a,b):
                if dic[s1] > dic[s2]:
                    return False
                elif dic[s1] < dic[s2]:
                    break
        return True


    def isAlienSorted2(self, words, order):
        dic = {ch:i for i, ch in enumerate(order) }
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            if len(w1)>len(w2) and w1[:len(w2)]==w2:
                    return False
            for j in range(len(w1)):
                if dic[w1[j]] > dic[w2[j]]:
                    return False
                elif dic[w1[j]] < dic[w2[j]]:
                    break
        return True

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
obj = Solution()
print(obj.isAlienSorted(words, order))
