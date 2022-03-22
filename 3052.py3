num = []

for i in range(10) :
    inp = int(input())
    num.append(inp%42)
  
num = set(num)
print(len(num))