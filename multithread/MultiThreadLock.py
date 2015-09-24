#coding=utf-8
'''
本示例演示多个线程交替打印递增数字
Python多线程的两种写法：继承Thread类并重写Run方法及直接Thread方法调用函数
通过互斥锁来达到线程安全的目的（print打印非线程安全）
通过Thread类的name属性 获得线程名 实际中使用默认名称即可
研究超时结束线程方法，程序问题不能结束
'''
import threading
from time import sleep
num=1
class ThreadCls(threading.Thread):
    def __init__(self,name=None):
        #threading.Thread.__init__(self)
        super(ThreadCls, self).__init__()
        #name属性改写
        self.name="MyThread1"
    def run(self):
        global num
        #线程结束标志初始False
        self.thread_stop=False
        #t=threading.currentThread()
        while not self.thread_stop:
            for i in range(5):
                #打印前上锁 防止串线
                lk.acquire()
                print self.name+':'+str(num)
                num+=1
                sleep(1)
                #打印完解锁 让其他线程进来
                lk.release()
    def stop(self):
        self.thread_stop=True
def ThreadFun():
    #t是Thread对象 属性name是字符串
    #t=threading.currentThread()
    #print type(t.name)
    global num
    for i in range(5):
        lk.acquire()
        print (threading.currentThread()).name+':'+str(num)
        num+=1
        sleep(1)
        lk.release()
if __name__ == '__main__':
    #‘主函数’定义一个锁
    lk=threading.Lock()
    tcls=ThreadCls()
    #target=函数名不能有() 否则独占整个线程
    tfun1=threading.Thread(target=ThreadFun,name="MyThread2")
    tfun2=threading.Thread(target=ThreadFun,name="MyThread3")
    #线程name属性改写如下
    #调用start方法时必须有() 否则无法启动
    tcls.start()
    tfun1.start()
    tfun2.start()
    '''
    join方法用来等待一个线程结束，如果这个函数没有结束，那么就会阻塞当前运行的程序。
    join([timeout])阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
    调用此方法是被等待线程
    '''
    tcls.join(3)
    '''
    isAlive()方法判断线程是否活动
    如果超时，isAlive()返回True(join()方法不会结束线程，线程仍然活动)
    如果执行结束，run()函数已经返回，isAlive()方法返回的是False
    '''
    if tcls.isAlive():
        #print 'Thread-1 is time out!'
        tcls.stop()