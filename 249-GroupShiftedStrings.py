class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i, string in enumerate(strings):
            if string[0]=='a': dic[string].append(string)
            else:
                diff = ord(string[0]) - ord('a')
                updated = ""
                for ch in string:
                    if ord(ch)- diff < ord('a'): 
                        updated += chr(ord(ch)- diff + 26)
                    else: updated += chr(ord(ch) - diff)
                dic[updated].append(string)
        # sol = []
        # for item, values in dic.items():
        #     sol.append(values)
        # return sol
        return list(dic.values()) # [value for key, value in dic.items()]
