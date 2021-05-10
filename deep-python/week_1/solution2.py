import math
import sys 
a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

discr = b ** 2 - 4 * a * c

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(int(x1))
    print(int(x2))
else:
    x = -b / (2 * a)
    print(int(x))
