#encoding:utf-8
# Import the two function from the core
import core.T2I_core as T2I_core
import os

print('图片藏字 V2 by Wyatt\n=================')
mode = int(input('加密模式（1）还是解密模式（2）：'))

print('=================')
if mode == 1:
    print('加密模式\n=================')
    sampleText = input('请输入要加密的内容：')
    samplePictureDir = input('请输入图片地址：')
    outputPictureDir = samplePictureDir.split('.')[0] + '_hideText.png'

    print('开始加密...')
    try:
        T2I_core.txt2Img(
            photoDir=samplePictureDir,
            message=sampleText,
            outputFile=outputPictureDir
        )
        print('加密成功！')
    except Exception as e:
        print('程序出错：'+ str(e))
        input()
        os._exit(0)

elif mode == 2:
    print('解密模式\n=================')
    pictureContainTextDir = input('请输入图片地址：')


    print('开始解密...')
    try:
        message = T2I_core.img2Txt(
            photoDir=pictureContainTextDir
        )
        print('解密成功！')
        print('=================\n内容：')
        print(message)
    except Exception as e:
        print('程序出错：' + str(e))
        os._exit(0)
else:
    print('兄嘚，你输的是个啥？')

input('=================\n源码详见：Https://gitlab.com/wyatthuang/text2image-v2\npress enter to quit...')
