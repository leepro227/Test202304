import threading
import time
import requests
data_list  = []

class myThread(threading.Thread):
    def __init__(self, arg,name):
        threading.Thread.__init__(self) # 这2种方法都可以使用
        #super(myThread, self).__init__()
        self.arg = arg
        self.name = name

    def run(self):  # 这个函数定义每个线程要执行的代码，可以嵌套函数
        self.action()

    def action(self):
        headerss={}
        res_data = requests.get(url=self.arg,headers=headerss)
        try:
            if res_data.status_code == 200:
                for data in  res_data.json():
                    data_list.append(data['email'])
            else:
                print('请求错误，status_code：{},请求地址：{}'.format(res_data.status_code,self.arg))
        except Exception as e:
            print('请求错误地址：{}'.format(self.arg))
            print('错误信息：{}'.format(e))



if __name__ == "__main__":
    start = time.time()
    url_list = []
    new_list=[]
    for x in range(100):
        req_url='https://jsonplaceholder.typicode.com/posts/{}/comments'.format(x+1)
        url_list.append(req_url)

    # 虚拟线程做并发抓取任务
    max_connections = 5
    pool_sema = threading.BoundedSemaphore(max_connections)
    thread_list=[]
    for urls in url_list:
        a = myThread(urls,urls)
        thread_list.append(a)

    for a in thread_list:
        a.start()

    for a in thread_list:
        a.join()
        end = time.time()
    end1 = time.time()
    print('全部时间：{}'.format(end1 - start))
    print('获取的Email数量:{}'.format(len(data_list)))
    print('获取的Email:{}'.format(data_list))
