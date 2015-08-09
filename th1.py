__author__ = 'rohit'

import threading

class Thread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        a=threading.currentThread().name




        if(a=="Thread-1"):
            print "1"

        if(a=="Thread-2"):
            print "2"

c=Thread1()
d=Thread1()
c.start()
d.start()
