# import imgkit
#
#
# # 将HTML文件导出为图片
#
# def html_to_png(html_path, pdf_path='.\\pdf_new.pdf', html_encoding='UTF-8', path_wkpdf='../wkhtmltopdf/bin/wkhtmltoimage.exe'):
#     """
#     将HTML文件导出为图片
#
#     :param html_path:str类型，目标HTML文件的路径，可以是一个路径，也可以是多个路径，以list方式传入路径；或者一个或者多个网址；或者为一个字符串
#
#     :param pdf_path:str类型，需要导出的图片文件的路径
#
#     :param html_encoding:str类型，html的编码格式，具体要看html页面到底是以什么编码格式保存的
#
#     :param path_wkpdf:str类型，path_wkpdf = r'.\Tools\wwkhtmltoimage.exe'  # 工具路径
#     :return:
#     """
#     cfg = imgkit.config(wkhtmltoimage=path_wkpdf)
#     options = {
#         "encoding": html_encoding  # 这个具体要看html页面到底是以什么编码格式保存的
#     }
#
#     if 'http' in str(html_path) and ('html' not in str(html_path) or 'HTML' not in str(html_path)):  # 判断是否为非网址
#         # 从url获取html，再转为pdf
#         print('http=>png')
#         # pdfkit.from_url('https://httpbin.org/ip', 'ip.png', options=options, configuration=cfg) pdfkit.from_url([
#         # 'https://httpbin.org/ip', 'https://httpbin.org/ip'], 'ip.png', options=options,configuration=cfg)  # 传入列表
#         imgkit.from_url(html_path, pdf_path, options=options, config=cfg)
#
#     elif 'html' in str(html_path) or 'HTML' in str(html_path):  # 判断是否为HTML文件
#         # 将html文件转为pdf
#         print('html,str=>png')
#         # pdfkit.from_file(r'./helloworld.html', 'helloworld.png',options=options,  configuration=cfg)
#         imgkit.from_file(html_path, pdf_path, options=options, config=cfg)
#
#     elif isinstance(html_path, list) and ('html' in str(html_path) or 'HTML' in str(html_path)):  # 判断html目标是否为list,
#         # 如：[r'./helloworld.html', r'./111.html', r'./222.html']
#         print('html,list=>png')
#         imgkit.from_file(html_path, pdf_path, options=options, config=cfg)  # 传入列表
#
#     else:
#         # 将字符串转为pdf
#         print('from_string=>png')
#         imgkit.from_string(html_path, pdf_path, options=options, config=cfg)
#
#
# html_to_png("temp.html")

# import imgkit
#
# path_wkimg = r'wkhtmltopdf/bin/wkhtmltoimage.exe'  # 工具路径
# cfg = imgkit.config(wkhtmltoimage=path_wkimg)
# # 1、将html文件转为图片
# imgkit.from_file(r'HTML/test.html', 'test.png', config=cfg)
# 2、从url获取html，再转为图片
# imgkit.from_url('https://www.google.com/', 'google.png', config=cfg)
# 3、将字符串转为图片
# imgkit.from_string('Hello!', 'hello.png', config=cfg)


# import pdfkit
#
# path_wkpdf = r'../wkhtmltopdf/bin/wkhtmltopdf.exe'  # 工具路径
# cfg = pdfkit.configuration(wkhtmltopdf=path_wkpdf)
#
# # 1、将html文件转为pdf
# pdfkit.from_file(r'test.html', 'helloworld.pdf', configuration=cfg)
# pdfkit.from_file([r'./helloworld.html', r'./111.html', r'./222.html'], 'helloworld.pdf', configuration=cfg)  # 传入列表
#
# # 2、从url获取html，再转为pdf
# pdfkit.from_url('https://httpbin.org/ip', 'ip.pdf', configuration=cfg)
# pdfkit.from_url(['https://httpbin.org/ip','https://httpbin.org/ip'], 'ip.pdf', configuration=cfg)  # 传入列表
#
# # 3、将字符串转为pdf
# pdfkit.from_string('Hello!','hello.pdf', configuration=cfg)


# from PIL import Image
# import os
#
# '''
# 保存图片到另一个文件夹
# '''
# # 保存图片到test_result文件夹下，文件名字为hello.jpg
# image = Image.open("../SB-V.png")
# img_name = 'hello'
# image.save(os.path.join("../IMG/", img_name + ".png"))

# from tkinter import *
# import tkinter.messagebox
#
# # 创建主窗口
# win = Tk()
# win.config(bg='#87CEEB')
# win.title("C语言中文网")
# win.geometry('450x350+300+200')
#
#
# # win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
#
# # 绑定一个执行函数，当点击菜单项的时候会显示一个消息对话框
# def menu_command():
#     tkinter.messagebox.showinfo("主菜单栏", "你正在使用主菜单栏")
#
#
# # 创建一个主目录菜单，也被称为顶级菜单
# main_menu = Menu(win)
# # 新增命令菜单项，使用 add_command() 实现
# main_menu.add_command(label="文件", command=menu_command)
# main_menu.add_command(label="编辑", command=menu_command)
# main_menu.add_command(label="格式", command=menu_command)
# main_menu.add_command(label="查看", command=menu_command)
# main_menu.add_command(label="帮助", command=menu_command)
# # 显示菜单
# win.config(menu=main_menu)
# win.mainloop()


# 创建一个下拉式菜单
# from tkinter import *
# import tkinter.messagebox
#
# # 创建主窗口
# win = Tk()
# win.config(bg='#87CEEB')
# win.title("C语言中文网")
# win.geometry('450x350+300+200')
# # win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
#
#
# # 创建一个执行函数，点击下拉菜单中命令时执行
# def menuCommand():
#     tkinter.messagebox.showinfo("下拉菜单", "您正在使用下拉菜单功能")
#
#
# # 创建主目录菜单（顶级菜单）
# mainmenu = Menu(win)
#
# # 在顶级菜单上新增"文件"菜单的子菜单，同时不添加分割线
# filemenu = Menu(mainmenu, tearoff=False)
#
# # 新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
# filemenu.add_command(label="新建", command=menuCommand, accelerator="Ctrl+N")
# filemenu.add_command(label="打开", command=menuCommand, accelerator="Ctrl+O")
# filemenu.add_command(label="保存", command=menuCommand, accelerator="Ctrl+S")
# # 添加一条分割线
# filemenu.add_separator()
# filemenu.add_command(label="退出", command=win.quit)
# # 在主目录菜单上新增"文件"选项，并通过menu参数与下拉菜单绑定
# mainmenu.add_cascade(label="文件", menu=filemenu)
#
# # 将主菜单设置在窗口上
# win.config(menu=mainmenu)
# # 绑定键盘事件，按下键盘上的相应的键时都会触发执行函数
# win.bind("<Control-n>", menuCommand)
# win.bind("<Control-N>", menuCommand)
# win.bind("<Control-o>", menuCommand)
# win.bind("<Control-O>", menuCommand)
# win.bind("<Control-s>", menuCommand)
# win.bind("<Control-S>", menuCommand)
# # 显示主窗口
# win.mainloop()


