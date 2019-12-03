# -*- coding: utf-8 -*-
from detect.gate import gate_news, gate_startup
from detect.amazon import amzn
from detect.sweaters import sweater_data
import send_interval as sil

def main():
    #amzn.product_info()
    #gate_news.detect()
    #gate_startup.detect()
    sil.interval_processing()

if __name__ == "__main__":
    main()
