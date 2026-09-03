class Solution:
    
    #  Push elements of an array into a stack.
    def push(self, arr):
        # code here
        stack= []
        for i in range(len(arr)):
            stack.append(arr[i])
        return stack
    
    #  Print elements of a stack and pop them.
    def printAndPop(self, stack):
        # code here
        while len(stack)>0:
            print(stack.pop(),end=' ')