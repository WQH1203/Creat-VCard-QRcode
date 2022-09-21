# import webbrowser
# import qrcode
# from PIL import Image, ImageTk
#
# # webbrowser.open_new_tab('test.html')
#
# qr = qrcode.QRCode(
#     version=5,
#     error_correction=qrcode.constants.ERROR_CORRECT_M,
#     box_size=5,
#     border=1,
# )
# img = qrcode.make('test.html')
# img.save('../QR_Image/1.png')

# coding:utf-8

# coding:utf-8

# from segno import helpers
#
# qr = helpers.make_mecard(
#     name='Antonio',
#     email='1111111@qq.com',
#     phone='110'
# )
#
# qr.save('pyhui电话.png', scale=10)

# import os

# html = """<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Carta</title>
# <body>
#   <div class="carta_1" style="background:#39cc46; width: 500px; height: 400px;">
#         <section style="position: absolute; left: 50px; top: 25px;">
#             <h2 style="font-size: 50px; margin-bottom: 66px;">%s</h2>
#             <ul>
#                 <li style="list-style: none; line-height: 25px; font-size: 20px;">%s</li>
#             </ul>
#           </section>
#     </div>
# </body>
# </html>"""
#
# datas = ['Table ', '一致']
# f = open('temp.html', 'w', encoding="utf-8")
# f.write(html % (tuple(datas)))
# f.close()
# if os.path.exists('temp.html'):
#     os.remove('temp.html')

# from selenium import webdriver
# import time
# import os.path
# import multiprocessing as mp
#
#
# def webshot(tup):
#     print("当前进程%d已启动" % os.getpid())
#
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')  # 不知为啥只能在无头模式执行才能截全屏
#     options.add_argument('--disable-gpu')
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     # 返回网页的高度的js代码
#     js_height = "return document.body.clientHeight"
#     picname = str(tup[0])
#     link = tup[1]
#     print(link)
#
#     try:
#         driver.get(link)
#         k = 1
#         height = driver.execute_script(js_height)
#         while True:
#             if k * 500 < height:
#                 js_move = "window.scrollTo(0,{})".format(k * 500)
#                 print(js_move)
#                 driver.execute_script(js_move)
#                 time.sleep(0.2)
#                 height = driver.execute_script(js_height)
#                 k += 1
#             else:
#                 break
#         scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#         scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#         driver.set_window_size(scroll_width, scroll_height)
#         driver.get_screenshot_as_file("D:/pics/" + picname)
#         print("Process {} get one pic !!!".format(os.getpid()))
#         driver.quit()
#     except Exception as e:
#         print(picname, e)
#
#
# if __name__ == '__main__':
#     # 首先创建一个保存截图的文件夹
#     filename = "C:/Users/Ruan1203/Desktop/GitHub/PY-porjects/Estagio/Test"
#     if not os.path.isdir(filename):
#         # 判断文件夹是否存在，如果不存在就创建一个
#         os.makedirs(filename)
#
#     # 读取保存url的文件，返回一个列表
#     # 列表中每个元素都是一个元组，文件保存url的格式是：保存为图片的名称, 网页地址。
#     # 例：baidu.png,https://www.baidu.com
#     #     zhihu.png,https://www.zhihu.com
#     with open('urls.txt', 'r') as f:
#         lines = f.readlines()
#     urls = []
#     for line in lines:
#         thelist = line.strip().split(",")
#         if len(thelist) == 2 and thelist[0] and thelist[1]:
#             urls.append((thelist[0], thelist[1]))
#
#     # 创建进程池来多进程执行
#     pool = mp.Pool()
#     pool.map_async(func=webshot, iterable=urls)
#     pool.close()
#     pool.join()

# import base64
# import os
# import time
#
# from selenium import webdriver
# from selenium.common.exceptions import WebDriverException
#
# options = webdriver.ChromeOptions()
# # options.add_argument('--headless') # Chrome最新驱动无效，可以使用firefox或phantomjs
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('window-size=1920x1080')
#
# path = os.getcwd().replace("\\", "/")
# full_path = path + '/templates/test_flask_render.html'
#
# try:
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     driver.get(f'file:///{full_path}')
#     time.sleep(3)
#     driver.get_screenshot_as_file('./images/test-canvas.png')
#     driver.quit()
#     print("截图成功")
# except WebDriverException:
#     print("截图失败")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.python.org/")
# print(driver.title)
# aux = driver.find_element(By.NAME, "q")
# aux.send_keys("python")
# aux.send_keys(Keys.RETURN)
# time.sleep(5)
aux = driver.find_elements(By.CLASS_NAME, "widget-title")
for title in aux:
    print(title.text)
driver.quit()
