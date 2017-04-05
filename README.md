# ClusterPool

Provides a map function which works with the SLURM supercomputer scheduler and can be extended to others.  Also works on "normal" computers, mainly for testing purposes.  (see examples/testfile_primes.py)

A ClusterPool object is an object which gives you a map function.  You tell what kind of architecture the ClusterPool exists on (currently only "SLURM" and "normal") and it creates a dispatcher object which keeps track of the objects which need calculating, saves them to disk and collects them when they are done being calculated.

These objects are calculated by "Trawler" objects which get spun to life by the dispatcher and are given a directory full of pickled python objects.  The Trawlers then randomly pick an object and throw up a sempahore on the filesystem to tell the other Trawlers they are working on that object.  They load the object and the run object.calculate() (Note that currently the ClusterPool package can ONLY handle calling functions called calculate which take no arguments)
