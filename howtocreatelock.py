import threading
import time
tl=threading.Lock()
def timer(name,delay,repeat):
    print('timer'+name+'started lock\n')
    tl.acquire()
    print(name+'acquire the lock\n')
    while repeat>0:
        time.sleep(delay)
        repeat-=1
    print('timer'+name+'release the lock\n')
    tl.release()
    print(name+'completed\n')
t1=threading.Thread(target=timer,args=('timer1',2,5))
t1.start()
