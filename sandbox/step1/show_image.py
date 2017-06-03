from PyQt4 import QtGui, QtCore

class AppManager:

    def __init__(self,args=[]):
        self.app = QtGui.QApplication(args)

    def launch_window(self,title,size=(500,500)):
        self.windowSize = size
        self.window = QtGui.QWidget()
        self.window.setWindowTitle(title)
        self.window.resize(size[0],size[1])
    
    def set_image(self,image_path):
        # set label
        label = QtGui.QLabel(self.window)
        
        # load image(maybe verbose)
        image = QtGui.QImage(image_path)
        
        # convert to pixmap
        pixmap = QtGui.QPixmap.fromImage(image)

        # set scale
        w, h = self.windowSize
        pixmap = pixmap.scaled(w,h,aspectRatioMode=QtCore.Qt.KeepAspectRatio,transformMode=QtCore.Qt.SmoothTransformation)
        
        # set image on label
        label.setPixmap(pixmap)	
        label.setScaledContents(True)
        label.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        label.setAlignment(QtCore.Qt.AlignCenter)

    def run(self):
        self.window.show()
        self.app.exec()

def main():
    manager = AppManager()
    manager.launch_window(title="app",size=(500,500))
    manager.set_image('../../../../Desktop/hoge.png')
    manager.run()

if __name__ == '__main__':
    main()
