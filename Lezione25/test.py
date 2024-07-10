import time

import multiprocessing

def sleepy():
    print(f"Sono nella funzione")
    time.sleep(1)
    print(f"Sto uscendo ddalla funzione")

if __name__ == "__main__":
    tic: float = time.time()

    t1 = multiprocessing.Process(target = sleepy)
    t2 = multiprocessing.Process(target = sleepy)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    toc : float = time.time()

    time_elapsed: float = toc - tic
    
    print(f"{time_elapsed=}")

