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
