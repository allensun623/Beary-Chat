import signal
from selenium import webdriver
import os
import time
import pysnooper

@pysnooper.snoop()
def screenshot():
   url = "http://www.nba.com"

   PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
   DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

   driver = webdriver.Chrome(executable_path = DRIVER_BIN)
   try:
      driver.get(url)
       # 截图保存到内存中，后续使用 Pillow 压缩图片
      driver.get_screenshot_as_file("screenshot\\" + ".png")
      
   except:
      return ''
    # 结束 Phantomjs 进程
   finally:
      driver.service.process.send_signal(signal.SIGTERM)
      time.sleep(2)
      driver.quit()

def main():
    screenshot()

if __name__ == "__main__":
    main()