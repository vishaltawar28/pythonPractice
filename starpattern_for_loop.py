'''
*
**
***
****
*****
'''
#using for loop
n=5
for i in range(0,n):
    for j in range(0, i+1):
        print('* ', end="")
    print()



#write function
def myfun(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print('* ', end="")
        print()

n=5
myfun(n)