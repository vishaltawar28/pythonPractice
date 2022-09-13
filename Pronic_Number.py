#find pronic number or not
'''
Logic = n(n+1)
'''
num = int(input('enter the number: '))
a = int(num**0.5)
if (a*(a+1))== num:
    print('given number is pronic number')
else:
    print('not a pronic number')