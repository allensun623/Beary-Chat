import time
from detect.gate import gate_news, gate_startup
from detect.amazon import amzn

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
    while True:
        amzn.product_info()
        gate_news.detect()
        gate_startup.detect()
        print("==================================================")
        print("=========Interval for next detection...===========")
        print("==================================================")
        time.sleep(interval_amzn)

def main():
    interval()

if __name__ == "__main__":
    main()

