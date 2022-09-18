def Sort(list):
    if len(list) > 1:
        
        r = len(list)//2
        L = list[:r]
        M = list[r:]

        Sort(L)
        Sort(M)

        i = j = k = 0


        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                list[k] = L[i]
                print("(",L[i],M[j],")")
                i += 1
            else:
                list[k] = M[j]
                print("(",L[i],M[j],")")
                j += 1
            k += 1


        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            list[k] = M[j]
            j += 1
            k += 1
list = [1,6,4,3,8,7,9]
n = 7
print("Current List")
print(list)
print(" Added into new sorted array")
Sort(list)
print("final list")
print(list)