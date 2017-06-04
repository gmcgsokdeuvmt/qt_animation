import sys, os
import glob
from PyQt4 import QtGui, QtCore

class Action():
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    def getExitAction(self):
        exitAction = QtGui.QAction(QtGui.QIcon('src'+os.sep+'exit.png'), '&Exit', self.mainWindow)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        return exitAction

class ImageWidget(QtGui.QWidget):
    def __init__(self):
        super(ImageWidget,self).__init__()
        self.initUI()
        self.index = 0
        self.pixmaps = []

    def initUI(self):
        self.setLabel()
        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.label)

    def setLabel(self):
        self.label = QtGui.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    def setImage(self,image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)
        size = self.size()
        
        pixmap = pixmap.scaled(size,
                               aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                               transformMode=QtCore.Qt.SmoothTransformation
                              )
        self.label.setPixmap(pixmap)

    def addImage(self,image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)
        size = self.size()
        
        pixmap = pixmap.scaled(size,
                               aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                               transformMode=QtCore.Qt.SmoothTransformation
                              )
        self.pixmaps.append(pixmap)

    def showNextImage(self):
        self.index = self.index + 1 if self.index + 1 < len(self.pixmaps) else self.index 
        pixmap = self.pixmaps[self.index]
        self.label.setPixmap(pixmap)

    def showPrevImage(self):
        self.index = self.index - 1 if self.index > 0 else self.index 
        pixmap = self.pixmaps[self.index]
        self.label.setPixmap(pixmap)

    def getNextAction(self):
        nextAction = QtGui.QAction(QtGui.QIcon('src'+os.sep+'next.png'), '&Next', self)
        nextAction.setShortcut('Right')
        nextAction.setStatusTip('Next Image')
        nextAction.triggered.connect(self.showNextImage)
        return nextAction

    def getPrevAction(self):
        prevAction = QtGui.QAction(QtGui.QIcon('src'+os.sep+'prev.png'), '&Prev', self)
        prevAction.setShortcut('Left')
        prevAction.setStatusTip('Previous Image')
        prevAction.triggered.connect(self.showPrevImage)
        return prevAction

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.registerActions()
        self.statusBar()
        self.setMenuBar()
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('MainWindow')

        self.imageWidget = ImageWidget()
        self.setCentralWidget(self.imageWidget)
        image_list = glob.glob('../../../../Pictures/*.PNG')
        for path in image_list:
            self.imageWidget.addImage(path)
        self.setControl(self.imageWidget)

    
    def registerActions(self):
        action = Action(self)
        self.actions = {}
        self.actions['exit'] = action.getExitAction()

    def setMenuBar(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.actions['exit'])

    def setControl(self,imageWidget):
        menubar = self.menuBar()
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(imageWidget.getNextAction())
        editMenu.addAction(imageWidget.getPrevAction())

class AppManager():
    
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.window = MainWindow()
    
    def run(self):
        self.window.show()
        return self.app.exec_()

def main():
    manager = AppManager()
    return manager.run()

if __name__ == '__main__':
    sys.exit(main())

