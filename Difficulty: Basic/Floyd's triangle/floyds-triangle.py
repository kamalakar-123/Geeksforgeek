n = int(input())

# code here
m=1
for i in range(n):
    for j in range(i+1):
        print(m, end=" ")
        m+=1
    print()
    
