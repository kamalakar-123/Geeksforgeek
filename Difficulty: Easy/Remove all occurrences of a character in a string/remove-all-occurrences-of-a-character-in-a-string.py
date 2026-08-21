class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        # code here
        new=""
        for ch in s:
            if ch!=c:
                new=new+ch
        return new