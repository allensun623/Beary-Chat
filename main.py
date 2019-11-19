# -*- coding: utf-8 -*-
from detect import gate_news
import amzn

def main():
    amzn.product_info()
    gate_news.detect()

if __name__ == "__main__":
    main()
