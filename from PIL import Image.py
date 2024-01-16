from PIL import Image
from PIL import ImageFilter
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
QFileDialog, QMessageBox, 
QListWidget,QHBoxLayout,QVBoxLayout,QWidget,QLabel,QPushButton,
QFileDialog)
import os
from PyQt5.QtGui import QPixmap
from PIL.ImageFilter import ( BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN, GaussianBlur, UnsharpMask )
from PyQt5.QtCore import Qt
app = QApplication([])
window = QWidget()
window.setWindowTitle('Easy Editor')
btn_dir = QPushButton('Папка')
lb_image = QLabel('Картинка')
lw_files = QListWidget()

btn_left = QPushButton('Left')
btn_right = QPushButton('Right')
btn_flip = QPushButton('Flip')
btn_sharp = QPushButton('Sharp')
btn_bw = QPushButton('B/W')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image,95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1,20)
row.addLayout(col2,80)
window.setLayout(row)
window.show()
wdir = ""
def filter(files, extension):
    result = []
    for filename in files:
        for ext in extension:
            if filename.endwith(ext):
                result.append(filename)
    return result

def choosewDir():
    global wdir
    wdir = QFileDialog.getExistingDirectory()
def showFileNameList():
    extensions = ['.jpg','.jpeg','.png','.gif','.bmp']
    choosewDir()
    filenames = filter(os.listdir(wdir),extensions)

    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)
btn_dir.clicked.connect(showFileNameList)

class ImageProcessor():
        def __init___(self):
            self.image = None
            self.filename = None
            self.dir = None
            self.save_dir = "Modified/"
        def loadimmage(self, dir, filename):
            self.filename = filename
            self.dir = dir
            image_path = os.path.join(dir,filename)
            self.image = Image.open(image_path)
        
        def saveImage(self):
            path = os.path.join(self.dir,self.save_dir)
            if not(os.path.exists(path) or os.path.isdir(path)):
                os.mkdir(path)
            image_path = os.path.join(path,self.filename)
            self.image.save(image_path)
        def do_btw(self):
            self.image = self.image.convert("L")
            self.saveImage()
            image_path = os.path.join(self.dir,self.save_dir,self.filename)
            self.showImage(image_path)
        def do_left(self):
            self.image = self.image.transpose(Image.ROTATE_90)
            self.saveImage()
            image_path = os.path.join(self.dir,self.save_dir,self.filename)
            self.showImage(image_path)
        def do_right(self):
            self.image = self.image.transpose(Image.ROTATE_270)
            self.saveImage()
            image_path = os.path.join(self.dir,self.save_dir,self.filename)
            self.showImage(image_path)
        def do_flip(self):
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage()
            image_path = os.path.join(self.dir,self.save_dir,self.filename)
            self.showImage(image_path)
        def apply_blur(self):
            self.image = self.image.filter(ImageFilter.BLUR)
            self.save_image()
            image_path = os.path.join(self.dir,self.save_dir,self.filename)
            self.showImage(image_path)
        def showImage(self,path):
            lb_image.hide()
            pixmapimage = QPixmap(path)
            w , h =lb_image.width(), lb_image.height()
            pixmapimage = pixmapimage.scaled(w,h, Qt.KeepAspectRatio)
            lb_image.setPixmap(pixmapimage)
            lb_image.show()
def showChosemimage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        wkImage.loadimmage(filename)
        wkImage.showImage(os.path.join(wdir,wkImage.filename))
wkImage = ImageProcessor()
lw_files.currentRowChanged.connect(showChosemimage)                
        
        


app.exec_()