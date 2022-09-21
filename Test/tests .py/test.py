# import xlwings as xw
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 快速入门
# # 这将创建一个新工作簿
# # wb = xw.Book()
# # 连接到打开的文件或当前工作目录中的文件
# wb = xw.Book('dados.xlsx')
# # 实例化 sheet 对象：
# sheet = wb.sheets[0]
# # 读取/写入
# sheet.range('A1').value = 'Foo 1'
# print(sheet.range('A1').value)
# # 范围扩展：
# sheet.range('A2').value = [['Foo 1', 'Foo 2', 'Foo 3'],
#                            [10.0, 20.0, 30.0]]
# print(sheet.range('A2').expand().value)
#
# df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
# sheet.range('A5').value = df
# print(sheet.range('A5').options(pd.DataFrame, expand='table').value)
#
# fig = plt.figure()
# plt.plot([1, 2, 3, 4, 5])
# sheet.pictures.add(fig, name='MyPlot', update=True)
#
# wb.save('dados.xlsx')
# wb.close()

# 读取 Excel

# xw.Range('A1').value = 'something' ?

# app = xw.App()
#
# apbk = app.books['dados.xlsx']
#
# with xw.App() as app:
#     book = app.books['dados.xlsx']


# 1.保存数据
# wb = xw.Book()
# sht = wb.sheets[0]
# info_list = [["'20190001", "已揽收", "凯撒邮局"],
#              ["'20190001", "已发货", "凯撒邮局"],
#              ["'20192288", "已揽收", "麻花镇邮局"],
#              ["'20192288", "已发货", "麻花镇邮局"],
#              ["'20192288", "正在派送", "阿里山"]]
#
# titles = [['包裹号', '状态', '地点']]
# sht.range('a1').value = titles
#
# sht.range('a2').value = info_list
#
# wb.save('dados.xlsx')
#
# wb.close()

# 2.更新数据

# wb = xw.Book('dados.xlsx')

# sht = wb.sheets[0]
#
# first = sht.range('a2').expand('table').value
#
# for i in first:
#     i[0] = str(round(i[0]))
#     first_str.append(i)
# print(first_str)
#
# 求出行数:
# rng = sht.range('b1').expand('table')
# nrows = rng.rows.count
# a = sht.range(f'b1:b{nrows}').value
#
# print(nrows)
# print(a)

# wb.close()


# from tkinter import *
#
#
# # 定义事件函数，必须用event参数
# def show_key(event):
#     # 查看触发事件的按钮
#     s = event.keysym
#     # 将其显示在按钮控件上
#     lb.config(text=s)
#
#
# root = Tk()
# root.config(bg='#87CEEB')
# root.title("C语言中文网")
# root.geometry('450x350+300+200')
# # root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# # 添加一个按钮控件
# lb = Label(root, text='请按键', fg='blue', font=('微软雅黑', 15))
# # 给按钮控件绑定事件，按下任意键，然后调用事件处理函数。注意，此处需要在英文状态下进行输入
# lb.bind('<Return>', show_key)
# # 设置按钮获取焦点
# lb.focus_set()
# lb.pack()
# # 显示窗口
# root.mainloop()


from PIL import Image, ImageTk  # 导入图像处理函数库
import tkinter as tk
from tkinter import filedialog  # 导入文件对话框函数库

# 创建窗口 设定大小并命名
window = tk.Tk()
window.title('图像显示界面')
window.geometry('600x500')
global img_png  # 定义全局变量 图像的
var = tk.StringVar()  # 这时文字变量储存器


# 创建打开图像和显示图像函数
def open_img():
    global img_png
    file_path = filedialog.askopenfilename()
    img_01 = Image.open(file_path)
    img_png = ImageTk.PhotoImage(img_01)
    var.set('已打开')


def show_img():
    global img_png
    var.set('已显示')  # 设置标签的文字为 'you hit me'
    lbl_img = tk.Label(window, image=img_png)
    lbl_img.pack()


# 创建文本窗口，显示当前操作状态
Label_Show = tk.Label(window,
                      textvariable=var,  # 使用 textvariable 替换 text, 因为这个可以变化
                      bg='blue', font=('Arial', 12), width=15, height=2)
Label_Show.pack()
# 创建打开图像按钮
btn_Open = tk.Button(window,
                     text='打开图像',  # 显示在按钮上的文字
                     width=15, height=2,
                     command=open_img)  # 点击按钮式执行的命令
btn_Open.pack()  # 按钮位置
# 创建显示图像按钮
btn_Show = tk.Button(window,
                     text='显示图像',  # 显示在按钮上的文字
                     width=15, height=2,
                     command=show_img)  # 点击按钮式执行的命令
btn_Show.pack()  # 按钮位置

# 运行整体窗口
window.mainloop()
