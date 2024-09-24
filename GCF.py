numone=int(input("type a number"))
numtwo=int(input("type another number"))

for y in range(1,min(numone, numtwo) + 1):
  if numtwo % y == 0 and numone % y == 0:
    gcf=y
    
print(gcf)