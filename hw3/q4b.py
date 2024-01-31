import random
from concurrent.futures import ThreadPoolExecutor

MILLION = 1_000_000
ATTEMPT_CONST = 10 #in millions
successes = 0
def millionAttempts():
    print("starting")
    succ = 0
    for j in range(MILLION):
        rolled6 = 0
        for i in range(12):
            if random.randint(1,6) == 6:
                if rolled6 == 1:
                    succ+=1
                    break
                rolled6+=1

    print("done")
    return succ

with ThreadPoolExecutor() as exec:
    futures = []
    for i in range(ATTEMPT_CONST):
        futures.append(exec.submit(millionAttempts))
    print(sum([f.result() for f in futures])/(ATTEMPT_CONST*MILLION))
        

