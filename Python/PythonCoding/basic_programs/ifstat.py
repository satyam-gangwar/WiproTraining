"""
Date: 22-04-26
Desc:learning various if stmt formats
"""
#big 2
'''
num1 = int(input('Enter a number'))
num2 = int(input('Enter another number'))

if num1 == num2 :
    print('Both are equal ')

elif  num1 > num2 :
    print(num1 ,   ' is big. ')
else:
    print(num2, ' is big. ')
'''

#big3

'''num1 = int(input('Enter a number'))
num2 = int(input('Enter another number'))
num3 = int(input('Enter another number'))

if num1 == num2 and num2 == num3:
    print('All values are equal')

elif num1 > num2 and num1 > num3:
    print(num1, 'num1 is biggest ')

elif num2 > num1 and num2 > num3:
    print(num2, 'num2 is biggest ')

elif num3 > num1 and num3 > num1:
    print(num3, 'num3 is biggest ')'''


#weekday

ch = int(input('Enter a number between 1-7'))

match ch:
    case 1:
        print('Monday')
    case 2:
        print('Tue')
    case 3:
        print('Wed')
    case 4:
        print('thu')
    case 5:
        print('fri')
    case 6:
        print('sat')
    case 7:
        print('sun')
    case _:
        print('Invalid choice')


