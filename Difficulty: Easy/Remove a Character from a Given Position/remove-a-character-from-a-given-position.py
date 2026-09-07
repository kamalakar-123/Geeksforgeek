class Solution:
    def removeCharacter(self, s, pos):
        # code here
        return s[:pos] + s[pos+1:]