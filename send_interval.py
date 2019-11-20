import time
from detect import gate_news, gate_startup
import amzn

AMZN_HOUR = 0
AMZN_MINUTE = 1
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
        gate_news.detect()
        gate_startup.detect()
        amzn.product_info()
        time.sleep(interval_amzn)

def main():
    interval()

if __name__ == "__main__":
    main()

