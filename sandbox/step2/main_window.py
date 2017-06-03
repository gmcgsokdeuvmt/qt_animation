import sys, os
from PyQt4 import QtGui

class Action():
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    def exit(self):
        exitAction = QtGui.QAction(QtGui.QIcon('src'+os.sep+'exit.png'), '&Exit', self.mainWindow)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        return exitAction
        
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
    
    def registerActions(self):
        action = Action(self)
        self.actions = {}
        self.actions['exit'] = action.exit()

    def setMenuBar(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.actions['exit'])

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

