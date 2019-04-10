import sys
import os
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.uic import loadUi
except Exception as e:
    print(str(e))

dir_path = os.path.dirname(os.path.abspath(__file__))
ui_path = os.path.join(dir_path,'resource/demo.ui')
ico_path = os.path.join(dir_path,'pic/demo.png')
img_path = os.path.join(dir_path,'pic/scene.jpg')

class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        loadUi(ui_path, self)
        self.set_icon()
        self.set_timer()
        self.image_dis()

        # demo of signal and slot
        self.pushButton.clicked.connect(self.handle_pushbutton_click)

        # demo of using signal and slot to transmit parameter
        self.checkBox.clicked[bool].connect(self.handle_checkbox_clicked)

    # slot function with parameter
    def handle_checkbox_clicked(self,flag):
        self.label_checkbox.setText(str(flag))

    # slot function without parameter
    def handle_pushbutton_click(self):
        self.label_button.setText(str('clicked'))

    # set icon of this window
    def set_icon(self): 
        self.icon = QIcon(QPixmap(ico_path))
        if not self.icon.isNull():
            self.setWindowIcon(self.icon)

    # demo of qtimer
    def set_timer(self):    
        self.count = 0
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.handle_timer)
    
    def handle_timer(self):
        self.count += 1
        dis = 'Current Time is ' + str(self.count) + ' s'
        self.label_time.setText(str(dis))

    # we use qlabel to display image
    def image_dis(self):
        pic = QPixmap(img_path)
        self.image.setPixmap(pic)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()

    # we can ternimate the app with control c
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
 
    sys.exit(app.exec_())
