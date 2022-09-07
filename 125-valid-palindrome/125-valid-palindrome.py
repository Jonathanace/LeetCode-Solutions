class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set('abcdefghijlkmnopqrstuvwxyz1234567890')
        temp = ''
        for i in s.lower():
            if i in alphanumeric:
                temp += i
        return temp[::-1] == temp