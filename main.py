# -*- coding: utf-8 -*-
from detect.gate import gate_news, gate_startup
from detect.amazon import amzn

def main():
    amzn.product_info()
    gate_news.detect()
    gate_startup.detect()

if __name__ == "__main__":
    main()
