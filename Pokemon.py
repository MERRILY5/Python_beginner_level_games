l=[3,6,9,7]

maxi,mini = 0,0

for i in l:
    if maxi == 0  and mini == 0:
        maxi,mini = l[0],l[0]
        print(mini,maxi)
    else:
        mini= min(mini,i)
        maxi = max(maxi,i)
        print(mini,maxi)
        
