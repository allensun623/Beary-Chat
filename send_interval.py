import time
from detect.gate import gate_news, gate_startup
from detect.amazon import amzn
from detect.sweaters import sweater_data
import threading 
import pysnooper

AMZN_HOUR = 1
AMZN_MINUTE = 0
AMZN_SECOND = 0
GATE_HOUR = 0
GATE_MINUTE = 1
GATE_SECOND = 0
"""send message interval"""
def __sleeptime(hr,min,sec):
    return hr*3600 + min*60 + sec

def interval():
    interval_amzn = __sleeptime(
                    AMZN_HOUR,
                    AMZN_MINUTE,
                    AMZN_SECOND
                    ) # interval
    interval_nike = __sleeptime_nike(0, 0, 30)

    while True:
        amzn.product_info()
        gate_news.detect()
        gate_startup.detect()
        sweater_data.product_info()
        print("==================================================")
        print("=========Interval for next detection...===========")
        print("==================================================")
        time.sleep(interval_amzn)

@pysnooper.snoop()
def run_thread(detect_function, detect_interval, detect_name):
    __run_detect = detect_function
    __interval = detect_interval # interval
    while True:
        __run_detect 
        print("detect_name", detect_name)
        print("__interval", __interval)
        print("==================================================")
        print("=========Interval for next detection...===========")
        print("==================================================")
        time.sleep(__interval)

def interval_threading():
    interval_amzn = __sleeptime(0, 0, 45)
    interval_gate = __sleeptime(0, 1, 0)
    t1 = threading.Thread(target=run_thread, 
                            args=(amzn.product_info(), interval_amzn, "amazon"))
    t2 = threading.Thread(target=run_thread, 
                            args=(gate_news.detect(), interval_gate, "gate"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def main():
    interval_threading()

if __name__ == "__main__":
    main()

