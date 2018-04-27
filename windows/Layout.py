""" 母版窗体 """

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

""" 窗体类 """
class WinLayout(QWidget):
    def __init__(self):
        super().__init__()

        """ 初始化窗体基本属性 """
        self.resize(480, 600)
        self.move(300, 50)
        self.setWindowTitle("智能乐谱识别")
        self.setWindowIcon(QIcon('images/favicon.ico'))

        """ 创建基本控件 """
        # 退出按钮
        btn_quit = QPushButton('Exit', self)
        btn_quit.setGeometry(0, 0, 48, 48)

        # 切换按钮
        btn_mode = QPushButton('Mode', self)
        btn_mode.setGeometry(48, 0, 48, 48)

        # 标题栏
        label_title = QLabel('  智能识谱仪', self)
        label_title.setGeometry(96, 0, self.width() - 144, 48)

        # 菜单按钮
        btn_menu = QPushButton('Menu', self)
        btn_menu.setGeometry(self.width() - 48, 0, 48, 48)


    """ 窗体被关闭事件 """
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "提示", "确定要退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accpet()
        else:
            event.ignore()