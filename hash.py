
# Python 3 code to demonstrate the 
# working of MD5 (byte - byte)
 

import hashlib
 
# encoding GeeksforGeeks using md5 hash
# function 
i = 0
ts = 1698387200

while (True):
  data = "timeStamp="+str(ts)+"&key=!QHwF2022Xi1fis!"
  result = hashlib.md5(data.encode())
  res = result.hexdigest()
  print(data)
  print(res)
  i = i +1
  ts = ts + 1
  if res == '6f05a54db3ca503ffaaeffaf621be55b':
  	print("True")
  else:
  	print("False")
      