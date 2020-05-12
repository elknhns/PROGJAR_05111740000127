# Tugas 10
## Performance Test LoadBalancer

1. Jalankan async_server.py pada port 9002, 9003, 9004, 9005

  ![1](capture%20async%20with%20load%20balancer/runserver.png)

2. Jalankan file lb.py, dengan port 44444

  ![2](capture%20async%20with%20load%20balancer/run-lb_py.png)

3. Akses pada browser, http://localhost:44444/page.html

  ![3](capture%20async%20with%20load%20balancer/page_html.png)

4. Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian

  ![4](capture%20async%20with%20load%20balancer/request-satu-satu.png)

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
1|1|6.52|1000|0|122000|153.37|6.52|18.27
2|3|7.3|1000|0|122000|136.99|21.9|16.32
3|5|7.546|1000|0|122000|132.52|37.73|15.79
4|8|5.701|1000|0|122000|175.41|45.607|20.9
5|10|6.652|1000|0|122000|150.33|66.521|17.91


## Screenshot hasil run

### Async Server HTTP with LoadBalancer

![1](capture%20async%20with%20load%20balancer/loadbalancer_con_1.png)

![2](capture%20async%20with%20load%20balancer/loadbalancer_con_3.png)

![3](capture%20async%20with%20load%20balancer/loadbalancer_con_5.png)

![4](capture%20async%20with%20load%20balancer/loadbalancer_con_8.png)

![5](capture%20async%20with%20load%20balancer/loadbalancer_con_10.png)
