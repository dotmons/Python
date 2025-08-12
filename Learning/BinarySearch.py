
    
def bin_search(ls, search)-> int:
    left: int = 0
    right: int = len(ls)-1
    mid: int = (left+right)//2

    while (left<=right):

        if (search == ls[mid]):
            return mid

        if (search >= ls[mid]):
            left = mid + 1

        else:
            right = mid - 1
        
        mid = (left+right)//2
    
    

    
    return -1


ls = [2,3,7,10,13,17]
print(bin_search(ls, 12))