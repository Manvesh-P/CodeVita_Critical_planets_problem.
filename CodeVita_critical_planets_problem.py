# CodeVita Critical planet problem.

from collections import defaultdict

list1 = []
list2 = []
list3 = []

d = defaultdict(list)

c = 0

M,N = map(int, input("Enter total number of paths and planets:").split())


for i in range(0, M):
    a, b = map(int, input().split())
    list1.append(a)
    list2.append(b)
    
# print(list1)
# print(list2)

for j in range(0, N):
    for k in range(0, len(list1)):
        
        if j == list1[k]:
            d[j].append(list2[k])
            

            
for j in range(0, N):
    for k in range(0, len(list2)):
        
        if j == list2[k]:
            d[j].append(list1[k])

            
            
for i in d:
    e = len(d[i])
    
    if e == 1:
        list3.append(i)
        
    else:
        f = d[i]
        
        for j in range(0, len(f)-1):
            
            g = d[f[j]]
            
            for k in range(0, len(g)):
                
                if g[k] != f[j+1]:
                    c += 1
                    
            if c == len(g):
                list3.append(i)
                
            c = 0
        
            
print("\nThe critical planets are:")   

if len(list3) == 0:
    print("-1")
else:
    for i in range(0, len(list3)):
        print(list3[i])
