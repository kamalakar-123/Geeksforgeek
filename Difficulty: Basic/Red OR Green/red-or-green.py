class Solution:
    def redOrGreen(self, s: str) -> int:
        # code here
        red=0
        green=0
        for ch in s:
            if ch=="R":
                red+=1
            else:
                green+=1
                
        return min(red,green)