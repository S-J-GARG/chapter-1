
M1=['s','h','i','v','a','n','k']   #! Given characters by user 

def two_char_lenth(M1): # It is used to generate all possible 2 character different string of  
    
    x=int(pow(len(M1),2)) # count the number of indiviual multipiction needed and also number of loops

    copy_matix=M1               #? make a copy for making row matrix and column matrix multipiction

    storing_matrix=[None]*x     #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x: # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(M1)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    storing_matrix[k]=M1[i]+copy_matix[j] # if condition satisfy then storing storing[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of storing since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    storing_matrix[k]=M1[i] # storing matrix storing[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of storing since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return storing_matrix #? function will return generated M3 matrix
return_matrix=two_char_lenth(M1)
# print(return_matrix)
def three_char_lenth(return_matrix):
    x=int(pow(len(M1),3)) # count the number of indiviual multipiction needed and also number of loops
    print(x)
    copy_matix=return_matrix              #? make a copy for making row matrix and column matrix multipiction

    M5=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    M5[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    M5[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return M5 #? function will return generated M3 matrix
M6=three_char_lenth(return_matrix)
# print(len(M6))
def func(M6):
    return  [x for x in M6 if len(x)>2 and x[0]!=x[1] and x[0]!=x[2] ] 

# print(func(M6))
# print(len(func(M6)))

def four_char_lenth(M1):
    x=int(pow(len(M1),4)) # count the number of indiviual multipiction needed and also number of loops
    # print(x)
    copy_matix=M6             #? make a copy for making row matrix and column matrix multipiction

    M5=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    M5[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    M5[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return M5 #? function will return generated M3 matrix
M6=four_char_lenth(M1)

def filt_0(M6):
    return  [x for x in M6 if len(x)==4 and x[0]!=x[1] and x[0]!=x[2] and x[0]!=x[3] and x[1]!=x[0]and x[1]!=x[0] and x[1]!=x[2] and x[1]!=x[3] and x[2]!=x[0] and x[2]!=x[1] and x[2]!=x[3] and x[3]!=x[0] and x[3]!=x[1] and x[3]!=x[2] ]
# print(filt_0(M6))
# print(len(filt_0(M6)))
M7=filt_0(M6)

def five_char_lenth(M1):
    x=int(pow(len(M1),5)) # count the number of indiviual multipiction needed and also number of loops
    print(x)
    copy_matix=M7             #? make a copy for making row matrix and column matrix multipiction

    M5=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    M5[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    M5[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return M5 #? function will return generated M3 matrix
M7=five_char_lenth(M1)
# print(M7)
# print(len(M7))
def remove_none(M7):
    return[x for x in M7 if x!=None ]
M8=remove_none(M7)
def filt_0(M8):
    return  [x for x in M8 if len(x)==5 and x[0]!=x[1] and x[0]!=x[2] and x[0]!=x[3] and x[0]!=x[4]and x[1]!=x[0] and x[1]!=x[2] and x[1]!=x[3] and x[2]!=x[0] and x[2]!=x[1] and x[2]!=x[3] ]
# print(filt_0(M8))
# print(len(filt_0(M8)))
M9=filt_0(M8)
def six_char_lenth(M1):
    x=int(pow(len(M1),6)) # count the number of indiviual multipiction needed and also number of loops
    print(x)
    copy_matix=M9             #? make a copy for making row matrix and column matrix multipiction

    M5=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    M5[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    M5[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return M5 #? function will return generated M3 matrix
M7=six_char_lenth(M1)
# print(M7)
# print(len(M7))
def remove_none(M7):
    return[x for x in M7 if x!=None ]
M10=remove_none(M7)
def filt_0(M10):
    return  [x for x in M10 if len(x)==6 and x[0]!=x[1] and x[0]!=x[2] and x[0]!=x[3] and x[0]!=x[4]and x[0]!=x[5] and x[1]!=x[2] and x[1]!=x[3] and x[2]!=x[0] and x[2]!=x[1] and x[2]!=x[3]]
# print(filt_0(M10))
M11=filt_0(M10)
def seven_char_lenth(M1):
    x=int(pow(len(M1),7)) # count the number of indiviual multipiction needed and also number of loops
    print(x)
    copy_matix=M11             #? make a copy for making row matrix and column matrix multipiction

    M5=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    M5[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    M5[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return M5 #? function will return generated M3 matrix
M7=seven_char_lenth(M1)

def remove_none(M7):
    return[x for x in M7 if x!=None ]
M10=remove_none(M7)
# print(M10)
def filt_0(M10):
    return [x for x in M10 if len(x)==7 and x[0]!=x[1] and x[0]!=x[2] and x[0]!=x[3] and x[0]!=x[4]and x[0]!=x[5] and x[0]!=x[6] ]

# print(filt_0(M10))
