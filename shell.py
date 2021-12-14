import time
import multiprocessing
import gc

time.sleep(1)
print("starting RPIB ...")

proc = 0
gap = 1800

time.sleep(2)

while proc< 100000000: # 18 MONTHS @ 1800
    exec(open("rpib_CORE.py").read())

    def main():
        pool = multiprocessing.Pool(processes=10)
        while 1:
            pool.apply_async(process)
            gc.collect()
        pool.close()
        pool.join()

    time.sleep(gap)