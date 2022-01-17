def compareTriplets(a, b):
    pointAlice = 0
    pointBob = 0
    for i in range(len(a)):
        if a[i]>b[i]:
            pointAlice+=1
        elif a[i]<b[i]:
            pointBob+=1
        else:
            pass
        
    output = [pointAlice,pointBob]
    return output