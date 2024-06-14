import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QTimer
import datetime

class CountdownApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('中考倒计时')
        self.setGeometry(1360, 0, 580, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 打印今天的日期
        self.today_label = QLabel('今天是', self)
        self.today_label.setGeometry(10, 10, 300, 50)
        self.today_label.setAlignment(Qt.AlignLeft)
        self.today_label.setStyleSheet('font-size: 26px; font-family: "微软雅黑"; color: black; background-color: transparent;')

        # 打印中考倒计时
        self.countdown_label = QLabel('距离中考仅有0天！', self)
        self.countdown_label.setGeometry(10, 70, 560, 100)
        self.countdown_label.setAlignment(Qt.AlignCenter)
        self.countdown_label.setStyleSheet('font-size: 40px; font-family: "幼圆"; color: black; background-color: transparent;')

        # 更新倒计时
        self.updateCountdown()

        # 使用定时器每秒更新一次倒计时
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateCountdown)
        self.timer.start(1000)

        self.show()

    def updateCountdown(self):
        exam_time = datetime.datetime(2025, 6, 12)
        now = datetime.datetime.now()
        days_left = (exam_time - now).days
        self.countdown_label.setText(f'距离中考<b><font size="6" color="red">仅有{days_left}天</font></b>')
        current_date = now.strftime("%Y-%m-%d")
        self.today_label.setText('今天是{}'.format(current_date))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CountdownApp()
    sys.exit(app.exec_())
