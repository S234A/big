from mymapapi import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton 
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QPixmap

W = 400
H = 450
dMenu = 50
m = 10 #отступ
map_w, map_h = W -2 * m, H - dMenu - 2 * m


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, W, H)
        self.setWindowTitle('Карта')

        self.maps = "one.png"
        self.mas = 8


        self.label = QLabel(self)
        self.label.setText("Введите координаты центра карты:")
        self.label.move(10, 10)

        self.lat_input = QLineEdit(self)
        self.lat_input.resize(80,25)
        self.lat_input.move(10, 30)
        self.lat_input.setText("55.7507")
        self.lon_input = QLineEdit(self)
        self.lon_input.resize(80,25)
        self.lon_input.move(100, 30)
        self.lon_input.setText("37.6256")

        self.btn = QPushButton('Отобразить', self)
        self.btn.resize(80,25)
        self.btn.move(200, 30)
        self.btn.clicked.connect(self.show_map_file)

        self.btnp = QPushButton('+', self)
        self.btnp.resize(25, 25)
        self.btnp.move(320, 30)
        self.btnp.clicked.connect(self.mas_plus)

        self.btnm = QPushButton('-', self)
        self.btnm.resize(25, 25)
        self.btnm.move(360, 30)
        self.btnm.clicked.connect(self.mas_minus)

        self.pixmap = QPixmap(self.maps)
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.lbl.setGeometry(m , m + dMenu, map_w, map_h)
        self.lbl.move(10, 60)

        self.count = 0

    def show_map_file(self):
        # Показать карту

        lon = self.lon_input.text()
        lat = self.lat_input.text()

        map_locations = "ll=" + ",".join([lon,lat])# + "&spn=1.0,1.0"

        map_type = "map"
        map_param = "z={0}&size={1},{2}".format(str(self.mas),
                                                str(map_w),
                                                str(map_h))
        f_name = get_file_map(map_locations, map_type,map_param)
        if f_name:
            self.maps = f_name

        self.pixmap.load(self.maps)
        self.lbl.setPixmap(self.pixmap)

    def mas_minus(self):
       self.mas = (self.mas - 1) % 18
       self.show_map_file()

    def mas_plus(self):
       self.mas = (self.mas + 1) % 18
       self.show_map_file()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
