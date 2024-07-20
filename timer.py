from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSpinBox
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window()

    def main_window(self):
        centralwidget = QWidget()
        self.setCentralWidget(centralwidget)
        self.setWindowTitle('Таймер')
        self.setFixedSize(550, 200)

        layout = QVBoxLayout()

        self.hello_text = QLabel('''Добро пожаловать в Таймер!
В нём вы сможете поставить время за которое вы хотели бы себе напомнить/сделать,
по истечению времени у вас появится уведомление о завершении таймера!''')
        layout.addWidget(self.hello_text)

        self.time_input_layout = QHBoxLayout()
        self.time_input_label = QLabel("Установить таймер (в минутах):")
        self.time_input = QSpinBox()
        self.time_input.setRange(1, 360)  # Setting range from 1 minute to 6 hours
        self.time_input_layout.addWidget(self.time_input_label)
        self.time_input_layout.addWidget(self.time_input)
        layout.addLayout(self.time_input_layout)

        self.start_button = QPushButton("Начать таймер")
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        self.timer_label = QLabel("Оставшееся время: ")
        layout.addWidget(self.timer_label)

        centralwidget.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_left = 0

    def start_timer(self):
        self.time_left = self.time_input.value() * 60  # Convert minutes to seconds
        self.timer.start(1000)  # Timer updates every second
        self.update_timer_label()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_timer_label()
        else:
            self.timer.stop()
            self.timer_label.setText("Время вышло!")
            self.notify_user()

    def update_timer_label(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label.setText(f"Оставшееся время: {minutes} минут {seconds} секунд")

    def notify_user(self):
        self.hello_text.setText("Таймер завершён!")

def start():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start()
