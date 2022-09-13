#find given number is spy number or not
'''
for eg input= 1124
sum = 1+1+2+4 =8 and product = 1*1*2*4 =8
so Sum = Product then oys spy number
'''
n=num = int(input('enter thr number :'))
sum = 0
product = 1
while num>0:
    digit = num%10
    sum = sum + digit                  #logic
    product = product * digit
    num=num//10
if sum==product:
    print(n, 'is spy number')
else:
    print(n, 'is not spy number')



