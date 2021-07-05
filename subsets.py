def subsets(set):
    L = len(set)
    N = 2**L
    subsets = []
    setDict = dict(zip(set, [0]*L))
    for i in range(N):
        subset = [s for s in setDict.keys() if setDict[s]!=0]
        subsets.append(subset)
        for k in setDict.keys():
            setDict[k] += 1
            if setDict[k]==2:
                setDict[k]=0
                continue
            break
    return subsets

print(subsets([1,2,3,4]))