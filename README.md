# Timer
## 1. 方式一 class timer 
便於觀察程式碼各行的執行時間。
* 開始計時(starts timer)：timer.start()
* 建立斷點(break point)：timer.bp()
* 結束計時(ends timer)：timer.end()s

### 使用方式：
```python=
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
```
### Outputs:
```
+-------+---------------------+-----------------+
|   bp  |     record_time     | process_time(s) |
+-------+---------------------+-----------------+
|   1   | 2022-12-02 12:45:11 |        0        |
|   2   | 2022-12-02 12:45:11 |      0.1616     |
|   3   | 2022-12-02 12:45:18 |      6.5473     |
|   4   | 2022-12-02 12:45:19 |      1.0872     |
| total |          -          |      7.7961     |
+-------+---------------------+-----------------+
```


## 2. 方式二 decorator
* 使用裝飾器實作，觀查程序運行時間

### 使用方式二：裝飾器
```
@timer_deco
def dummyLoop(t):
    nb_iter = 13
    for i in range(nb_iter):
        time.sleep(t)

dummyLoop(0.5)
```
### Outputs:
```
開始時間: 2022-12-07 08:58:26
結束時間: 2022-12-07 08:58:33
花費時間: 6.5531 s
```

## 3. Remark 
* 實作中以 time.time() 獲取時間，因此其中包含 sleep。
* 若不需要計算到sleep，可替換成 time.perf_counter 或者 time.process_time。