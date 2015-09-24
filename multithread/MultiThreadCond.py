#coding=utf-8
import threading  
from time import sleep 
L=[]  
class boy(threading.Thread):  
    def __init__(self,cond,name = 'A boy'):  
          
        threading.Thread.__init__(self)  
        self.cond = cond  
        self.name = name  
    def run(self):  
        #不睡这0.1秒女孩线程启动不起来
        sleep(0.1)  
        '''boy start conversation, make sure  
          the girl thread stared before send notify'''  
        self.cond.acquire()  
        print self.name + ':Hello pretty~,I miss you\n'
        sleep(2)  
        self.cond.notify()  
        self.cond.wait()  
        print self.name + ':like moth missing fire\n'
        sleep(2)  
        self.cond.notify()  
        self.cond.wait()  
        print self.name + ':and I bought a gift for you in the list L\n'
        sleep(2)  
        L.append('Porsche')  
        self.cond.notify()  
        self.cond.release()  
          
class girl(threading.Thread):  
    def __init__(self,cond,name = 'A girl'):  
          
        threading.Thread.__init__(self)  
        self.cond = cond  
        self.name = name  
    def run(self):        
        self.cond.acquire()  
        self.cond.wait()  
        print self.name + ':Really, show me how much~\n'
        sleep(2)  
        self.cond.notify()  
        self.cond.wait()  
        print self.name +':you\'re so sweet~\n'
        sleep(2)  
        self.cond.notify()  
        self.cond.wait()  
        print self.name +':wow~~, that\'s '+L.pop()+'---the one I dreamed for so long, I love you\n' 
        sleep(2)   
        self.cond.release()  
if __name__ == '__main__':  
    cond = threading.Condition()  
    husband = boy(cond)  
    wife = girl(cond)  
    husband.start()  
    wife.start()  
    #husband.start()  
    husband.join() #wait untill these two threads end  
    wife.join()  
    print '***End converdarion***\n' 