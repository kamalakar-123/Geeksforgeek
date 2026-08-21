n = int(input())

# code here
for i in range(1,n+1):
    if i==n:
        print("*" *(2*n-1))
    else:
        
        spaces=2*(n-i)-1
        print("*" * i + " " * spaces + "*" * i)

for i in range(n-1,0,-1):
    spaces = 2*(n-i)-1
    print("*" * i + " " * spaces + "*" * i)