from tkinter import *



# wb = load_workbook('dados.xlsx')




root = Tk()
root.title('carta de pessoa')
# root.geometry('1500x1000')
root.iconbitmap('radar.ico')
root["background"] = "yellow"
root.resizable(0,0)
# text = Label(root, text="identidade", bg="white", fg="red", font=('Times', 20, 'bold italic'))
#
# text.place(x=40, y=40, width=125, height=30)

Label(root, text="Nome").grid(row=0, sticky="w")
entry01 = Entry(root)

entry01.grid(row=0, column=1)

root.mainloop()

