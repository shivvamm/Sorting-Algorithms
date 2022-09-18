list = [1,6,4,3,8,7,9]
n = 7
print("Current List")
print(list)
print("Swaps")
for i in range(1,n-1):
    key = list[i]
    j=i-1
    while j>=0 and list[j]>key:
        list[j+1]=list[j]
        j=j-1
        print("(",list[j+1],key,")")
    list[j+1]=key
    
print("final list")
print(list)