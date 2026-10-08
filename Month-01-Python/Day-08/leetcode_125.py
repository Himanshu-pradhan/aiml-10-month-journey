class Solution:
    def isPalindrome(self, s):
        s = s.lower()

        text = ""

        for char in s:
            if char.isalnum():
                text = text+ char

        if text == text[::-1]:
            return True
        else:
            return False
