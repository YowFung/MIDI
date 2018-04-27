""" 事件发送者 """

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

class Win(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 50, 480, 600)
        self.setWindowTitle("事件发送者")

        self.initUI()

    def initUI(self):
        btn1 = QPushButton('Button1', self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()                            # 创建状态栏

    def buttonClicked(self):
        sender = self.sender()                      # 获取seeder信号源

        self.statusBar().showMessage(sender.text() + " was pressed")        # 状态栏显示消息


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()

    sys.exit(app.exec_())
