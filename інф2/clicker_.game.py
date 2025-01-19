from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Golub.clicker")
window.resize(800, 600)


current_boost = 1

score1 = 0
score = QLabel()
score.setText(str(score1))



area = QPushButton()
area.setFixedSize(250, 250)

pixmap = QPixmap("images.jpg")
area.setIcon(QIcon(pixmap))
area.setIconSize(pixmap.size())
area.setStyleSheet("text-align: center;")


upgrade_text = QLabel()
boost_text = QLabel()
boost_text.setText(f"Сила кліку: {current_boost}")
upgrade6 = QPushButton()
upgrade6.setText("+50")
upgrade6_sell = QPushButton()
upgrade6_sell.setText("Ціна 5000")
upgrade_text.setText("UPGRADES")
upgrade2_sell = QPushButton()
upgrade2_sell.setText("Ціна: 250 кліків")
upgrade2 = QPushButton()
upgrade2.setText("+5")
upgrade3_sell = QPushButton()
upgrade3_sell.setText("Ціна: 500 кліків")
upgrade3 = QPushButton()
upgrade3.setText("+10")
upgrade4 = QPushButton()
upgrade4_sell = QPushButton()
upgrade4_sell.setText("Ціна: 1000 кліків")
upgrade4.setText("+15")
upgrade5_sell = QPushButton()
upgrade5_sell.setText("Ціна: 1500 кліків")
upgrade5 = QPushButton()
upgrade5.setText("+25")
upgrade_sell = QPushButton()
upgrade_sell.setText("Ціна: 100 кліків")
upgrade = QPushButton()
upgrade.setText("+1")
button_leave = QPushButton()
button_leave.setText("Leave")


layout1 = QVBoxLayout()
layout3 = QVBoxLayout()
layout4 = QVBoxLayout()
layout5 = QVBoxLayout()

layout3.setSpacing(0)
layout3.setContentsMargins(0, 0, 0, 0)

frame = QFrame()
frame_layout = QVBoxLayout()
frame_layout2 = QVBoxLayout()
frame_layout3 = QVBoxLayout()
frame_layout4 = QVBoxLayout()
frame_layout5 = QVBoxLayout()
frame_layout6 = QVBoxLayout()

frame_layout6.addWidget(upgrade6)
frame_layout6.addWidget(upgrade6_sell)

frame_layout.addWidget(upgrade2)
frame_layout.addWidget(upgrade2_sell)

frame_layout3.addWidget(upgrade)
frame_layout3.addWidget(upgrade_sell)

frame_layout4.addWidget(upgrade4)
frame_layout4.addWidget(upgrade4_sell)

frame_layout5.addWidget(upgrade5)
frame_layout5.addWidget(upgrade5_sell)

frame_layout2.addWidget(upgrade3)
frame_layout2.addWidget(upgrade3_sell)

frame_layout.setSpacing(0)
frame_layout.setContentsMargins(0, 0, 0, 0)




layout1.addWidget(area)
layout1.addWidget(button_leave)




layout4.addWidget(boost_text)
layout4.addWidget(score)


layout2 = QHBoxLayout()



layout5.addLayout(frame_layout6)
layout3.addLayout(frame_layout5)
layout3.addLayout(frame_layout4)
layout3.addLayout(frame_layout3)
layout3.addLayout(frame_layout2)
layout3.addLayout(frame_layout)
layout2.addLayout(layout1)
layout2.addLayout(layout3)
layout2.addLayout(layout5)
layout2.addLayout(layout4)



window.setLayout(layout2)







game_over = False

def leave():
    window.close()

def scoree():
    global score1
    score1 += current_boost
    score.setText(str(score1))



def upgrade_clicked():
    global current_boost, score1
    if score1 >= 100:
        score1 -= 100
        current_boost += 1
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade2_clicked():
        global current_boost, score1
        if score1 >= 250:
            score1 -= 250
            current_boost += 5
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade3_clicked():
        global current_boost, score1
        if score1 >= 500:
            score1 -= 500
            current_boost += 10
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade4_clicked():
        global current_boost, score1
        if score1 >= 1000:
            score1 -= 1000
            current_boost += 15
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade5_clicked():
        global current_boost, score1
        if score1 >= 1500:
            score1 -= 1500
            current_boost += 25
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade6_clicked():
        global current_boost, score1
        if score1 >= 5000:
            score1 -= 5000
            current_boost += 50
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")


button_leave.clicked.connect(leave)
area.clicked.connect(scoree)
upgrade.clicked.connect(upgrade_clicked)
upgrade2.clicked.connect(upgrade2_clicked)
upgrade3.clicked.connect(upgrade3_clicked)
upgrade4.clicked.connect(upgrade4_clicked)
upgrade5.clicked.connect(upgrade5_clicked)
upgrade6.clicked.connect(upgrade6_clicked)





window.show()
app.exec_()