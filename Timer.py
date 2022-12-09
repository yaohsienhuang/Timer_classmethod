import time
from prettytable import PrettyTable

class timer():
    timer=[]
    
    @classmethod
    def start(cls):
        cls.timer=[]
        cls.timer.append(time.time())
    
    @classmethod
    def bp(cls):
        cls.timer.append(time.time())
        
    @classmethod
    def end(cls):
        cls.timer.append(time.time())
        print('totol= %s bp'%len(cls.timer))
        my_table = PrettyTable()
        my_table.field_names = ["bp",'record_time',"process_time(s)"]
        for i in range(len(cls.timer)):
            process_time=round(cls.timer[i]-cls.timer[i-1],4) if i!=0 else 0
            my_table.add_row([
                i+1,
                time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(cls.timer[i])),
                process_time
            ])
            
        my_table.add_row(['total','-',round(cls.timer[-1]-cls.timer[0],4)])
        print(my_table)
        cls.timer=[]

def timer_deco(func):
    def inner(*args,**kwargs):
        t1=time.time()
        print(f'開始時間: {time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(t1))}')
        result=func(*args,**kwargs)
        t2=time.time()
        print(f'結束時間: {time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(t2))}')
        print(f'花費時間: {round(t2-t1,4)} s')
        return result
    return inner

class call_timer:
    def __init__(self,func):
        self.func=func
        
    def __call__(self,*args,**kwargs):
        t1=time.time()
        print(f'開始時間: {time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(t1))}')
        result=self.func(*args,**kwargs)
        t2=time.time()
        print(f'結束時間: {time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(t2))}')
        print(f'花費時間: {round(t2-t1,4)} s')
        return result


class timer_context:
    def __init__(self):
        self.elapsed=0
        
    def __enter__(self):
        self.t1=time.time()
        print(f'開始時間: {time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(self.t1))}')
        return self
        
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.t2=time.time()
        self.elapsed=round(self.t2-self.t1,4)
        print(f'結束時間: {time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(self.t2))}')
        print(f'花費時間: {round(self.elapsed,4)} s')
        return False

if __name__ == '__main__':

    #使用方法一
    def dummyLoop(t):
        nb_iter = 13
        for i in range(nb_iter):
            time.sleep(t)

    timer.start()
    dummyLoop(0.01)
    timer.bp()
    dummyLoop(0.05)
    timer.bp()
    dummyLoop(0.08)
    timer.end()
    
    #使用方法二
    @timer_deco
    def dummyLoop2(t):
        nb_iter = 13
        for i in range(nb_iter):
            time.sleep(t)
    
    dummyLoop2(0.5)
    
    # 使用方式三
    @call_timer
    def dummyLoop3(t):
        nb_iter = 13
        for i in range(nb_iter):
            time.sleep(t)
        
    dummyLoop3(0.5)
    
    # 使用方式四
    with timer_context() as timer:
        dummyLoop(0.5)