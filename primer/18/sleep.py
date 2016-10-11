from time import sleep,ctime
import _thread

loops =[4,2,11]
def loop(nloop,nsec,lock):
    print(" start loop:",nloop,"at",ctime())
    sleep(nsec)
    print("loop :",nloop, "done at:",ctime())

def main():
    print("start at:", ctime())
    locks = []
    nloops = list(range(len(loops)))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():pass
        
    print(" all done at:" ,ctime())
if __name__ == "__main__":
    main()
