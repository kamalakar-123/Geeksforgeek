class Solution:
    def sortString(self, s: str) -> str:
        # code here
        s=list(s)
        s.sort()
        return "".join(s)