list = [1,6,4,3,8,7,9]
n = 7
print("Current List")
print(list)
print("Swaps")
for i in list:
    for j in range(0,n-i-1):
        if list[j]>list[j+1]:
            print("(",list[j],list[j+1],")")
            temp = list[j]
            list[j]=list[j+1]
            list[j+1]=temp;
print("final list")
print(list)