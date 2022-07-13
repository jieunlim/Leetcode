class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sol = 1
        words_dict = {}
        words = sorted(words, key = len)
        print(words)
        
        for word in words:
            words_dict[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in words_dict:
                    words_dict[word] = max(words_dict[prev] + 1, words_dict[word])
                    sol = max(sol, words_dict[word])
        return sol
