class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set('1234567890abcdefghijklmnopqrstuvwxyz')
        l = [i for i in s.lower() if i in alphanumeric]
        return l == l[::-1]