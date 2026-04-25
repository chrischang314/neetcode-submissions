class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderdict = {}
        for i, c in enumerate(order):
            orderdict[c] = i
        
        def compare(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                if orderdict[word1[i]] > orderdict[word2[i]]:
                    return -1
                elif orderdict[word1[i]] < orderdict[word2[i]]:
                    return 1
                i += 1
            if i < len(word1):
                return -1
            if i < len(word2):
                return 1
            return 0
        
        for i in range(len(words) - 1):
            if compare(words[i], words[i + 1]) == -1:
                return False
        return True