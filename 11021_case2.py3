num = int(input())

for i in range(num) :
    sum = 0
    a,b = input().split()
    sum = int(a)+int(b)
    print("Case #%d: %d"%(i+1,sum))