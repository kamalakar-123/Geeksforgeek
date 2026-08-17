class Solution:
    def divisibleByDigits(self, S):
        ans = 0

        for d in "123456789":
            if d in S:
                rem = 0

                for x in S:
                    rem = (rem * 10 + int(x)) % int(d)

                if rem == 0:
                    ans += S.count(d)

        return ans