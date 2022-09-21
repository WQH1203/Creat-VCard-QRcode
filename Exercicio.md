# Ciração de QR Code VCard

Este aplicação é feito por:
>
> * Python
> * SQL
> * MYSQL
> * VCard
> * QR Code

Os modulos de Python usei são:
>
> * os
> * qrcode
> * re
> * tkinter
> * mysql.connector
> * PIL

## Codigo

### Inicio

Indiquei os modulos que usei e as ferramenas

```Python
import os
import qrcode
import re
import tkinter.messagebox
from tkinter import filedialog, ttk
from tkinter import *
import mysql.connector as myconect
from PIL import Image, ImageTk
```

### Funções

```Python
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
```

Este função é para limar as caixas de textos e imagem de pasta

`global photo_01` - Após a função ser chamada, a recolha do lixo recupera a foto variável, razão pela qual a variável global é utilizada.

`label['text'] = ''` - para o texto de label ser vazio

`text.delete("1.0", "end")` - é para eleminar os caracteres do caixa de texto

`label['image'] = (imagem)` - seria modar a imagem do label para outro imagem

***

```Python
def get_txt(aux):
    name = aux.get("0.0", "end").replace("\n", "").replace("\r", "")
    return name
```

Este função é para retirar as informações de caixa de texto sem `\n` e `\r`

`text.get("0.0", "end")` - é para receber infomação de caixa de texto

`variavel.replace("\n", "")` - é para subestituir `\n` por nada

***

```Python
def messagebox(title_aux, mensagem):
    tkinter.messagebox.showwarning(title_aux, mensagem)
```
