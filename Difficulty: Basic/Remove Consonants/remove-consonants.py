class Solution:
    def remConsonants(self, s):
        # code here
        result=''
        v=['a','e','i','o','u','A','E',"I",'O',"U"]
        for i in s:
            if i in v:
                
                result=result+i
        return result