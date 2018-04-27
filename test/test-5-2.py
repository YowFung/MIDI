""" 重新实现事件处理器 """

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class Win(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("重新实现事件处理器")
        self.resize(480, 600)
        self.move(300, 50)

    # 键盘按下事件
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:                    # 按下 ESC 键就关闭窗体
            self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()

    sys.exit(app.exec_())