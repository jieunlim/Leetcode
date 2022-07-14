class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dic = {}
        words.sort(key = lambda x: len(x))
        sol = 1
        for word in words:
            dic[word] = 1
            for i in range(len(word)):
                prev = word[:i]+word[i+1:]
                if prev in dic:
                    dic[word] = max(dic[word], dic[prev] + 1)
                    sol = max(sol, dic[word])
        return sol
