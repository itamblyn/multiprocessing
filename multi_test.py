import numpy as np
import time
import multiprocessing
from multiprocessing import Pool

HT_factor = 2

# this simulates a python program which takes a few seconds to execute
# it involves generation of many random numbers, an allocating some memory

def counter(seed):
    np.random.seed(seed)
    random_numbers = np.random.rand(2**25)
    average = np.sum(random_numbers)/float(random_numbers.shape[-1])
    return average, seed

# measure the time it takes to complete tasks one at a time using standard techinques
toc = time.time()
ntask=2
for i in range(ntask):
    average = counter(i)
tic = time.time()
print('using ', 1, ' process to complete ', str(ntask), 'tasks')
print(tic-toc, ' seconds')

print('now lets create a lot of tasks, and throw cores at it (i.e. without HT)')
ntask=256

tic = time.time()
seeds = np.arange(ntask)
pool = Pool(processes=multiprocessing.cpu_count()/HT_factor)
print('using ', multiprocessing.cpu_count()/float(HT_factor), ' processes to complete ', ntask, 'tasks')
tic = time.time()
run = pool.map(counter, seeds)
toc = time.time()
print(toc-tic, ' seconds')

print('lets see how HT helps')

tic = time.time()
seeds = np.arange(ntask)
pool = Pool(processes=multiprocessing.cpu_count())
print('using ', multiprocessing.cpu_count(), ' processes to complete ', ntask, 'tasks')
tic = time.time()
run = pool.map(counter, seeds)
toc = time.time()
print(toc-tic, ' seconds')
