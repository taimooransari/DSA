def mergeSort(lst):
    if(len(lst)>1):
        r =len(lst)//2
        left,right = lst[:r],lst[r:]
        mergeSort(right),mergeSort(left)

        i=j=k=0

        while(i<len(left) and j<len(right)):

            if(left[i]<=right[j]):
                lst[k]=left[i]
                i+=1
            else:
                lst[k]=right[j]
                j+=1
            k+=1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst

arr = [12, 11, 13, 5, 6, 7]
print(mergeSort(arr))

    