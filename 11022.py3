num = int(input())

for i in range(1,num+1) :
    sum = 0
    a,b = input().split()
    sum = int(a)+int(b)
    print("Case #",i,": ",a," + ",b," = ",sum, sep='')