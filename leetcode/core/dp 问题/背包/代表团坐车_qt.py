import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def save_dp(visit: list[int], car: int) -> int:
    dp = [0]*(car+1)
    dp[0] = 1
    for v in visit:
        for pre_c in range(car, -1, -1):
            if pre_c+v <= car:
                dp[pre_c+v] += dp[pre_c]
    return dp[car]

class DelegationCarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("代表团坐车方案计算器")
        self.setMinimumSize(600, 400)
        
        # 创建主窗口部件和布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # 创建标题
        title = QLabel("代表团坐车方案计算器")
        title.setFont(QFont('Arial', 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # 创建输入区域
        input_layout = QVBoxLayout()
        
        # 代表团人数输入
        visit_layout = QHBoxLayout()
        visit_label = QLabel("代表团人数(用逗号分隔):")
        self.visit_input = QLineEdit()
        self.visit_input.setPlaceholderText("例如: 1,2,3,4")
        visit_layout.addWidget(visit_label)
        visit_layout.addWidget(self.visit_input)
        input_layout.addLayout(visit_layout)
        
        # 汽车容量输入
        car_layout = QHBoxLayout()
        car_label = QLabel("汽车容量:")
        self.car_input = QLineEdit()
        self.car_input.setPlaceholderText("例如: 5")
        car_layout.addWidget(car_label)
        car_layout.addWidget(self.car_input)
        input_layout.addLayout(car_layout)
        
        # 计算按钮
        self.calc_button = QPushButton("计算方案数")
        self.calc_button.clicked.connect(self.calculate)
        self.calc_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        input_layout.addWidget(self.calc_button)
        
        layout.addLayout(input_layout)
        
        # 结果显示区域
        result_label = QLabel("计算结果:")
        result_label.setFont(QFont('Arial', 12))
        layout.addWidget(result_label)
        
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet("""
            QTextEdit {
                background-color: #f5f5f5;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.result_display)
        
        # 设置窗口样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: white;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit {
                padding: 6px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
        """)
    
    def calculate(self):
        try:
            # 获取输入
            visit_str = self.visit_input.text().strip()
            car_str = self.car_input.text().strip()
            
            if not visit_str or not car_str:
                self.result_display.setText("请输入代表团人数和汽车容量！")
                return
            
            # 解析输入
            visit = [int(x.strip()) for x in visit_str.split(',')]
            car = int(car_str)
            
            # 计算方案数
            result = save_dp(visit, car)
            
            # 显示结果
            self.result_display.setText(f"输入信息：\n代表团人数：{visit}\n汽车容量：{car}\n\n计算结果：\n共有 {result} 种坐车方案")
            
        except ValueError as e:
            self.result_display.setText("输入格式错误！请确保：\n1. 代表团人数用逗号分隔\n2. 所有输入都是正整数")
        except Exception as e:
            self.result_display.setText(f"计算出错：{str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DelegationCarWindow()
    window.show()
    sys.exit(app.exec_()) 