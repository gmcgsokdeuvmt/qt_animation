from PyQt4 import QtGui

class AppManager:

    def __init__(self,args=[]):
        self.app = QtGui.QApplication(args)

    def launch_window(self,title,size=(300,300)):
        self.window = QtGui.QWidget()
        self.window.setWindowTitle(title)
        self.window.resize(size[0],size[1])
        self.window.show()
    
    def run(self):
        self.app.exec()

def main():
    manager = AppManager()
    manager.launch_window(title="app",size=(300,300))
    manager.run()

if __name__ == '__main__':
    main()
