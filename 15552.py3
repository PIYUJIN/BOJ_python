import sys

n = int(input())

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    # sys.stdin.readline() == input()
    # import sys를 앞에 써줘야 한다.
    print(a+b)