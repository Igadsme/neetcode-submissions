from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start: int) -> List[str]:
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]
            
            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Get all valid sentences possible from the remaining substring
                    sub_sentences = backtrack(end)
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
                            
            memo[start] = res
            return res

        return backtrack(0)
        