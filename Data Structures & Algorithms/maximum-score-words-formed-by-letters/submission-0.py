from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Count available letters
        left_count = Counter(letters)
        
        # Precompute the score of each word and character counts for efficiency
        word_counts = [Counter(word) for word in words]
        word_scores = []
        for wc in word_counts:
            s = 0
            for char, count in wc.items():
                s += count * score[ord(char) - ord('a')]
            word_scores.append(s)
            
        def backtrack(i: int, current_letters: Counter) -> int:
            if i == len(words):
                return 0
            
            # Option 1: Skip the current word
            max_score = backtrack(i + 1, current_letters)
            
            # Option 2: Include the current word (if we have enough letters)
            wc = word_counts[i]
            if all(current_letters[char] >= count for char, count in wc.items()):
                # Deduct letters used by the word
                for char, count in wc.items():
                    current_letters[char] -= count
                
                # Recurse and add this word's score
                max_score = max(max_score, word_scores[i] + backtrack(i + 1, current_letters))
                
                # Backtrack: restore letters
                for char, count in wc.items():
                    current_letters[char] += count
                    
            return max_score

        return backtrack(0, left_count)