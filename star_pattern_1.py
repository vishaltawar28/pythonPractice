'''
*
**
***
****
*****
'''

i =0
rows = 5
cols = 5
while i < rows:
    j = 0
    while j < cols:
        if i>=j:
            print('*', end='')             #for space end=' '
        else:
            print(' ', end='')
        j =j+1
    print('\n')
    i = i+1

 #flip right then up above pattern  only condn change    (if i<=j)
'''
*****
 ****
  ***
   **
    *
'''

i=0
rows=5
cols=5
while i<rows:
    j=0
    while j<cols:
        if i<=j:
            print('*', end='')
        else:
            print(' ', end='')
        j =j+1
    print('\n')
    i = i+1
