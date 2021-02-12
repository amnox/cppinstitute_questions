import bisect

def pick_box(arr, item):
    ind = bisect.bisect(arr, item)
    print(ind,arr)
    if(ind==len(arr)):
        return -1
    else:
        if(arr[ind-1]==item):
            return arr[ind-1]
        else:
            return arr[ind]

print(pick_box([2, 7, 9, 12,12,13],12))\

def height(root):
    if root is None:
        return -1
    Ldepth = height(root.left)
    Rdepth = height(root.right)
    
    return max(Ldepth,Rdepth)+1