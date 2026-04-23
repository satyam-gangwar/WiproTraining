
#functions
'''def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div():
    pass

#driver
num1=int(input('Enter a number:'))
num2=int(input('Enter a another number:'))

res= add(num1, num2)
print('Add : ', res)
res= sub(num1, num2)
print('Sub : ', res)
res= mul(num1, num2)
print('Mul : ', res)
'''

#Arbitary

'''def add(nums):
    sum=0
    for n in nums:
        sum += n
    return sum

numbers = list()
count = int(input('How many :'))

for _ in range(1, count+1):
    numbers.append(int(input('No. ')))
    print(add(numbers))'''

    #Optional
'''

def add(n1, n2, n3=10):
    return n1 + n2 +n3

#driver
num1=int(input('Enter a number:'))
num2=int(input('Enter a another number:'))

print(add(num1, num2))
print(add(num1,num2,100))
'''
#lambda function

num1=int(input('Enter a number:'))
num2=int(input('Enter a another number:'))

add = lambda n1, n2 : n1+n2

print(add(num1, num2))



