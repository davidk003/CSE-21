import random
from concurrent.futures import ThreadPoolExecutor

MILLION = 1_000_000
ATTEMPT_CONST = 10 #in millions
successes = 0
def millionAttempts():
    print("starting")
    succ = 0
    for i in range(MILLION):
        for i in range(6):
            if random.randint(1,6) == 6:
                succ+=1
                break
    print("done")
    return succ

with ThreadPoolExecutor() as exec:
    futures = []
    for i in range(ATTEMPT_CONST):
        futures.append(exec.submit(millionAttempts))
    print(sum([f.result() for f in futures])/(ATTEMPT_CONST*MILLION))
        

