import time 
import threading
import os
  
class MyThread(threading.Thread): 
  
    # Thread class with a _stop() method.  
    # The thread itself has to check 
    # regularly for the stopped() condition. 
  
    def __init__(self, *args, **kwargs): 
        super(MyThread, self).__init__(*args, **kwargs) 
        self._stop = threading.Event() 
  
    # function using _stop function 
    def stop(self): 
        self._stop.set() 
  
    def stopped(self): 
        return self._stop.isSet()

    def record_audio(num): 
        """ 
        function to print square of given num 
        """
        os.system('python E:\\Python-Tools\\PyAudioExample.py')
  
    def run(self): 
        while True: 
            if self.stopped(): 
                return
            print("Hello, world!")
            os.system('python E:\\Python-Tools\\PyAudioExample.py')
            time.sleep(1) 
  
t1 = MyThread() 
  
t1.start() 

t1.stop() 
t1.join() 
