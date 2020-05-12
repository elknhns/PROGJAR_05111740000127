# Tugas 10
## Performance Test LoadBalancer

1. Jalankan async_server.py pada port 9002, 9003, 9004, 9005

![1](link)

2. Jalankan file lb.py, dengan port 44444

![2](link)

3. Akses pada browser, http://localhost:44444/page.html

![3](link)

4. Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian

![3](link)

5. Lakukan performance test seperti pada tugas 9, bandingkan penggunaan load balancer dengan async_server dengan server_thread_http pada folder progjar5
* Jumlah request : 1000
* Concurrency: 1,3,5,8,10

## Hasil Performance Test

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



### Server_async_http with LoadBalancer ('127.0.0.1:44444')

**No Test**|**Concurrency level**|**Time taken for test (s)**|**Complete request**|**Failed request**|**Total transferred (bytes)**|**Request per second (#/sec)**|**Time per request (ms)**|**Transfer rate (Kbytes/sec)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
1|1|b|1000|0|122000|b|b|b
2|3|b|1000|0|122000|b|b|b
3|5|b|1000|0|122000|b|b|b
4|8|b|1000|0|122000|b|b|b
5|10|b|1000|0|122000|b|b|b


## Screenshot hasil run

### Async Server HTTP

![1](link)
![2](link)
![3](link)
![4](link)
![5](link)
