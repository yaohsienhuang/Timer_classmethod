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

if __name__ == '__main__':

    #使用方法一
    def dummyLoop(t):
        nb_iter = 13
        for i in range(nb_iter):
            time.sleep(t)

    timer.start()
    dummyLoop(0.01)
    timer.bp()
    dummyLoop(0.5)
    timer.bp()
    dummyLoop(0.08)
    timer.end()
    
    #使用方法二
    @timer_deco
    def dummyLoop(t):
        nb_iter = 13
        for i in range(nb_iter):
            time.sleep(t)
            
    dummyLoop(0.5)