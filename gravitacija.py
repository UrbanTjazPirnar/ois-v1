import math



v = float(input("input height: "))

c = 6.674 * math.pow(10, -11)
m = 5.972 * math.pow(10, 24)
r = 6.371 * math.pow(10, 6)


a = (c * m)/((r + v)*(r+v))
print(a)
