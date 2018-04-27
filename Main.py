""" 窗体母板 """

import sys
from PyQt5.QtWidgets import QApplication
from windows.Layout import *
from windows.Player import *

# 窗体程序入口
if __name__ == '__main__':
    # 初始化窗体
    app = QApplication(sys.argv)
    window = WinPlayer(WinLayout())
    # window.win.showFullScreen()
    window.win.show()

    # 使窗体程序进入主循环
    sys.exit(app.exec_())