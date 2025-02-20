"""15.1 Use multiprocessing to create three separate processes. 
Make each one wait a random number of seconds between zero and one, 
print the current time, and then exit."""

import multiprocessing as mp
import os
import random
import time
from datetime import datetime



def looper(who):
    rand_num = random.random()
    time.sleep(rand_num)
    the_time = datetime.now()    
    print(f"I am {who} with id {os.getpid()} and the time is {the_time.time()}")

def run_processes():
    # An array to keep track of the process objects.
    processes = []
    for i in range(3):
        p = mp.Process(target=looper, args=(f"process {i+1}",))
        #This adds the process to the array.
        processes.append(p)
        p.start()

    for p in processes:
        # Waiting for each process to complete.
        p.join()

if __name__ == '__main__':
    run_processes()
