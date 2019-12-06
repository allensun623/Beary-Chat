# -*- coding: utf-8 -*-
from detect.gate import gate_news, gate_startup
from detect.amazon import amzn
from detect.sweaters import sweater_data
import send_interval as sil

def main():
    #gate_news.detect()
    #gate_startup.detect()
    amzn.product_info()
    #sil.interval_processing()

if __name__ == "__main__":
    main()
