list = [1,6,4,3,8,7,9]
n = 7
print("Current List")
print(list)
print("Swaps")
for i in range(0,n-1):
    min = list[i]
    for j in range(i+1,n-1):
        if list[j]<min:
            min = list[j]
            pos = j
    if min<list[i]:
        print("(",list[i],min,")")
        temp = list[i]
        list[i]=list[pos]
        list[pos]=temp
print("final list")
print(list)