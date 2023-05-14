
M1=['a','b','c','d','e','g']   #! Given characters by user 
def two_char_lenth(M1): # It is used to generate all possible 2 character different string of M1 
    
    x=int(pow(len(M1),2)) # count the number of indiviual multipiction needed and also number of loops

    M2=M1               #? make a copy for making row matrix and column matrix multipiction

    M3=[None]*x     #? make a another matrix to store all multipied element of M1 and M2
    
    k=0

    while k<=x: # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of M2
            j=0
            while j<=len(M1)-1: #! to check and add matrix element of M2 with element intiated by M1 in for loop
            
                if M1[i]!=M2[j]: # check if intiated any element of M1 is not same(equal) as picking elements of M2
                
                    M3[k]=M1[i]+M2[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + M2[intiated index of while loop for M2]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of M2 to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of M2 then
            
                    M3[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of M2 to add with intiated element of M1
            continue
        break
    return M3 #? function will return generated M3 matrix
M4=two_char_lenth(M1)
# print(M4)
def three_char_lenth(M4):
    x=int(pow(len(M1),3)) # count the number of indiviual multipiction needed and also number of loops
    print(x)
    M2=M4              #? make a copy for making row matrix and column matrix multipiction

    M5=[None]*x   #? make a another matrix to store all multipied element of M1 and M2
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of M2
            j=0
            while j<=len(M2)-1: #! to check and add matrix element of M2 with element intiated by M1 in for loop
            
                if M1[i]!=M2[j]: # check if intiated any element of M1 is not same(equal) as picking elements of M2
                
                    M5[k]=M1[i]+M2[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + M2[intiated index of while loop for M2]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of M2 to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of M2 then
            
                    M5[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of M2 to add with intiated element of M1
            continue
        break
    return M5 #? function will return generated M3 matrix
M6=three_char_lenth(M4)
# print(len(M6))
def func(M6):
    return  [x for x in M6 if len(x)>2 and x[0]!=x[1] and x[0]!=x[2] ] 

# print(func(M6))
# print(len(func(M6)))

def four_char_lenth(M1):
    x=int(pow(len(M1),4)) # count the number of indiviual multipiction needed and also number of loops
    # print(x)
    M2=M6             #? make a copy for making row matrix and column matrix multipiction

    M5=[None]*x   #? make a another matrix to store all multipied element of M1 and M2
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of M2
            j=0
            while j<=len(M2)-1: #! to check and add matrix element of M2 with element intiated by M1 in for loop
            
                if M1[i]!=M2[j]: # check if intiated any element of M1 is not same(equal) as picking elements of M2
                
                    M5[k]=M1[i]+M2[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + M2[intiated index of while loop for M2]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of M2 to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of M2 then
            
                    M5[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of M2 to add with intiated element of M1
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
    M2=M7             #? make a copy for making row matrix and column matrix multipiction

    M5=[None]*x   #? make a another matrix to store all multipied element of M1 and M2
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of M2
            j=0
            while j<=len(M2)-1: #! to check and add matrix element of M2 with element intiated by M1 in for loop
            
                if M1[i]!=M2[j]: # check if intiated any element of M1 is not same(equal) as picking elements of M2
                
                    M5[k]=M1[i]+M2[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + M2[intiated index of while loop for M2]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of M2 to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of M2 then
            
                    M5[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of M2 to add with intiated element of M1
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
    M2=M9             #? make a copy for making row matrix and column matrix multipiction

    M5=[None]*x   #? make a another matrix to store all multipied element of M1 and M2
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of M2
            j=0
            while j<=len(M2)-1: #! to check and add matrix element of M2 with element intiated by M1 in for loop
            
                if M1[i]!=M2[j]: # check if intiated any element of M1 is not same(equal) as picking elements of M2
                
                    M5[k]=M1[i]+M2[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + M2[intiated index of while loop for M2]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of M2 to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of M2 then
            
                    M5[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of M2 to add with intiated element of M1
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
print(filt_0(M10))