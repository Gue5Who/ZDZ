import time
import numpy as np
from multiprocessing import Process
from multiprocessing import Pool, Array, Lock


def f( a, r, l, i):
    print('Feeling sleepy...')
    time.sleep(1)
    print('Slept for 1 second and had crazy dreams for %s seconds' % a)
    l.acquire()
    r[i]= 1-a
    l.release()
    return 1 - a
if __name__ == '__main__':
    print('Script started')
    N = 20

    N_cpu = 4

    results = Array('f',N)

    lock = Lock()

    t = np.random.rand(N)

    processes = [Process(target = f, args = [t[i], results, lock, i]) for i in range(N)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    #pool = Pool(N_cpu)

    #results = pool.map(f,t)

    print(results[:])
    
    #print('All processes slept for %s seconds and had no dreams for %s.' % (N, np.sum(results)))
    #processes = [Process(target=f, args = [i]) for i in t]

    #for p in processes:
    #    p.start()
    #for p in processes:
    #    p.join()
    #    p.close()
    
    #pool.close()
    
    print('Script finished')