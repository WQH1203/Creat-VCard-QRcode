import os
import qrcode
import re
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import mysql.connector as myconect
from PIL import Image, ImageTk


def clear():
    global photo_01
    lbl_Id_V['text'] = ''
    txt_Name.delete("1.0", "end")
    txt_tele.delete("1.0", "end")
    txt_telf.delete("1.0", "end")
    txt_email.delete("1.0", "end")
    txt_morada.delete("1.0", "end")
    txt_cidade.delete("1.0", "end")
    txt_distrito.delete("1.0", "end")
    txt_cod_postal.delete("1.0", "end")
    txt_pais.delete("1.0", "end")
    txt_empr.delete("1.0", "end")
    txt_ocup.delete("1.0", "end")
    txt_local.delete("1.0", "end")
    lbl_img1['image'] = photo_01


def get_txt(aux):
    name = aux.get("0.0", "end").replace("\n", "").replace("\r", "")
    return name


def messagebox(title_aux, mensagem):
    tkinter.messagebox.showwarning(title_aux, mensagem)


def ver_email():
    str_aux = r"^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+@\w+[.]\w{2,4}$"
    if not (re.match(str_aux, get_txt(txt_email))):
        return 0
    else:
        return 1


def sort_column(tabela, coluna, reverse):
    l = [(tabela.set(k, coluna).upper(), k) for k in tabela.get_children('')]
    if coluna == 'Id':
        l.sort(key=lambda t: int(t[0]), reverse=reverse)
    else:
        l.sort(key=lambda t: t[0], reverse=reverse)
    for index, (val, k) in enumerate(l):
        tabela.move(k, '', index)
    tabela.heading(coluna, command=lambda: sort_column(tabela, coluna, not reverse))


def mostrar(row):
    clear()
    global number_aux, photo
    number_aux = row[0]
    lbl_Id_V['text'] = row[0]
    txt_Name.insert(INSERT, row[1])
    txt_tele.insert(INSERT, row[2])
    txt_telf.insert(INSERT, row[3])
    txt_email.insert(INSERT, row[4])
    txt_morada.insert(INSERT, row[5])
    txt_cidade.insert(INSERT, row[6])
    txt_distrito.insert(INSERT, row[7])
    txt_cod_postal.insert(INSERT, row[8])
    txt_pais.insert(INSERT, row[9])
    txt_empr.insert(INSERT, row[10])
    txt_ocup.insert(INSERT, row[11])
    txt_local.insert(INSERT, row[12])
    ver_img = os.path.exists('./IMG/' + str(lbl_Id_V['text']) + ".png")
    if ver_img:
        img = Image.open('./IMG/%s.png' % str(lbl_Id_V['text']))
        photo = ImageTk.PhotoImage(img)
        lbl_img1['image'] = photo


def back_next(aux):
    global indice_aux
    if aux == "button1":
        if indice_aux <= 0:
            btn_back["state"] = DISABLED
        else:
            indice_aux -= 1
            btn_next["state"] = ACTIVE
            btn_back["state"] = DISABLED if indice_aux <= 0 else ACTIVE
    elif aux == "button2":
        if indice_aux >= len(rows_aux) - 1:
            btn_next["state"] = DISABLED
        else:
            indice_aux += 1
            btn_back["state"] = ACTIVE
            btn_next["state"] = DISABLED if indice_aux >= len(rows_aux) - 1 else ACTIVE
    mostrar(rows_aux[indice_aux])


def porcura():
    try:
        clear()
        global rows_aux, indice_aux
        indice_aux = 0
        procurador_aux = procurador % ('*', 'pessoa',
                                       'convert(pessoa_Id,CHAR(50)) = "' + numEty.get() +
                                       '" or pessoa_name like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Telemovel like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Telefone like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Email like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Morada like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Cidade like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Distrito like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Codigo_Postal like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Pais like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Empresa like "%' + numEty.get() + '%"' +
                                       ' or pessoa_Profissao like "%' + numEty.get() + '%"' +
                                       ' or pessoa_loacal_emp like "%' + numEty.get() + '%"')
        cursor.execute(procurador_aux)
        rows_aux = cursor.fetchall()
        mostrar(rows_aux[indice_aux])
        if indice_aux < len(rows_aux) - 1:
            btn_next["state"] = ACTIVE
            btn_back["state"] = DISABLED
        else:
            btn_next["state"] = DISABLED
            btn_back["state"] = DISABLED
    except Exception as e:
        messagebox('Error', 'Não encontou este informação')
        print("Erro:", e)
        mysql_db.rollback()


def criar():
    try:
        if get_txt(txt_Name) == '':
            messagebox('Error', 'Nome obrigatorio')
        elif lbl_Id_V['text']:
            messagebox('Error', 'Limpe o Id')
        else:
            if get_txt(txt_email) != '' and ver_email() == 0:
                messagebox('Error', 'Email invalido')
            inseridor_aux = inseridor % ("pessoa",
                                         "(pessoa_Name,pessoa_Telemovel,pessoa_Telefone,pessoa_Email,pessoa_Morada,pessoa_Cidade,pessoa_Distrito,pessoa_Codigo_Postal,pessoa_Pais,pessoa_Empresa,pessoa_Profissao,pessoa_loacal_emp)",
                                         "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'"
                                         % (get_txt(txt_Name), get_txt(txt_tele), get_txt(txt_telf), get_txt(txt_email),
                                            get_txt(txt_morada), get_txt(txt_cidade), get_txt(txt_distrito),
                                            get_txt(txt_cod_postal), get_txt(txt_pais), get_txt(txt_empr),
                                            get_txt(txt_ocup), get_txt(txt_local)))
            cursor.execute(inseridor_aux)
            mysql_db.commit()
            procurador_aux = procurador % ('pessoa_Id', 'pessoa', 'pessoa_Name = "%s"' % get_txt(txt_Name))
            cursor.execute(procurador_aux)
            aux = cursor.fetchone()
            lbl_Id_V['text'] = aux
            messagebox('Finis', 'Informação creada')
    except Exception as e:
        messagebox('Error', 'Erro de informações')
        print("Erro:", e)
        mysql_db.rollback()


def mudar():
    try:
        global number_aux
        if get_txt(txt_email) != '' and ver_email() == 0:
            messagebox('Error', 'Email invalido')
        else:
            modificar_aux = modificar % ('pessoa',
                                         "pessoa_Name = '%s',pessoa_Telemovel = '%s',pessoa_Telefone = '%s',pessoa_Email = '%s',pessoa_Morada = '%s',pessoa_Cidade = '%s',pessoa_Distrito = '%s',pessoa_Codigo_Postal = '%s',pessoa_Pais = '%s',pessoa_Empresa = '%s',pessoa_Profissao = '%s',pessoa_loacal_emp = '%s'"
                                         % (get_txt(txt_Name), get_txt(txt_tele), get_txt(txt_telf), get_txt(txt_email),
                                            get_txt(txt_morada), get_txt(txt_cidade), get_txt(txt_distrito),
                                            get_txt(txt_cod_postal), get_txt(txt_pais), get_txt(txt_empr),
                                            get_txt(txt_ocup), get_txt(txt_local)),
                                         'pessoa_Id = "%s"' % str(number_aux))
            cursor.execute(modificar_aux)
            messagebox('Finis', 'Informação alterado')
    except Exception as e:
        messagebox('Error', 'Erro de informações')
        print("Erro:", e)
        mysql_db.rollback()


def eliminar():
    try:
        aux = tkinter.messagebox.askokcancel("Help", "Queres eliminar informações deste id")
        if aux:
            eliminador_aux = eliminador % ('pessoa', 'pessoa_Id = "%s"' % str(number_aux))
            cursor.execute(eliminador_aux)
            messagebox('Finis', 'Informação elminado')
            clear()
            mysql_db.commit()
    except Exception as e:
        messagebox('Error', 'Erro de informações')
        print("Erro:", e)
        mysql_db.rollback()


def crear_qrc():
    try:
        global vcard
        qr = qrcode.QRCode(version=10, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=5, border=1)
        procurador_aux = procurador % ('*', 'pessoa', 'pessoa_Id = ' + str(number_aux))
        cursor.execute(procurador_aux)
        aux = cursor.fetchone()
        if str(lbl_Id_V['text']) <= str(10):
            img_url = "https://pigsrockfestival.com/antonio/" + str(lbl_Id_V['text']) + ".png"
            vcard_aux = vcard % (aux[0], aux[1], aux[2], aux[3], aux[4], aux[5], aux[6],
                             aux[7], aux[8], aux[9], aux[10], aux[11], aux[12], img_url)
        else:
            vcard_aux = vcard % (aux[0], aux[1], aux[2], aux[3], aux[4], aux[5], aux[6],
                             aux[7], aux[8], aux[9], aux[10], aux[11], aux[12], None)
        if not os.path.exists('QR_Image'):
            os.makedirs("QR_Image")
        qr.add_data(vcard_aux)
        img = qr.make_image()
        img.save("QR_Image/" + str(lbl_Id_V['text']) + '.png')
        img.show()
        fin = open("QR_Image/" + str(lbl_Id_V['text']) + ".png", 'rb')
        img_aux = fin.read()
        fin.close()
        modificar_aux = modificar % ("pessoa", "pessoa_qrcode = %s", "pessoa_Id = '%s'")
        args = (img_aux, lbl_Id_V['text'])
        cursor.execute(modificar_aux, args)
        mysql_db.commit()
        print(vcard_aux)
    except Exception as e:
        messagebox('Error', 'Erro de informações')
        print("Erro:", e)
        mysql_db.rollback()


def create_img():
    try:
        global photo_aux
        if not os.path.exists('IMG'):
            os.makedirs("QR_Image")
        if not os.path.exists('./IMG/' + str(lbl_Id_V['text']) + ".png"):
            filepath = filedialog.askopenfilename()
            if filepath != '':
                img = Image.open(filepath)
                photo_aux = ImageTk.PhotoImage(img)
                lbl_img1['image'] = photo_aux
                img.save(os.path.join("./IMG/", str(lbl_Id_V['text']) + ".png"))
                fin = open("./IMG/" + str(lbl_Id_V['text']) + ".png", 'rb')
                img_aux = fin.read()
                fin.close()
                modificar_aux = modificar % ("pessoa", "pesooa_img= %s", "pessoa_Id = '%s'")
                args = (img_aux, lbl_Id_V['text'])
                cursor.execute(modificar_aux, args)
                mysql_db.commit()
            else:
                messagebox("erro", "Não seleccionou nenhum documento")
    except Exception as e:
        messagebox('Error', 'Erro de informações')
        print("Erro:", e)
        mysql_db.rollback()


def move_img():
    try:
        if not os.path.exists('./IMG/' + str(lbl_Id_V['text']) + ".png"):
            messagebox("erro", "Cria a imagem primeiro")
        else:
            global photo_aux_3
            filepath = filedialog.askopenfilename()
            if filepath != '':
                img = Image.open(filepath)
                photo_aux_3 = ImageTk.PhotoImage(img)
                lbl_img1['image'] = photo_aux_3
                img.save(os.path.join("./IMG/", str(lbl_Id_V['text']) + ".png"))
                fin = open("./IMG/" + str(lbl_Id_V['text']) + ".png", 'rb')
                img_aux = fin.read()
                fin.close()
                modificar_aux = modificar % ("pessoa", "pesooa_img = %s", "pessoa_Id = '%s'")
                args = (img_aux, lbl_Id_V['text'])
                cursor.execute(modificar_aux, args)
                mysql_db.commit()
            else:
                messagebox("erro", "Não seleccionou nenhum documento")
    except Exception as e:
        messagebox('Error', 'Erro de informações')
        print("Erro:", e)
        mysql_db.rollback()


def dele_img():
    try:
        if not os.path.exists('./IMG/' + str(lbl_Id_V['text']) + ".png"):
            messagebox("erro", "Não existe a imagem")
        else:
            os.remove('./IMG/' + str(lbl_Id_V['text']) + ".png")
            messagebox("delete", "Imagem eliminado")
            eliminar_aux = modificar % ("pessoa", "pesooa_img = %s", "pessoa_Id = '%s'")
            args = (None, lbl_Id_V['text'])
            cursor.execute(eliminar_aux, args)
            mysql_db.commit()
    except Exception as e:
        messagebox('Error', 'Erro de informações')
        print("Erro:", e)
        mysql_db.rollback()


def list_users():
    global aux01
    top = Toplevel()
    top.title('Menu')
    top.geometry('1000x700')
    top.iconbitmap('./SB-Vidros.ico')
    top["background"] = "#5ab100"

    sbar1 = Scrollbar(top)
    sbar1.pack(side='right', fill='y')
    sbar2 = Scrollbar(top, orient='horizontal')
    sbar2.pack(side='bottom', fill="x")

    columns = ("Id", "Nome", "Telemovel", "Telefone", "Email", "Morada", "Cidade", "Distrito",
               "Codigo_Postal", "Pais", "Empresa", "Profissão", "loacal_trabalho")
    treeview_user = ttk.Treeview(top, columns=columns, show="headings", xscrollcommand=sbar2.set,
                                 yscrollcommand=sbar1.set)
    for insert in columns:
        if insert == "Id":
            aux01 = 25
        if insert == "Email" or insert == "Morada" or insert == "Profissão" or insert == "loacal_trabalho":
            aux01 = 200
        treeview_user.column(insert, width=aux01, minwidth=aux01, anchor='center')
        treeview_user.heading(insert, text=insert, command=lambda _col=insert: sort_column(treeview_user, _col, False))
        aux01 = 100
    treeview_user.pack(side=LEFT, fill=BOTH)

    cursor.execute("SELECT * FROM pessoa")
    result = cursor.fetchall()

    for i in result:
        treeview_user.insert('', END, values=i)
    sbar1.config(command=treeview_user.yview)
    sbar2.config(command=treeview_user.xview)


mysql_db = myconect.connect(host="localhost", user="Antonio", password="20031203zhijie", database="qr_code_db")
cursor = mysql_db.cursor(buffered=True)
procurador = "SELECT %s FROM %s WHERE %s"
inseridor = "INSERT INTO %s %s VALUES (%s)"
modificar = "UPDATE %s SET %s WHERE %s"
eliminador = "DELETE FROM  %s WHERE %s"
vcard = '''BEGIN:VCARD
VERSION:4.0
NOTE:ID:%s
FN:%s
TEL;TYPE=cell:%s
TEL;TYPE=home:%s
EMAIL:%s
ADR;TYPE=home:;;%s;%s;%s;%s;%s
ORG:%s
TITLE:%s
ADR;TYPE=WORK:;;%s;;;;
PHOTO;VALUE=URL:%s
END:VCARD'''
number_aux = 0
indice_aux = 0
rows_aux = ''

root = Tk()
root.title('Menu')
root.geometry('1000x710')
root.iconbitmap('./SB-Vidros.ico')
root["background"] = "#5ab100"

img_01 = Image.open('SB-V.png')
photo_01 = ImageTk.PhotoImage(img_01)

title = Label(root, text='Informação pessoal', font=('Calibri', 50, 'bold italic'), bg="white",
              fg="red", relief="raised", padx=5)
numLbl = Label(root, text='Insere o que quere procure :')
numEty = Entry(root)
procBtn = Button(root, text='Procurar', command=porcura)
btn_Clear = Button(root, text='Limpar', command=clear)
btn_Save = Button(root, text='Modificar', command=mudar)
btn_Create = Button(root, text='Criar uma nova', command=criar)
btn_Del = Button(root, text='Apagar', command=eliminar)
btn_Crate_Img = Button(root, text='Carregar imagem', command=create_img)
btn_Move_Img = Button(root, text='Modificar imagem', command=move_img)
btn_Del_Img = Button(root, text='Eliminar imagem', command=dele_img)
btn_List_User = Button(root, text='Listar pessoas', command=list_users)
btn_QRC = Button(root, text='Crear QRCode', command=crear_qrc)
btn_back = Button(root, text='<', state=DISABLED, command=lambda: back_next("button1"))
btn_next = Button(root, text='>', state=DISABLED, command=lambda: back_next("button2"))
lbl_img1 = Label(root, image=photo_01)

fm = Frame(root)
lbl_Id = Label(fm, text='Id:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
lbl_Id_V = Label(fm, relief="sunken", borderwidth=5, anchor='w')
lbl_Name = Label(fm, text='Nome:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_Name = Text(fm)
lbl_tele = Label(fm, text='Telemóvel:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_tele = Text(fm)
lbl_telf = Label(fm, text='Telefone:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_telf = Text(fm)
lbl_email = Label(fm, text='Email:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_email = Text(fm)
lbl_morada = Label(fm, text='Morada:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_morada = Text(fm)
lbl_cidade = Label(fm, text='Cidade:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_cidade = Text(fm)
lbl_distrito = Label(fm, text='Distrito:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_distrito = Text(fm)
lbl_cod_postal = Label(fm, text='Código Pos. :', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_cod_postal = Text(fm)
lbl_pais = Label(fm, text='Páis:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_pais = Text(fm)
lbl_empr = Label(fm, text='Empresa:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_empr = Text(fm)
lbl_ocup = Label(fm, text='Ocupação:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_ocup = Text(fm)
lbl_local = Label(fm, text='Local:', font=('Calibri', 20, 'bold italic'), anchor='e', justify='left')
txt_local = Text(fm)

title.place(x=35, y=40, width=740, height=80)
numLbl.place(x=35, y=125, width=170, height=20)
numEty.place(x=225, y=125, width=250, height=20)

procBtn.place(x=540, y=150, width=240, height=20)
btn_Clear.place(x=540, y=175, width=240, height=20)
btn_Save.place(x=540, y=200, width=240, height=20)
btn_Create.place(x=540, y=225, width=240, height=20)
btn_Del.place(x=540, y=250, width=240, height=20)
btn_Crate_Img.place(x=540, y=275, width=240, height=20)
btn_Move_Img.place(x=540, y=300, width=240, height=20)
btn_Del_Img.place(x=540, y=325, width=240, height=20)
btn_List_User.place(x=540, y=350, width=240, height=20)
btn_QRC.place(x=540, y=375, width=240, height=20)
lbl_img1.place(x=540, y=400)
btn_back.place(x=250, y=680, width=20, height=20)
btn_next.place(x=300, y=680, width=20, height=20)

fm.place(x=35, y=150, width=475, height=525)
lbl_Id.place(x=35, y=5, width=130, height=20)
lbl_Id_V.place(x=170, y=5, width=285, height=25)
lbl_Name.place(x=35, y=40, width=130, height=20)
txt_Name.place(x=170, y=40, width=285, height=20)
lbl_tele.place(x=35, y=80, width=130, height=20)
txt_tele.place(x=170, y=80, width=285, height=20)
lbl_telf.place(x=35, y=120, width=130, height=20)
txt_telf.place(x=170, y=120, width=285, height=20)
lbl_email.place(x=35, y=160, width=130, height=20)
txt_email.place(x=170, y=160, width=285, height=20)
lbl_morada.place(x=35, y=200, width=130, height=20)
txt_morada.place(x=170, y=200, width=285, height=20)
lbl_cidade.place(x=35, y=240, width=130, height=20)
txt_cidade.place(x=170, y=240, width=285, height=20)
lbl_distrito.place(x=35, y=271, width=130, height=35)
txt_distrito.place(x=170, y=280, width=285, height=20)
lbl_cod_postal.place(x=20, y=310, width=145, height=35)
txt_cod_postal.place(x=170, y=320, width=285, height=20)
lbl_pais.place(x=35, y=350, width=130, height=35)
txt_pais.place(x=170, y=360, width=285, height=20)
lbl_empr.place(x=35, y=390, width=130, height=35)
txt_empr.place(x=170, y=400, width=285, height=20)
lbl_ocup.place(x=35, y=430, width=130, height=35)
txt_ocup.place(x=170, y=440, width=285, height=20)
lbl_local.place(x=35, y=475, width=130, height=20)
txt_local.place(x=170, y=480, width=285, height=20)

if __name__ == '__main__':
    root.mainloop()
    mysql_db.commit()
