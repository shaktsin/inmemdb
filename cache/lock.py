import threading

class RWLock:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._wlock = threading.Lock()
        self._readers = 0 

    def acquire_read(self):
        self._lock.acquire()
        self._readers += 1
        if self._readers == 1:
            self._wlock.acquire()
        self._lock.release()

    def release_read(self):
        self._lock.acquire()
        self._readers -= 1
        if self._readers == 0:
            self._wlock.release()
        self._lock.release()

    def acquire_write(self):
        self._wlock.acquire()

    def release_write(self):
        self._wlock.release()