# -*- coding: utf-8 -*-
from detect import gate_news, gate_startup
import amzn

def main():
    amzn.product_info()
    gate_news.detect()
    gate_startup.detect()

if __name__ == "__main__":
    main()
