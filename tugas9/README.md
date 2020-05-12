# Tugas 9
## Performance Test

1. Jalankan kedua model server berikut:
* Server_async_http.py di port 45000
* Server_thread_http.py di port 46000

2. Uji cobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi
* Jumlah request: 1000
* Konkurensi: 1, 3, 5, 8, 10

### Server_async_http ('127.0.0.1:45000')

**No Test**|**Concurrency level**|**Time taken for test (s)**|**Complete request**|**Failed request**|**Total transferred (bytes)**|**Request per second (#/sec)**|**Time per request (ms)**|**Transfer rate (Kbytes/sec)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
1|1|4.203|1000|0|122000|237.91|4.203|28.34
2|3|3.911|1000|0|122000|255.71|11.732|30.47
3|5|b|1000|0|122000|b|b|b
4|8|b|1000|0|122000|b|b|b
5|10|b|1000|0|122000|b|b|b


### Server_thread_http ('127.0.0.1:46000')

**No Test**|**Concurrency level**|**Time taken for test (s)**|**Complete request**|**Failed request**|**Total transferred (bytes)**|**Request per second (#/sec)**|**Time per request (ms)**|**Transfer rate (Kbytes/sec)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
1|1|4.203|1000|0|122000|237.91|4.203|28.34
2|3|b|1000|0|122000|b|b|b
3|5|b|1000|0|122000|b|b|b
4|8|b|1000|0|122000|b|b|b
5|10|b|1000|0|122000|b|b|b


## Screenshot hasil run

### Async Server HTTP

![1](capture%20-%20async%20vs%20thread/async_con_1.png)
![2](capture%20-%20async%20vs%20thread/async_con_3.png)
![3](capture%20-%20async%20vs%20thread/async_con_5.png)
![4](capture%20-%20async%20vs%20thread/async_con_8.png)
![5](capture%20-%20async%20vs%20thread/async_con_10.png)

### Thread Server HTTP

![1](capture%20-%20async%20vs%20thread/thread_con_1.png)
![2](capture%20-%20async%20vs%20thread/thread_con_3.png)
![3](capture%20-%20async%20vs%20thread/thread_con_5.png)
![4](capture%20-%20async%20vs%20thread/thread_con_8.png)
![5](capture%20-%20async%20vs%20thread/thread_con_10.png)
