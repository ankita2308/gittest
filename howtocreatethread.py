import threading
import time
def demo():
    print("threading started \n")
    time.sleep(2)
    print("threading stopped \n")
t1=threading.Thread(target=demo)
t1.start()
