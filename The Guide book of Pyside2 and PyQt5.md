# The Guide book of Pyside2 and PyQt5

##  Author: Siyu chen 陈思宇
##  Date : 2019/04/10

### 安装
对于我们的开发环境,如果你电脑上面已经安装了ROS,那么你可以在通过`python2`直接使用`PySide2 PyQt5`,但是如果你电脑上没有安装ROS,那么需要配置开发环境.
#### 开发环境依赖ROS
你可以在`terminal`中安装ROS,具体见ROS官网.
#### 开发环境不依赖ROS
我们推荐使用Anaconda,请先在计算机上安装`anaconda`,具体如何安装请参考官网.

对于`Anaconda`我们建议不要在安装时候把环境变量写入`~/.bashrc`而是写一个脚本,每次使用`Anaconda`时候执行脚本.否则会造成系统的`python`的环境变量混乱.

##### 安装PySide2
通过conda安装PySide2
```shell
conda install PySide2
```
##### 安装PyQt5
通过conda安装PyQt5
```shell
conda install pyqt
```
请自行验证系统是否已经安装`PySide2`与`PyQt5`成功.

### 简易教程
我们以`PyQt5`为例,讲解基本使用.
#### QLabel,QPushbutton,QTimer,QWidget,QLayout,QCheckBox的简要介绍
```python
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
        dis = 'Current Time is ' + str(self.count)
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
```

