# import mysql.connector as myconect
#
# conn = myconect.connect(host="localhost", user="Antonio", password="20031203zhijie", database="qr_code_db")
# cursor = conn.cursor()
#
# fin = open("1.jpg", 'rb')  # 'rb'加上才能将图片读取为二进制
# img = fin.read()  # 将二进制数据读取到img中
# fin.close()
#
# sql2 = "UPDATE pessoa SET pessoa_qrcode = %s WHERE pessoa_Id = '%s'"
# args = (img, 14)  # 对应表格的数据
# # cursor.execute(sql2, args)
# # conn.commit()
#
# # cursor.execute("SELECT pessoa_qrcode FROM pessoa WHERE pessoa_Id = '14' ")
# # rows_aux = cursor.fetchone()
# # fout = open('test_new.jpg', 'wb')
# # fout.write(rows_aux[0])
#
# # fout.close()
# cursor.close()
#
#
# conn.close()
#
#
from tkinter import *


# 定义事件函数，必须用event参数
def show_key(event):
    # 查看触发事件的按钮
    s = event.keysym
    # 将其显示在按钮控件上
    btn_Clear.config(text=s)


root = Tk()
root.config(bg='#87CEEB')
root.title("C语言中文网")
root.geometry('450x350+300+200')
# 添加一个按钮控件
btn_Clear = Button(root, command=show_key)
# 给按钮控件绑定事件，按下任意键，然后调用事件处理函数。注意，此处需要在英文状态下进行输入
btn_Clear.bind('<Return>', show_key)
# 设置按钮获取焦点
btn_Clear.focus_set()
btn_Clear.pack()
# 显示窗口
root.mainloop()
