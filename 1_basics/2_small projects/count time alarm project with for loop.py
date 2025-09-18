#count time alarm project with for loop

import time

timer=int(input("inter the time in seconds : "))

for x in range (timer, 0, -1 ):
    seconds=x % 60
    minutes=int(x / 60)%60   #int() here to remove the dicemal of the devition done 
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) 
    
print("wake up !!")