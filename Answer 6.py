def  generate_lyrics(items):
    numString = {1:"first", 2: "second", 3:"third", 4:"forth", 5:"fifth", 6:"sixth",
                 7:"seventh", 8:"eighth", 9:"ninth", 10:"tenth", 11:"eleventh", 12:"twelveth"}
    for index in xrange(1, items + 1):
      if index == 1:
        print "On the 1 day of Christmas my true love sent to me: 1 first item:"
      else:
        print "On the " + str(index) + " day of Chrismtas my true love gave to me:"
        for repeat in range(index, 0, -1):
          if repeat == 1:
            print ("and 1 first time")
          else:
            print str(repeat) + " " + str(numString[repeat]) + " items"
                
