import random 

def solution(N):
  binaryNumberTemp = bin(N)
  binaryNumber = binaryNumberTemp[2:]
  startCounter = False
  indexCounter = 0
  highestGap = 0
  print(N)
  print(binaryNumber)
  #print(len(binaryNumber))
  for indexNumber in binaryNumber:
    if (int(indexNumber) == 1):
      if (startCounter == False):
        startCounter = True
      else:
        if (indexCounter > highestGap):
          highestGap = indexCounter
          indexCounter = 0
        else:
          indexCounter = 0
    elif ((int(indexNumber) == 0) & startCounter == True):
      indexCounter += 1
  print (highestGap)

solution(random.randrange(0,10000000))