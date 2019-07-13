# Text2Img V2
By using this tool, you can hide any text under picture. And compare to the version one, this version is  much more faster, and higher efficiency. 

## How to use

First of all, install the needed package below:

```cmd
pip install opencv-python
```

**Using GUI:**

Just run the `t2i_GUI.py` by using `pythonw t2i_GUI.py`. And following the step

**Using core:**

```python
# Import the two function from the core
import core.T2I_core as T2I_core

# 1. hide text into picture
sampleText = 'This is the world which will be hidden under the picture'
samplePictureDir = 'sample_picture.jpg'
outputPictureDir = 'picture_after.png'

T2I_core.txt2Img(
    photoDir=samplePictureDir,
    message=sampleText,
    outputFile=outputPictureDir
)

# 2. abstract text from picture
pictureContainTextDir = 'picture_after.png'

message = T2I_core.img2Txt(
    photoDir=pictureContainTextDir
)

```

## principle
> *The order below might exist difference compared to the programming part:*

![flow chart](https://cdn-1257758577.cos.ap-chengdu.myqcloud.com/2019/06/30/1561862395.png)

## Advantage
+ Low data loss, for a 4k picture, it can storage 550000+ english letter.
+ Theoretically, without considering the size of the picture. It can storage more than 1b data.
+ High executing efficiency

## Limited
+ Data loss will dramatically loss if the texts are write in the language which have the different length of ASCII.
+ Only support ASCII in range between: 1 to $\sum_{i=1}^{31}$
+ The relationship between picture size and encoding text is **approximately** equal to the `picture's height * width` divided by `max length of the ASCII of data`. For example, for all the english letters, their ASCII is always equal to 7. 

## In the future

Add a encryption option

## Open source
GPL