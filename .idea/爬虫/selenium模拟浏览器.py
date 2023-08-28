import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from io import BytesIO
import gzip
import os
print(os.__file__)

browser = webdriver.Chrome()
browser.get('https://fanyi.baidu.com')
time.sleep(2)
textarea = browser.find_element(By.ID,'baidu_translate_input')
textarea.send_keys('how are you')
time.sleep(2)
# 提取接口的请求信息
get_conver_header = {}
get_conver_url = ""
print(len(browser.requests))
for request in browser.requests:
    print(request.url)
    if "https://fanyi.baidu.com" in request.url:
        get_conver_url = request.url
        for header_key in request.headers:
            get_conver_header[header_key] = request.headers[header_key]
        break
print(get_conver_url)
print(get_conver_header)
rp_body = browser.requests[0].response.body
print(rp_body)
browser.requests
buff = BytesIO(rp_body)
f = gzip.GzipFile(fileobj=buff)
htmls = f.read().decode('utf-8')
print(htmls)
browser.quit()