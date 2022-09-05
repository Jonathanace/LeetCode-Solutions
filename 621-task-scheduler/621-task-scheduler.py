class Solution:
    def leastInterval(self, tasks, n):
        freqs = {}
        for i in tasks:
            freqs[i] = freqs.get(i, 0) + 1
        most_freq = max(freqs.values())
        most_freq_count = len([i for i in freqs.values() if i == most_freq])
        return max(len(tasks), (most_freq - 1) * (n + 1) + most_freq_count)