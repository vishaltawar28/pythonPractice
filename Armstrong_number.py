#identify given num is armstrong number or not
#for eg 153 = 1**1+5**5+3**3 = 153
# addition of each digits cube is equal to nimber itself
#num=153
n=num = int(input('enter given number:'))
number_of_digits = len(str(num))
sum =0
while num>0:
    digit = num%10                        #remainder in digit bsically first digit 153%10 = remainder 3
    sum = sum+ digit**number_of_digits     #0+3**3
    num = num//10                          #Quioant 153//10  Q=15 again loop repeat
if n==sum:
    print(n, 'is Armstrong Number')
else:
    print(n, 'is not Armstrong Number')

