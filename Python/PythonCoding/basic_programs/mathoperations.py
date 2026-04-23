from mypack.basicshapes import areaofsquare, perimeterofsquare, areaofrectangle
from mypack.circle import areaofcircle, perimeter

radius = int(input('Enter Radius'))

print('Area : ', areaofcircle(rad=radius))
print('Per1 : ', perimeter(rad=radius))

si=int(input('Enter side of sq '))
print('Area : ',areaofsquare(side=si))
print('Per1 : ', perimeterofsquare(side=si))

l = int(input('Enter length'))
b= int(input('Enter breadth'))
print('Area :', areaofrectangle(l,b))