import signal

from selenium import webdriver

def screenshot():
    driver = webdriver.PhantomJS(executable_path='Complete path/to/phantomjs')
    # 设置加载页面超时时间
    driver.set_page_load_timeout(12)
    # 设置窗口大小
    driver.set_window_size(1024, 768)

    try:
       driver.get(url)
       # 截图保存到内存中，后续使用 Pillow 压缩图片
       origin_png = self.driver.get_screenshot_as_png()
    except:
       return ''
    # 结束 Phantomjs 进程
    finally:
       driver.service.process.send_signal(signal.SIGTERM)
       driver.quit()

def main():
    screenshot()

if __name__ == "__main__":
    main()