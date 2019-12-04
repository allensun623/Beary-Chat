# -*- coding: utf-8 -*-

from detect.gate import gate_startup, gate_news

def product_info():  
    #gate news
    gate_news.detect()

    #gate startup  
    gate_startup.detect()
  
def main():
    product_info()

if __name__ == "__main__":
    main()

