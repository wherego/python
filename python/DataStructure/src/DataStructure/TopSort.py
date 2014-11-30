def topSort(G):
    top=[]
    queue=[]
    inDegree={}
    for v in G:
        inDegree[v]=0
    for v in G:
        for w in v.getNeighbors():
            inDegree[w]+=1
    for v in inDegree:
        if inDegree[v]==0:
            queue.append(v)
    while queue:
        v=queue.pop(0)
        top.append(v)
        for i in v.getNeighbors():
            inDegree[i]-=1
            if inDegree[i]==0:
                queue.append(i)
    return top