# -*- coding: utf-8 -*-
from detect.gate import gate_news, gate_startup
from detect.amazon import amzn
from detect.sweaters import sweater_data

def main():
    amzn.product_info()
    gate_news.detect()
    gate_startup.detect()

if __name__ == "__main__":
    main()
