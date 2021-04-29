import random
from statistics import mean
from statistics import variance

# X is sleeping time
# P is probability of sleeping

x1 = random.randint(0,10)
p1 = random.random()
mean1 = x1*p1

x2 = random.randint(0,10)
p2 = random.random()
mean2 = x2*p2

x3 = random.randint(0,10)
p3 = random.random()
mean3 = x3*p3


x4 = random.randint(0,10)
p4 = random.random()
mean4 = x4*p4

x5 = random.randint(0,10)
p5 = random.random()
mean5 = x5*p5

x6 = random.randint(0,10)
p6 = random.random()
mean6 = x6*p6

x7 = random.randint(0,10)
p7 = random.random()
mean7 = x7*p7

x8 = random.randint(0,10)
p8 = random.random()
mean8 = x8*p8

x9 = random.randint(0,10)
p9 = random.random()
mean9 = x9*p9

x10 = random.randint(0,10)
p10 = random.random()
mean10 = x10*p10



print("X1:",x1,"P1:",p1,"Mean: ",mean1)
print("X2:",x2,"P2:",p2,"Mean: ",mean2)
print("X3:",x3,"P3:",p3,"Mean: ",mean3)
print("X4:",x4,"P4:",p4,"Mean: ",mean4)
print("X5:",x5,"P5:",p5,"Mean: ",mean5)
print("X6:",x6,"P6:",p6,"Mean: ",mean6)
print("X7:",x7,"P7:",p7,"Mean: ",mean7)
print("X8:",x8,"P8:",p8,"Mean: ",mean8)
print("X9:",x9,"P9:",p9,"Mean: ",mean9)
print("X10:",x10,"P10:",p10,"Mean: ",mean10)

total_mean = mean1+mean2+mean3+mean4+mean5+mean6+mean7+mean8+mean9+mean10
print(total_mean/10)
print(variance())









