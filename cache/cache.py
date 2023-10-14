from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import TypeVar
from cache.lock import RWLock

K = TypeVar("K")
V = TypeVar("V")

class Cache(ABC):
    
    @abstractmethod
    def put(self, k: K, v: V): pass 

    @abstractmethod
    def get(self, k: K) -> V: pass 


class DictCache(Cache):

    def __init__(self) -> None:
        super().__init__()
        self._rwlock = RWLock()  
        self.d = dict()

    def put(self, k: K, v: V):
        self._rwlock.acquire_write()
        self.d[k] = v
        self._rwlock.release_write()
    
    def get(self, k: K):
        self._rwlock.acquire_read()
        if k not in self.d:
            raise KeyError(k)
        
        val = self.d[k]
        self._rwlock.release_read()
        return val
    
class Key(tuple):
    __slots__ = []

    def __new__(cls, __iterable: Iterable = ...):
        return super().__new__(__iterable)
    
