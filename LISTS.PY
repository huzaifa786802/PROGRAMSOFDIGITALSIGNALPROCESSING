def lists_are_equal(list1,list2):
    if len(list1)!=len(list2):
        return False
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            return False
        return True
list1=[1,2,3]
list2=[1,2,3]
if lists_are_equal(list1,list2):
    print("The lists are equal")
else:
    print("The lists are not equal")   