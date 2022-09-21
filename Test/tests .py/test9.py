# import mysql.connector
# from openpyxl import workbook, load_workbook
# from openpyxl.utils import get_column_letter
#
# mysql_connection = mysql.connector.connect(host="localhost", user="root", password="sbv2004", database="qr_code_db",autocommit =True)
#
# cursor = mysql_connection.cursor()
# wb = load_workbook('../dados2.xlsx')
# st = wb["Folha2"]
#
# aux = []
# aux2 = []
#
# for row in range(2, 12):
#     for col in range(2, 14):
#         char = get_column_letter(col)
#         aux += [st[char + str(row)].value]
#         if col == 13:
#             aux2.append(aux)
#             aux = []
#
# sql_01 = """
# INSERT INTO pessoa
# (pessoa_Name, pessoa_Telemovel, pessoa_Telefone, pessoa_Email,pessoa_Morada,pessoa_Cidade,pessoa_Distrito, pessoa_Codigo_Postal,pessoa_Pais,pessoa_Empresa,pessoa_Profissao,pessoa_loacal_emp)
# VALUES
# (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)
# """
# # for insert_aux in aux2:
# #     print(insert_aux)
# #     cursor.execute(sql_01, insert_aux)
#
# sql = "DELETE FROM pessoa WHERE pessoa_Pais = 'Portugal'"
#
# # cursor.execute(sql)
#
# mysql_connection.commit()


# from tkinter import ttk
# from tkinter import *
#
# root = Tk()  # 初始框的声明
# columns = ("姓名", "IP地址")
# treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格
#
# treeview.column("姓名", width=100, anchor='center')  # 表示列,不显示
# treeview.column("IP地址", width=300, anchor='center')
#
# treeview.heading("姓名", text="姓名")  # 显示表头
# treeview.heading("IP地址", text="IP地址")
#
# treeview.pack(side=LEFT, fill=BOTH)
#
# name = ['电脑1', '服务器', '笔记本']
# ipcode = ['10.13.71.223', '10.25.61.186', '10.25.11.163']
# for i in range(min(len(name), len(ipcode))):  # 写入数据
#     treeview.insert('', i, values=(name[i], ipcode[i]))
# root.mainloop()  # 进入消息循环

# import tkinter
#
# root = tkinter.Tk()
# root.title("C语言中文网")
# root.geometry('450x180+300+200')
# # 创建一个滚动条控件，默认为垂直方向
# sbar1 = tkinter.Scrollbar(root)
# # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
# sbar1.pack(side='right', fill='y')
# # 创建水平滚动条，默认为水平方向,当拖动窗口时会沿着X轴方向填充
# sbar2 = tkinter.Scrollbar(root, orient='horizontal')
# sbar2.pack(side='bottom', fill="x")
#
# # 创建列表框控件,并添加两个滚动条（分别在垂直和水平方向），使用 set() 进行设置
# mylist = tkinter.Listbox(root, xscrollcommand=sbar2.set, yscrollcommand=sbar1.set)
# for i in range(30):
#     mylist.insert('end', '第' + str(i + 1) + '次:' + 'C语言中文网，网址为：c.biancheng.net' + '\n')
# # 当窗口改变大小时会在X与Y方向填满窗口
# mylist.pack(side="left", fill="both")
# # 使用 command 关联控件的 yview、xview方法
# sbar1.config(command=mylist.yview)
# sbar2.config(command=mylist.xview)
# #  显示主窗口
# root.mainloop()
