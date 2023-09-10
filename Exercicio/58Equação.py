import math 
from math import exp, expm1

xnum1 = float(input("Entrar com 1 valor"))

xnum2 = float(input("Entrar com 1 valor"))

xnum3 = float(input("Entrar com 1 valor"))

x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 *(xnum1 - xnum2) + math.exp(64)/ math.expm1(2.)

print("X =",x)