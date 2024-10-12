def anagram(txt1,txt2):
    if len(txt1)!=len(txt2):     #Checking whether the length of the texts matches.
        return False
    else:
        dict1,dict2={},{}        #Creating a frequency dictionary for both texts.
        for i in txt1:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for j in txt2:
            if j not in dict2:
                dict2[j]=1
            else:
                dict2[j]+=1
        if len(dict1)!=len(dict2):                 #Checking whether the length of the dictionaries matches.
            return False
        else:
            for key,value in dict1.items():
                if key not in dict2:               #Checking whether the key in dict1 is also there in dict2.
                    return False
                else:
                    if dict1[key]!=dict2[key]:     #Checking whether the count of key in dict1 is same as that of  dict2.
                        return False
            return True                            #If none of them got it wrong, return True
        
txt1 = input("Enter Text-1 : ")
txt2 = input("Enter Text-2 : ")

if anagram(txt1,txt2):
    print("\nText-1 is an anagram of Text-2\n")
else:
    print("\nText-1 is not an anagram of Text-2\n")
