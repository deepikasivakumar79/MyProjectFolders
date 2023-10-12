def transitionPoint(arr, n):
    #Code here
    a=0
    b=n
    if arr == [1]*n:
        return 0
    elif arr == [0]*n:
        return -1
    n=(a+b)//2
    while n>0:
        if arr[n]==1 and arr[n-1]==0:
            return n
        elif arr[n]==1 and arr[n-1]==1:
            b=n-1
            n=(a+b)//2
        else:
            a=n+1
            n=(a+b)//2
    return -1
print(transitionPoint([1,1,1,1,1],5))

def transitionPoint(arr, n):
    #Code here
    
    s=0
    e=len(arr)-1
    if len(arr) == 1:
        return 0
    while(s<e):
        mid = (s+e)//2
        
        if arr[mid] == 1:
           
            if arr[mid+1] == 1 and arr[mid-1] == 0:
                return mid
            else:
                e = mid - 1
        if arr[mid] ==0:
            if arr[mid+1]==1:
                return mid + 1
            else:
                s = mid + 1
    return -1
                