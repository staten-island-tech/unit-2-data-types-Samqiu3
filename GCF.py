numone=int(input("type a number"))
numtwo=int(input("type another number"))
for y in range (1,numone + 1):
  if numtwo % y == 0 and numone % y == 0:
    print(y)
  
  