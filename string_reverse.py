class Solution:
    def reverseString(self, s: str) -> str:
        # code here
        new_str = ""
        for i in range(len(s)):
            new_str = s[i] + new_str
        return new_str