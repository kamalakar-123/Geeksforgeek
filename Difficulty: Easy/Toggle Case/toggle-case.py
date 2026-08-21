class Solution:
    def toggleCase(self, s):
        # code here
        new=""
        for ch in s:
            if ch.islower():
                new+=ch.upper()
            else:
                new+=ch.lower()
        return new