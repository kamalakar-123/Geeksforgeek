class Solution:
    def countVowels(self, s):
        #code here
        vowels=""
        for ch in s:
            if ch in "aeiou":
                if ch not in vowels:
                    vowels+=ch
        return len(vowels)