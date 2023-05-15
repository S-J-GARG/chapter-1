
# M1=['a','b','c','d','e','f','g']   #! Given characters by user 
def user_input():
    # Prompt the user to enter values
    user_input = input("Enter values separated by spaces: ")

# Split the user input into individual values
    values = user_input.split()

# Convert the values to the desired data type (e.g., string)
    values = [str(value) for value in values]

# Print the resulting list
    return values


M1=user_input()

def proces_mtrx_char_len_2(M1): # It is used to generate all possible 2 character different string of  
    
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
    return storing_matrix #? filter_matrix tion will return generated M3 matrix
return_matrix=proces_mtrx_char_len_2(M1)

def proces_mtrx_char_len_3(return_matrix):
    x=int(pow(len(M1),3)) # count the number of indiviual multipiction needed and also number of loops
    
    copy_matix=return_matrix              #? make a copy for making row matrix and column matrix multipiction

    storing_matrix=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    storing_matrix[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    storing_matrix[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return storing_matrix #? filter_matrix tion will return generated M3 matrix
return_matrix=proces_mtrx_char_len_3(return_matrix)

def filter_matrix (return_matrix):
    return  [x for x in return_matrix if len(x)>2 and x[0]!=x[1] and x[0]!=x[2] ] 

# print(filter_matrix (return_matrix))
# print(len(filter_matrix (return_matrix)))

def four_char_lenth(M1):
    x=int(pow(len(M1),4)) # count the number of indiviual multipiction needed and also number of loops
    # 
    copy_matix=return_matrix             #? make a copy for making row matrix and column matrix multipiction

    storing_matrix=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    storing_matrix[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    storing_matrix[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return storing_matrix #? filter_matrix tion will return generated M3 matrix
return_matrix=four_char_lenth(M1)

def filter_matrix(return_matrix):
    return  [x for x in return_matrix if len(x)==4 and x[0]!=x[1] and x[0]!=x[2] and x[0]!=x[3] and x[1]!=x[0]and x[1]!=x[0] and x[1]!=x[2] and x[1]!=x[3] and x[2]!=x[0] and x[2]!=x[1] and x[2]!=x[3] and x[3]!=x[0] and x[3]!=x[1] and x[3]!=x[2] ]
# print(filter_matrix(return_matrix))
# print(len(filter_matrix(return_matrix)))
return_matrix=filter_matrix(return_matrix)

def five_char_lenth(M1):
    x=int(pow(len(M1),5)) # count the number of indiviual multipiction needed and also number of loops
    
    copy_matix=return_matrix             #? make a copy for making row matrix and column matrix multipiction

    storing_matrix=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    storing_matrix[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    storing_matrix[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return storing_matrix #? filter_matrix tion will return generated M3 matrix
return_matrix=five_char_lenth(M1)
# print(return_matrix)
# print(len(return_matrix))
def remove_none(return_matrix):
    return[x for x in return_matrix if x!=None ]
return_matrix=remove_none(return_matrix)
def filter_matrix(return_matrix):
    return  [x for x in return_matrix if len(x)==5 and x[0]!=x[1] and x[0]!=x[2] and x[0]!=x[3] and x[0]!=x[4]and x[1]!=x[0] and x[1]!=x[2] and x[1]!=x[3] and x[2]!=x[0] and x[2]!=x[1] and x[2]!=x[3] ]
# print(filter_matrix(return_matrix))
# print(len(filter_matrix(return_matrix)))
return_matrix=filter_matrix(return_matrix)
def six_char_lenth(M1):
    x=int(pow(len(M1),6)) # count the number of indiviual multipiction needed and also number of loops
    
    copy_matix=return_matrix             #? make a copy for making row matrix and column matrix multipiction

    storing_matrix=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    storing_matrix[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    storing_matrix[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return storing_matrix #? filter_matrix tion will return generated M3 matrix
return_matrix=six_char_lenth(M1)
# print(return_matrix)
# print(len(return_matrix))
def remove_none(return_matrix):
    return[x for x in return_matrix if x!=None ]
return_matrix=remove_none(return_matrix)
def filter_matrix(return_matrix):
    return  [x for x in return_matrix if len(x)==6 and x[0]!=x[1] and x[0]!=x[2] and x[0]!=x[3] and x[0]!=x[4]and x[0]!=x[5] and x[1]!=x[2] and x[1]!=x[3] and x[2]!=x[0] and x[2]!=x[1] and x[2]!=x[3]]
# print(filter_matrix(return_matrix))
return_matrix=filter_matrix(return_matrix)
def seven_char_lenth(M1):
    x=int(pow(len(M1),7)) # count the number of indiviual multipiction needed and also number of loops
    
    copy_matix=return_matrix             #? make a copy for making row matrix and column matrix multipiction

    storing_matrix=[None]*x   #? make a another matrix to store all multipied element of M1 and copy_matix
    
    k=0

    while k<=x*len(M1): # while loop total multipication need to genrate all possible string

        for i in range(len(M1)): # it will multiply all element of M1 to all elements of copy_matix
            j=0
            while j<=len(copy_matix)-1: #! to check and add matrix element of copy_matix with element intiated by M1 in for loop
            
                if M1[i]!=copy_matix[j]: # check if intiated any element of M1 is not same(equal) as picking elements of copy_matix
                
                    storing_matrix[k]=M1[i]+copy_matix[j] # if condition satisfy then storing M3[storing index]= M1[initiated for loop indexing] + copy_matix[intiated index of while loop for copy_matix]
                
                    k+=1  # To move on next element index of M3 since previous index has taken the space
                
                    j+=1  # To move on for next element of copy_matix to add with intiated element of M1
                    continue
            
                else:        # check if intiated any element of M1 is same(equal) as picking elements of copy_matix then
            
                    storing_matrix[k]=M1[i] # storing matrix M3[storing index]= M1[initiated for loop indexing] 
            
                    k+=1    # To move on next element index of M3 since previous index has taken the space
               
                    j+=1   # To move on for next element of copy_matix to add with intiated element of M1
            continue
        break
    return storing_matrix #? filter_matrix tion will return generated M3 matrix
return_matrix=seven_char_lenth(M1)

def remove_none(return_matrix):
    return[x for x in return_matrix if x!=None ]
return_matrix=remove_none(return_matrix)
# print(return_matrix)
def filter_matrix(return_matrix):
    return [x for x in return_matrix if len(x)==7 and x[0]!=x[1] and x[0]!=x[2] and x[0]!=x[3] and x[0]!=x[4]and x[0]!=x[5] and x[0]!=x[6] ]

print(len(filter_matrix(return_matrix)))
