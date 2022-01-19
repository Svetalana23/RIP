from contextlib import contextmanager
import time

class Cm_timer_1:
    def __init__(self,before_ms,after_ms):
        self.before_ms=before_ms
        self.after_ms=after_ms
    def __enter__(self):
        print(self.before_ms)
        self.time=time.time()
        return self.time
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
           print(exc_type,exc_val,exc_tb)
        else:
            print("time1:",time.time()-self.time)
            print(self.after_ms)
before_ms = "Сообщение при входе в контекстный менеджер на основе классса"
after_ms= "Сообщение при выходе из контекстного менеджера на основе классса"
with Cm_timer_1(before_ms,after_ms) as cm_object:
    time.sleep(5.5)

@contextmanager
def cm_timer_2():
    t=time.time() # начальное время
    yield t
    print ("time2:",time.time()-t)# текущее время- начальное
with cm_timer_2():
        time.sleep(5.5)





