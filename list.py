#Unique elements

lst = [1,2,2,3,44,5,44,1,3,6,7,8,9]
new_lst = []
for i in range(len(lst)):   
    if lst[i] not in new_lst:
        new_lst.append(lst[i])
print("Unique elements using new list :",new_lst)   

lst2=list(set(lst))
print("Unique elements using set :",lst2)  

#Non-Repeating elements

lst3 = []
for num in lst:
    if lst.count(num)==1:
        lst3.append(num)
print("Non-repeating elements :",lst3)
