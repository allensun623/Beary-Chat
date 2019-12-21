import time
from detect.gate import gate
from detect.amazon import amznJSON as amzn
from multiprocessing import Process


AMZN_HOUR = 0
AMZN_MINUTE = 10
AMZN_SECOND = 0
GATE_HOUR = 12
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
    interval_gate = __sleeptime(GATE_HOUR,
                                        GATE_MINUTE,
                                        GATE_SECOND)
    
    interval_amzn = __sleeptime(AMZN_HOUR,
                                    AMZN_MINUTE,
                                    AMZN_SECOND)
    #add two processes
    p1 = Process(target=run_process, 
                args=(gate.product_info, interval_gate, "gate"))
    p2 = Process(target=run_process, 
                args=(amzn.product_info, interval_amzn, "amzn"))
    #run processes
    p1.start()
    p2.start()
    p1.join()
    p2.join()

def main():
    interval_processing()

if __name__ == "__main__":
    main()

