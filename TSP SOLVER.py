# Ludhiana=(0,61,140,106,93)
# Jalandhar=(61,0,80,149,154)
# Amritsar=(140,80,0,229,235)
# Chandigar=(106,149,229,0,75)
# Patiala=(93,154,235,75,0)


def check_min(l):
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1

    if i == -1:
        return False

    j = i+1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True

from sys import maxsize
def TSP(graph,start):
    v=[]
    points=len(graph)
    for i in range(points):
        if i!=start:
            v.append(i)
    print(v)
    min_path=maxsize

    while True:
        cost=0
        s=start
        for i in range(len(v)):
            cost+=graph[s][v[i]]
            s=v[i]
        cost += graph[s][start]
        min_path=min(min_path,cost)
        if not check_min(v):
            break
    return min_path

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
graph = [[int(input()) for x in range (C)] for y in range(R)]
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(graph[i][j], end = " ")
    print()
start=0
res=TSP(graph,start)
print("Total Cost of Shortest Path:",res)