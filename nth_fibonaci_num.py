#Nth fibonacci number find
#recusion method
'''
a series of numbers in which each number ( Fibonacci number ) is
 the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
'''
def Fibonacci(n):
    if n<0:
        print('incorrect input')
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(9))
