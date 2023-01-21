#program to product of list
#ishan hambir

def lstProduct(myLst):
 
    result = 1
    for x in myLst:
        result = result * x
    return result
 
 
lst1 = [10, 20, 30]
lst2 = [4, 5, 6]
print(lstProduct(lst1))
print(lstProduct(lst2))
