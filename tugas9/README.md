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
3|5|4.166|1000|0|122000|240.03|20.831|28.6
4|8|5.386|1000|0|122000|185.65|43.091|22.12
5|10|3.945|1000|0|122000|253.51|39.446|30.2


### Server_thread_http ('127.0.0.1:46000')

**No Test**|**Concurrency level**|**Time taken for test (s)**|**Complete request**|**Failed request**|**Total transferred (bytes)**|**Request per second (#/sec)**|**Time per request (ms)**|**Transfer rate (Kbytes/sec)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
1|1|8.775|1000|0|122000|113.97|8.775|13.58
2|3|9.605|1000|0|122000|104.11|28.816|12.4
3|5|6.402|1000|0|122000|156.2|32.011|18.61
4|8|31.661|1000|0|122000|31.58|253.290|3.76
5|10|11.002|1000|0|122000|90.89|110.023|10.83


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
