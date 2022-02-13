import sys
import time
import datetime
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sqlite3
from ui_info import Ui_Information
from ui_piano import Ui_MainWindow
from ui_delete import Ui_Form


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.C1.clicked.connect(self.run)
        self.C2.clicked.connect(self.run)
        self.D1.clicked.connect(self.run)
        self.D2.clicked.connect(self.run)
        self.E1.clicked.connect(self.run)
        self.F1.clicked.connect(self.run)
        self.F2.clicked.connect(self.run)
        self.G1.clicked.connect(self.run)
        self.G2.clicked.connect(self.run)
        self.A1.clicked.connect(self.run)
        self.A2.clicked.connect(self.run)
        self.B1.clicked.connect(self.run)
        self.C3.clicked.connect(self.run)
        self.C4.clicked.connect(self.run)
        self.D3.clicked.connect(self.run)
        self.D4.clicked.connect(self.run)
        self.E3.clicked.connect(self.run)
        self.F3.clicked.connect(self.run)
        self.F4.clicked.connect(self.run)
        self.G3.clicked.connect(self.run)
        self.G4.clicked.connect(self.run)
        self.A3.clicked.connect(self.run)
        self.A4.clicked.connect(self.run)
        self.B3.clicked.connect(self.run)
        self.C5.clicked.connect(self.run)
        self.C6.clicked.connect(self.run)
        self.D5.clicked.connect(self.run)
        self.D6.clicked.connect(self.run)
        self.E5.clicked.connect(self.run)
        self.start.clicked.connect(self.start_record)
        self.stop.clicked.connect(self.stop_record)
        self.vospr.clicked.connect(self.vosprr)
        self.delme.clicked.connect(self.dialog)
        self.info.clicked.connect(self.information)
        self.exit.clicked.connect(self.close)

        pygame.mixer.init()
        pygame.init()
        self.flag = 0
        self.record = []
        self.a = 0
        self.b = 0
        con = sqlite3.connect('piano.db')
        cur = con.cursor()
        self.id = cur.execute("""Select id from records""").fetchall()
        self.list_id = [i[0] for i in self.id]
        self.comboBox.addItems([str(x) for x in self.list_id])

    def run(self):
        if self.a == 0:
            self.a = datetime.datetime.now()
        elif self.a != 0:
            self.b = datetime.datetime.now()

            self.record.append((self.b - self.a).seconds + ((self.b - self.a).microseconds * (10 ** -6)))
            self.a = self.b

        if self.sender() == self.C1:
            self.music_file = 'c3.ogg'
        if self.sender() == self.C2:
            self.music_file = 'c3m.ogg'
        if self.sender() == self.D1:
            self.music_file = 'd3.ogg'
        if self.sender() == self.D2:
            self.music_file = 'd3m.ogg'
        if self.sender() == self.E1:
            self.music_file = 'e3.ogg'
        if self.sender() == self.F1:
            self.music_file = 'f3.ogg'
        if self.sender() == self.F2:
            self.music_file = 'f3m.ogg'
        if self.sender() == self.G1:
            self.music_file = 'g3.ogg'
        if self.sender() == self.G2:
            self.music_file = 'g3m.ogg'
        if self.sender() == self.A1:
            self.music_file = 'a3.ogg'
        if self.sender() == self.A2:
            self.music_file = 'a3m.ogg'
        if self.sender() == self.B1:
            self.music_file = 'b3.ogg'
        if self.sender() == self.C3:
            self.music_file = 'c4.ogg'
        if self.sender() == self.C4:
            self.music_file = 'c4m.ogg'
        if self.sender() == self.D3:
            self.music_file = 'd4.ogg'
        if self.sender() == self.D4:
            self.music_file = 'd4m.ogg'
        if self.sender() == self.E3:
            self.music_file = 'e4.ogg'
        if self.sender() == self.F3:
            self.music_file = 'f4.ogg'
        if self.sender() == self.F4:
            self.music_file = 'f4m.ogg'
        if self.sender() == self.G3:
            self.music_file = 'g4.ogg'
        if self.sender() == self.G4:
            self.music_file = 'g4m.ogg'
        if self.sender() == self.A3:
            self.music_file = 'a4.ogg'
        if self.sender() == self.A4:
            self.music_file = 'a4m.ogg'
        if self.sender() == self.B3:
            self.music_file = 'b4.ogg'
        if self.sender() == self.C5:
            self.music_file = 'c5.ogg'
        if self.sender() == self.C6:
            self.music_file = 'c5m.ogg'
        if self.sender() == self.D5:
            self.music_file = 'd5.ogg'
        if self.sender() == self.D6:
            self.music_file = 'd5m.ogg'
        if self.sender() == self.E5:
            self.music_file = 'e5.ogg'

        if self.flag == 1:
            self.record.append(self.music_file)

        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.event.poll()

    def start_record(self):
        self.flag = 1

    def stop_record(self):
        self.s = ''
        self.flag = 0
        self.record.append(1)
        for i in self.record:
            self.s += str(i) + ','
        self.con = sqlite3.connect('piano.db')
        self.cur = self.con.cursor()
        self.cur.execute("""INSERT INTO records(audio) VALUES(?)""", (self.s,))
        id = (self.cur.execute("""SELECT id FROM records WHERE audio = (?)""", (self.s,))).fetchall()
        self.con.commit()
        self.list_id.append(id[0][0])
        self.con.close()
        self.comboBox.addItem(str(id[0][0]))

    def vosprr(self):
        current_id = self.comboBox.currentText()
        self.con = sqlite3.connect('piano.db')
        self.cur = self.con.cursor()
        question = self.cur.execute("""SELECT audio FROM records WHERE id = (?)""", (current_id,)).fetchall()
        self.con.close()
        self.record2 = question[0][0].split(',')
        self.record2.pop()
        for i in range(0, (len(self.record2)) - 1, 2):
            pygame.mixer.music.load(self.record2[i])
            pygame.mixer.music.play()
            time.sleep(float(self.record2[i + 1]))

    def dialog(self):
        self.current_id = self.comboBox.currentText()
        self.del_dialog = Dialog(self, self.current_id)
        self.del_dialog.show()

    def information(self):
        self.inf = About(self)
        self.inf.show()

    def update_list(self):
        self.comboBox.clear()
        self.flag = 0
        self.record = []
        self.a = 0
        self.b = 0
        con = sqlite3.connect('piano.db')
        cur = con.cursor()
        self.id = cur.execute("""Select id from records""").fetchall()
        self.list_id = [i[0] for i in self.id]
        self.comboBox.addItems([str(x) for x in self.list_id])

    def close(self):
        self.hide()


class About(QMainWindow, Ui_Information):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inf_close)

    def inf_close(self):
        self.hide()


class Dialog(QWidget, Ui_Form):
    def __init__(self, *args):
        super().__init__()
        self.current_id = args[-1]
        self.setupUi(self)
        self.ok.clicked.connect(self.ok_del)
        self.cancel.clicked.connect(self.cancel_form)

    def cancel_form(self):
        self.hide()

    def ok_del(self):
        self.con = sqlite3.connect('piano.db')
        self.cur = self.con.cursor()
        self.cur.execute("""DELETE FROM records WHERE id = (?)""", (self.current_id,))
        self.con.commit()
        self.con.close()
        ex.update_list()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
