import time
from detect.gate import gate_news, gate_startup
from detect.amazon import amzn
from detect.sweaters import sweater_data
from multiprocessing import Process
import pysnooper

AMZN_HOUR = 1
AMZN_MINUTE = 0
AMZN_SECOND = 0
GATE_HOUR = 1
GATE_MINUTE = 0
GATE_SECOND = 0
"""send message interval"""
def __sleeptime(hr,min,sec):
    return hr*3600 + min*60 + sec

def run_process(detect_function, detect_interval, detect_name):
    while True:
        detect_function() #run detection function
        print("Run function: ", detect_name)
        print("==================================================")
        print("=========Interval for next detection...===========")
        print("==================================================")
        time.sleep(detect_interval)

def interval_processing():
#multiple processes   
    #interval timer
    interval_gate_startup = __sleeptime(GATE_HOUR,
                                        GATE_MINUTE,
                                        GATE_SECOND)
    interval_gate_news = __sleeptime(GATE_HOUR,
                                    GATE_MINUTE,
                                    GATE_SECOND)
    #add two processes
    p1 = Process(target=run_process, 
                args=(gate_startup.detect, interval_gate_startup, "gate_startup"))
    p2 = Process(target=run_process, 
                args=(gate_news.detect, interval_gate_news, "gate_news"))
    #run processes
    p1.start()
    p2.start()
    p1.join()
    p2.join()

def main():
    interval_processing()

if __name__ == "__main__":
    main()

