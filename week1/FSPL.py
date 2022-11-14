from math import pi, log10
d = int(input("Enter a distance "))
f = int(input("Enter a frequence "))

fspl = (4 * pi * d * f)
fer = fspl / 300000000
per = fer  ** 2

fspldb = (20 * log10(d)) + (20 * log10(f)) - 147.55

print(round(per, 3))
print(round(fspldb, 3))