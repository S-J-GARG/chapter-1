# a=['aab','aac','aba','abc','aca','acb','bab','bac','bba','bbc','bca','bcb','cab','cac','cba','cbc','cca','ccb','a','as']
# b=[None]*len(a)
# print(len(a))

# j=0
# while j<=len(a)-1 :
#     if a[j][0]==a[j][1] or a[j][0]==a[j][2]:
#         b[j]=a[j]
#     j+=1

# def func(a):
#     return[x for x in a if len(x)>2 and x[0]!=x[1] and x[0]!=x[2] ]
def remove_common_elements(a, b):
    return [x for x in a if x not in b]
       
# print(func(a))