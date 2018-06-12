import numpy as np
import time
import multiprocessing
from multiprocessing import Pool


# this simulates a python program which takes a few seconds to execute
# it involves generation of many random numbers, an allocating some memory

def counter(seed):
    np.random.seed(seed)
    random_numbers = np.random.rand(100000000)
    average = np.sum(random_numbers)/float(random_numbers.shape[-1])
    return average, seed

# measure the time it takes to complete tasks one at a time using standard techinques
toc = time.time()
for i in range(2):
    average = counter(i)
tic = time.time()
print tic-toc, ' seconds'

print 'now lets create a lot of tasks, and throw cores at it (i.e. without HT)'

tic = time.time()
seeds = np.arange(40)
pool = Pool(processes=multiprocessing.cpu_count()/2)
print 'using ', multiprocessing.cpu_count()/2, ' processes'
tic = time.time()
run = pool.map(counter, seeds)
toc = time.time()
print toc-tic, ' seconds'

print 'lets see how HT helps'

tic = time.time()
seeds = np.arange(40)
pool = Pool(processes=multiprocessing.cpu_count())
print 'using ', multiprocessing.cpu_count(), ' processes'
tic = time.time()
run = pool.map(counter, seeds)
toc = time.time()
print toc-tic, ' seconds'
