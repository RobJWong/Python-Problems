def nonRepeating(s):
  uniqueFlag = True
  position = 1
  if len(s) == 1:
    print s
    return
  for letter in s:
    for index in xrange(position, len(s)):
      #print letter, index, s[index]
      if letter == s[index]:
        uniqueFlag = False
    if uniqueFlag == True:
       print letter
    else:
      position += 1
  #if uniqueFlag == True:
    #return s[len(s) -1]
    
letter = nonRepeating("bab")
