class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = {}
        for word in words:
            freqs[word] = freqs.get(word, 0) + 1
            
        word_freq = [(word, -freqs[word]) for word in freqs.keys()]
        word_freq.sort(key = lambda x: (x[1], x[0]), reverse=True)
        return [i[0] for i in word_freq][-k:][::-1]