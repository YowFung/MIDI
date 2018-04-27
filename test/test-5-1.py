""" 信号槽 signal & slots """
""" sender是发出信号的对象。receiver是接收信号的对象。slot(插槽)是对信号做出反应的方法。 """

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号槽")
        self.resize(480, 600)
        self.move(300, 50)

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)                      # LCD 数字显示屏
        sld = QSlider(Qt.Horizontal, self)          # 滚动条

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)       # 将滚动条的valueChanged信号连接到lcd的display插槽




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()

    win.show()
    sys.exit(app.exec_())