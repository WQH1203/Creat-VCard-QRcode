# vim: set ts=4 et sw=4 sts=4 fileencoding=utf-8 :

import qrcode

# vCard内容
data = '''BEGIN:VCARD
VERSION:4.0
N:Gump;Forrest;;Mr.;  
ORG:Bubba Gump Shrimp Co.
TITLE:Shrimp Man
PHOTO;MEDIATYPE=image/gif:http://www.example.com/dir_photos/my_photo.gif
TEL;TYPE=work,voice;VALUE=uri:tel:+1-111-555-1212
TEL;TYPE=home,voice;VALUE=uri:tel:+1-404-555-1212
ADR;TYPE=WORK;PREF=1;LABEL="100 Waters Edge\nBaytown\, LA 30314\nUnited States of America":;;100 Waters Edge;Baytown;LA;30314;United States of America
ADR;TYPE=HOME;LABEL="42 Plantation St.\nBaytown\, LA 30314\nUnited States of America":;;42 Plantation St.;Baytown;LA;30314;United States of America
EMAIL:forrestgump@example.com
REV:20080424T195243Z
x-qq:21588891
END:VCARD'''

'''
ORG:Bubba Gump Shrimp Co. - 组织
各级组织成分，
    主要指组织名称（第一个字段）、
    组织下级单位（第二个字段）、
    更下级的单位名称（第三个字段），
依此递推。

TITLE:Shrimp Man - 职位

REV:2008/04/24-T195243Z - 	最近修改时间

x-qq:21588891 - 自己定义的类型需要以“x-”开头
'''

qr = qrcode.QRCode(
    # version值为1~40的整数,控制二维码的大小,(最小值是1,是个12*12的矩阵)
    # 如果想让程序自动确定,将值设置为 None 并使用 fit 参数即可
    version=4,
    # error_correction: 控制二维码的错误纠正功能,可取值下列4个常量
    #   ERROR_CORRECT_L: 大约7%或更少的错误能被纠正
    #   ERROR_CORRECT_M(默认): 大约15%或更少的错误能被纠正
    #   ERROR_CORRECT_Q: 大约25%或更少的错误能被纠正
    #   ERROR_CORRECT_H: 大约30%或更少的错误能被纠正
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    # 控制二维码中每个小格子包含的像素数
    box_size=5,
    # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4,是相关标准规定的最小值)
    border=4,
)

# 将vCard数据填入qr
qr.add_data(data)

qr.make(fit=True)

# 生成图片
img = qr.make_image()

# 将图片存入指定路径文件
img.save('jack.jpg')
