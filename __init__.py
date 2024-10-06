
import time
import multiprocessing

def deposit(balance,lock):
    for i in range(100):
        time.sleep(.01)
        lock.acquire()
        balance.value = balance.value+1
        lock.release()

def withdraw(balance):
    pass

if __name__ == '__main__':
    balance = multiprocessing.Value('i',2000)
    pass