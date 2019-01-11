# coding = utf-8
from  PIL import Image
# 导入argparse库，用来管理命令行参数输入
import argparse

# 创建解析对象
parse = argparse.ArgumentParser()
# 添加要解析的命令行参数
# parse.add_argument()
# 定义输入，输出文件，文件的高度与宽度
# file=open('D:\/test\/testpng.PNG','r')
parse.add_argument('-file')  # 输入文件
parse.add_argument('-o', '--output')  # 输出文件
parse.add_argument('--width', type=int, default=120)  # 设置宽度
parse.add_argument('--height', type=int, default=40)  # 设置高度
# 进行解析
arg = parse.parse_args()

# 设置参数输入，输出等
IMG = arg.file
# file.close()
WIDTH = arg.width

HEIGHT = arg.height

OUTPUT = arg.output
# 设置调用字符的集合
acsill_char = list("a!@#!%^#$^*()$%^shajncaljgmc,zxlc[p.v/,';]lpgf[zlkd[q,f;,+_vndjhhds")


# 讲RGB转换为字符
def get_char(r, g, b, alpha=256):
    # 判断alpha的值
    if alpha == 0:
        return ''
    # 获取字符集的长度
    length = len(acsill_char)
    # 将RGB值转换为灰度值gary,灰度返回为0-255
    gary = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 将灰度值映射到置顶的字符上
    unit = (256 + 1) / length
    # 返回灰度值对应的字符
    return acsill_char[int(gary / unit)]

if __name__ == '__main__':
    #打开并调整图片的高和宽
    im=Image.open('D:\/test\/testpng.PNG','r')
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt=""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt +=get_char(*im.getpixel((j,i)))
        txt +='\n'
    print(txt)

    if OUTPUT:
        with open(OUTPUT,'W') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)