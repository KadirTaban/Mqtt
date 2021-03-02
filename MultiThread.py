import time
import threading


def function_1():
    for i in range(1,31):
        print("CAM1 {}".format(i),end="\n")
def function_2():
    for A in range(1,31):
        print("CAM2 {}".format(A),end="\n")


t1=threading.Thread(target=function_1)
t2=threading.Thread(target=function_2)

t2.start()
t1.start()


s