# -*- coding: utf-8 -*-
from detect import amzn_calculator, amzn_oil_filter, gate_news

def main():
    amzn_calculator.detect()
    amzn_oil_filter.detect()
    gate_news.detect()

if __name__ == "__main__":
    main()
