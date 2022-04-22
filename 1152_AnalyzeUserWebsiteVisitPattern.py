class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
         
        dic = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])): 
            dic[user].append(site)
        print(dic)
        patterns = Counter()

        for user, sites in dic.items():
            patterns.update((set(combinations(sites, 3))))
        print(patterns)
        return max(sorted(patterns), key=patterns.get)
