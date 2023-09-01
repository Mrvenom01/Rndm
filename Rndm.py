import time
from random import randint
for i in range(1,100):
  print('')


space='  '

for i in range(1,1000):
  count=randint(1,99)
  while(count>0):
    space+=' '
    count-=1
  if(i%10==0):
   print(space +'\033[1;31mh\033[1;32ma\033[1;33mp\033[1;34mp\033[1;35my \033[1;36mb\033[1;37mi\033[1;31mr\033[1;32mt\033[1;33mh\033[1;34md\033[1;35ma\033[1;36my \033[1;37mt\033[1;31mo \033[1;32my\033[1;33mo\033[1;34mu🥳❤️')
  elif(i%9==0):
   print(space +'🎊🎊')
  elif(i%8==0):
   print(space +'🎈🎈')
  elif(i%7==0):
   print(space +'🍰🍰')
  elif(i%6==0):
   print(space +'🎂🎂')
  elif(i%5==0):
   print(space +'\033[1;31mh\033[1;32ma\033[1;33mp\033[1;34mp\033[1;35my \033[1;36mb\033[1;37mi\033[1;31mr\033[1;32mt\033[1;33mh\033[1;34md\033[1;35ma\033[1;36my \033[1;31mk\033[1;32mu\033[1;33mt\033[1;34mt\033[1;35mu 🥳❤️')
  elif(i%4==0):
   print(space +'😻😻')
  elif(i%3==0):
   print(space +'🥳🥳')
  elif(i%2==0):
   print(space +'🎉🎉')
  elif(i%1==0):
   print(space +'🎂🎂')

  space= ''
  time.sleep(0.6)
