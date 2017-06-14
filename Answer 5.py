def maxDifference(a):
  difference = -1
  high = 0
  indexHolder = 0
  for index in range(len(a)):
    if a[index] > high:
      high = a[index]
      indexHolder = index
  for marker in range(indexHolder):
    if (high - a[marker] > difference):
      difference = high - a[marker]
  return difference
