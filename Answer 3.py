import os 
                                      
for sChild in os.listdir(os.path.curdir):                
    sChildPath = os.path.join(os.path.curdir,sChild)
    if os.path.isdir(sChildPath):
        print (os.listdir(sChildPath))
    else:
        print(sChildPath)