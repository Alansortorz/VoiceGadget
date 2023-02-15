# -*- coding:utf-8 -*-
# 作者：超级大兔子
# 简介：系统工具助手

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtWidgets import QPushButton,QVBoxLayout,QHBoxLayout,QGroupBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,QThread,pyqtSignal
import sys,os

class My_Thread(QThread):
    signal_res = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.command = None

    def set_cmd(self,command):
        self.command = command

    def run(self):
        try:
            os.popen(rf"{self.command}")
            # self.signal_res.emit("执行成功")
            # print("执行成功")
        except:
            pass
            # self.signal_res.emit("执行失败")
            # print("执行失败")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("系统工具助手")
        self.setWindowIcon(QIcon("./images/logo.png"))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.setFixedSize(400,300)
        self.resize(400,300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.addLayout(self.init_system())
        layout.addLayout(self.init_def_app())
        self.setLayout(layout)

        # 绑定按钮事件
        self.btn11.clicked.connect(self.btn11_cmd)
        self.btn12.clicked.connect(self.btn12_cmd)
        self.btn13.clicked.connect(self.btn13_cmd)
        self.btn14.clicked.connect(self.btn14_cmd)
        self.btn21.clicked.connect(self.btn21_cmd)
        self.btn22.clicked.connect(self.btn22_cmd)
        self.btn23.clicked.connect(self.btn23_cmd)
        self.btn24.clicked.connect(self.btn24_cmd)
        self.btn31.clicked.connect(self.btn31_cmd)
        self.btn32.clicked.connect(self.btn32_cmd)
        self.btn33.clicked.connect(self.btn33_cmd)
        self.btn34.clicked.connect(self.btn34_cmd)
        self.btn41.clicked.connect(self.btn41_cmd)
        self.btn42.clicked.connect(self.btn42_cmd)
        self.btn43.clicked.connect(self.btn43_cmd)
        self.btn44.clicked.connect(self.btn44_cmd)
        self.btn51.clicked.connect(self.btn51_cmd)
        self.btn52.clicked.connect(self.btn52_cmd)
        self.btn53.clicked.connect(self.btn53_cmd)
        self.btn54.clicked.connect(self.btn54_cmd)
        self.btn61.clicked.connect(self.btn61_cmd)
        self.btn62.clicked.connect(self.btn62_cmd)
        self.btn63.clicked.connect(self.btn63_cmd)
        self.btn64.clicked.connect(self.btn64_cmd)

        # 实例化线程
        self.t = My_Thread()

    def init_system(self):
        box = QVBoxLayout()
        groupbox = QGroupBox("系统工具")
        layout = QVBoxLayout()
        layout.addLayout(self.init_btn_1(),2)
        layout.addLayout(self.init_btn_2(),2)
        layout.addLayout(self.init_btn_3(),2)
        layout.addLayout(self.init_btn_4(),2)
        groupbox.setLayout(layout)
        box.addWidget(groupbox)
        return box

    def init_def_app(self):
        box = QVBoxLayout()
        groupbox = QGroupBox("常用工具")
        layout = QVBoxLayout()
        layout.addLayout(self.init_btn_5())
        layout.addLayout(self.init_btn_6())
        groupbox.setLayout(layout)
        box.addWidget(groupbox)
        return box

    # 初始化按钮面板：第一排
    def init_btn_1(self):
        btn_layout = QHBoxLayout()
        self.btn11 = QPushButton("CMD")
        self.btn12 = QPushButton("控制面板")
        self.btn13 = QPushButton("注册表")
        self.btn14 = QPushButton("组策略")
        btn_layout.addWidget(self.btn11)
        btn_layout.addWidget(self.btn12)
        btn_layout.addWidget(self.btn13)
        btn_layout.addWidget(self.btn14)
        return btn_layout

    # 初始化按钮面板：第二排
    def init_btn_2(self):
        btn_layout = QHBoxLayout()
        self.btn21 = QPushButton("系统服务")
        self.btn22 = QPushButton("计算机管理")
        self.btn23 = QPushButton("设备管理器")
        self.btn24 = QPushButton("用户和组")
        btn_layout.addWidget(self.btn21)
        btn_layout.addWidget(self.btn22)
        btn_layout.addWidget(self.btn23)
        btn_layout.addWidget(self.btn24)
        return btn_layout

    # 初始化按钮面板：第三排
    def init_btn_3(self):
        btn_layout = QHBoxLayout()
        self.btn31 = QPushButton("事件查看器")
        self.btn32 = QPushButton("网络连接")
        self.btn33 = QPushButton("程序和功能")
        self.btn34 = QPushButton("Internet属性")
        btn_layout.addWidget(self.btn31)
        btn_layout.addWidget(self.btn32)
        btn_layout.addWidget(self.btn33)
        btn_layout.addWidget(self.btn34)
        return btn_layout

    # 初始化按钮面板：第四排
    def init_btn_4(self):
        btn_layout = QHBoxLayout()
        self.btn41 = QPushButton("磁盘管理器")
        self.btn42 = QPushButton("系统属性")
        self.btn43 = QPushButton("系统防火墙")
        self.btn44 = QPushButton("诊断工具")
        btn_layout.addWidget(self.btn41)
        btn_layout.addWidget(self.btn42)
        btn_layout.addWidget(self.btn43)
        btn_layout.addWidget(self.btn44)
        return btn_layout

    # 初始化按钮面板：第五排
    def init_btn_5(self):
        btn_layout = QHBoxLayout()
        self.btn51 = QPushButton("计事本")
        self.btn52 = QPushButton("计算器")
        self.btn53 = QPushButton("画图工具")
        self.btn54 = QPushButton("截图工具")
        btn_layout.addWidget(self.btn51)
        btn_layout.addWidget(self.btn52)
        btn_layout.addWidget(self.btn53)
        btn_layout.addWidget(self.btn54)
        return btn_layout

    # 初始化按钮面板：第六排
    def init_btn_6(self):
        btn_layout = QHBoxLayout()
        self.btn61 = QPushButton("远程桌面")
        self.btn62 = QPushButton("任务管理器")
        self.btn63 = QPushButton("任务计划")
        self.btn64 = QPushButton("IE浏览器")
        btn_layout.addWidget(self.btn61)
        btn_layout.addWidget(self.btn62)
        btn_layout.addWidget(self.btn63)
        btn_layout.addWidget(self.btn64)
        return btn_layout

    # CMD命令提示符
    def btn11_cmd(self):
        cmd = rf"start C:\Windows\System32\cmd.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 控制面板
    def btn12_cmd(self):
        cmd = rf"C:\Windows\System32\control.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 注册表
    def btn13_cmd(self):
        cmd = rf"C:\Windows\System32\regedt32.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 组策略
    def btn14_cmd(self):
        cmd = rf"C:\Windows\System32\gpedit.msc"
        self.t.set_cmd(cmd)
        self.t.start()

    # 系统服务
    def btn21_cmd(self):
        cmd = rf"C:\Windows\System32\services.msc"
        self.t.set_cmd(cmd)
        self.t.start()

    # 计算机管理
    def btn22_cmd(self):
        cmd = rf"C:\Windows\System32\compmgmt.msc"
        self.t.set_cmd(cmd)
        self.t.start()

    # 设备管理器
    def btn23_cmd(self):
        cmd = rf"C:\Windows\System32\hdwwiz.cpl"
        self.t.set_cmd(cmd)
        self.t.start()

    # 用户和组
    def btn24_cmd(self):
        cmd = rf"C:\Windows\System32\lusrmgr.msc"
        self.t.set_cmd(cmd)
        self.t.start()

    # 事件查看器
    def btn31_cmd(self):
        cmd = rf"C:\Windows\System32\eventvwr.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 网络连接
    def btn32_cmd(self):
        cmd = rf"C:\Windows\System32\ncpa.cpl"
        self.t.set_cmd(cmd)
        self.t.start()

    # 程序和功能
    def btn33_cmd(self):
        cmd = rf"C:\Windows\System32\appwiz.cpl"
        self.t.set_cmd(cmd)
        self.t.start()

    # Internet属性
    def btn34_cmd(self):
        cmd = rf"C:\Windows\System32\inetcpl.cpl"
        self.t.set_cmd(cmd)
        self.t.start()

    # 磁盘管理
    def btn41_cmd(self):
        cmd = rf"C:\Windows\System32\diskmgmt.msc"
        self.t.set_cmd(cmd)
        self.t.start()

    # 系统属性
    def btn42_cmd(self):
        cmd = rf"C:\Windows\System32\sysdm.cpl"
        self.t.set_cmd(cmd)
        self.t.start()

    # 系统防火墙
    def btn43_cmd(self):
        cmd = rf"C:\Windows\System32\Firewall.cpl"
        self.t.set_cmd(cmd)
        self.t.start()

    # 诊断工具
    def btn44_cmd(self):
        cmd = rf"C:\Windows\System32\dxdiag.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 计事本
    def btn51_cmd(self):
        cmd = rf"C:\Windows\System32\notepad.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 计算器
    def btn52_cmd(self):
        cmd = rf"C:\Windows\System32\calc.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 画图工具
    def btn53_cmd(self):
        cmd = rf"C:\Windows\System32\mspaint.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 截图工具
    def btn54_cmd(self):
        cmd = rf"C:\Windows\System32\snippingtool"
        self.t.set_cmd(cmd)
        self.t.start()

    # 远程桌面
    def btn61_cmd(self):
        cmd = rf"C:\Windows\System32\mstsc.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 任务管理器
    def btn62_cmd(self):
        cmd = rf"C:\Windows\System32\Taskmgr.exe"
        self.t.set_cmd(cmd)
        self.t.start()

    # 任务计划
    def btn63_cmd(self):
        cmd = rf"C:\Windows\System32\taskschd.msc"
        self.t.set_cmd(cmd)
        self.t.start()

    # 打开IE
    def btn64_cmd(self):
        cmd = rf"start iexplore.exe"
        self.t.set_cmd(cmd)
        self.t.start()

app = QApplication(sys.argv)
window = Window()
window.show()

qss = '''
* {
    background-color: rgb(25,35,45);
    font-family: 微软雅黑;
    color: rgb(224,225,227)
}
QPushButton {
    background-color: rgb(69,83,100);
    border: 2px solid rgb(69,83,100);
    border-radius: 5px;
    padding: 3px;
}
QPushButton:hover {
    background-color: rgb(84,104,122);
}
QPushButton:pressed {
    background-color: rgb(96,121,139);
}
'''
app.setStyleSheet(qss)
sys.exit(app.exec_())
