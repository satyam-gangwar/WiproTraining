
# natural number
'''
num = int(input('Enter a number'))
sum = 0
for i in range(1, num+1):
    sum=sum + i**2
    print('Sum of squares of nat num', sum)
'''

#print * for n times
num = int(input('Enter how many *'))
for _ in range(1, num+1):
    print('*', '&', sep='@@@@',end='----')