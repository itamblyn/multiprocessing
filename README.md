# multiprocessing
Some tests and explanations of multiprocessing python

This workbook does some simple tests with the multiprocessing feature of python. In my case, I am running on an i7 Macbook Air (Mid 2012). It has 2 cores + hypertreading. That means that the machine has two processors, but each processor has the ability to quickly switch back and forth between two tasks. On a POSIX machine (e.g. OS X, Linux), the system will see 4 processors (via a utility like top).

In this example, I try a few things to explore the behaviour of increasing the number of processes. Note that the time-to-solution does not go down by 50% for each x2 in processes. From 1 process --> 2, you get approximately a 50% reduction in time. From 2 --> 4 however, the speedup is less. This is because one core with hyperthreading is not equivalent to 2 physical cores.
