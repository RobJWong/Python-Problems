def solution(A):
    # write your code in Python 2.7
    lengthArray = len(A)
    spliceLeft= [] 
    spliceRight = []
    sumLeft = 0
    sumRight = 0
    equalIndex = []
    for indexNumber in range(0, lengthArray):
        sumLeft= sum(A[0:indexNumber])
        sumRight = sum(A[indexNumber+1:lengthArray])
        print(sumLeft,sumRight)
        if indexNumber == 0:
          sumLeft = 0
        if indexNumber == lengthArray - 1:
          sumRight = 0
        if sumLeft == sumRight:
          equalIndex.append(indexNumber)
    print (equalIndex)
    if not equalIndex:
        print ("-1")
    pass

solution([4,4,2,2])