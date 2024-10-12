import array as arr 

# Deleting 4th element from an array                               

arr1 = arr.array('i',[1,2,3,4,5,6,7,8,9,10])       # First approach
pos_to_del = 3
print("Array before deletion :",list(arr1))
new_arr=arr.array('i',[arr1[i] for i in range(len(arr1)) if i != pos_to_del])
print("Array after deletion :",list(new_arr))

arr1 = arr.array('i',[1,2,3,4,5,6,7,8,9,10])       # Second approach
pos_to_del = 3
print("Array before deletion :",list(arr1))
for i in range(pos_to_del,len(arr1)-1):
    arr1[i]=arr1[i+1]
print("Array after deletion :",list(arr1)[:(len(arr1)-1)])

#Reversing an array

lst = input("Enter the elements : ").split()
org_arr = arr.array('i',[int(elem) for elem in lst])
print("Array before reversing :",list(org_arr))
print("Array after reversing :",list(org_arr)[::-1])
