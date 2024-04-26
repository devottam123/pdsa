# Timer Object

import time
class Timer:
    def __init__(self):
        self._start_time=0
        self._elapsed_time=0

    def start(self):
        self._start_time=time.perf_counter()

    def stop(self):
        self._elapsed_time=time.perf_counter() - self._start

    def elapsed(self):
        return(self._elapsed_time)
    
# Python executes 10^7 operations per second