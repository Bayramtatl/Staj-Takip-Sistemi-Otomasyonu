from PyQt5.QtWidgets import*
from Tasarım_python import Ui_Form
from PyQt5.QtGui import QIcon
from Yonetici_page import Arayuz_Yonetici
from Ogretmen_page import Arayuz_Ogretmen
from Ogrenci_page import Arayuz_Ogrenci
import sqlite3

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # classın adını girdik uideki
        self.ui.setupUi(self)  # uideki setup fonksiyonunu çağırdık
        self.conn = sqlite3.connect("ogrenci_staj_projesi.db")
        self.c = self.conn.cursor()
        self.setWindowIcon(QIcon ("login.jpg"))
        self.yonetici_page = Arayuz_Yonetici()
        self.ui.radioButton_Ogrenci.clicked.connect(lambda: self.ogrenciSecildi())
        self.ui.radioButton_Ogretmen.clicked.connect(lambda: self.ogretmenSecildi())
        self.ui.radioButton_Yonetici.clicked.connect(lambda: self.yoneticiSecildi())
        self.ui.pushButton_Giris.clicked.connect(lambda: self.girisYap())# Giriş butonuna tıklandığında
        self.giristuru = -1
        self.ui.label_GirisTuru.close()
        self.ui.label_hata.close()
    # Öğrenci radiobutonunun seçilmesi durumunda çalışır.
    def ogrenciSecildi(self):
        self.ui.label_Id.setText("Öğrenci No : ")
        self.giristuru = 2
        self.ui.lineEdit_Sifre.setPlaceholderText("Şifreniz Tc No'nuzdur.")
        self.ui.label_GirisTuru.close()
    # Öğretmen radiobutonunun seçilmesi durumunda çalışır.
    def ogretmenSecildi(self):
        self.ui.label_Id.setText("Sicil No : ")
        self.giristuru = 1
        self.ui.lineEdit_Sifre.setPlaceholderText("")
        self.ui.label_GirisTuru.close()
    # Yönetici radiobutonunun seçilmesi durumunda çalışır.
    def yoneticiSecildi(self):
        self.ui.label_Id.setText("Kullanıcı Adı : ")
        self.giristuru = 0
        self.ui.lineEdit_Sifre.setPlaceholderText("")
        self.ui.label_GirisTuru.close()
    def girisYap(self): # Giriş türüne göre fonksiyon çağırıyor.
        if self.giristuru == -1:
            self.ui.label_GirisTuru.show()
        if self.giristuru ==0:
            if self.ui.lineEdit_ID.text() == "admin" and self.ui.lineEdit_Sifre.text() == "admin":
                self.open_yonetici_page()
            else:
                self.ui.label_hata.show()
        elif self.giristuru == 1:
            if self.ogretmenLogin(self.ui.lineEdit_ID.text(), self.ui.lineEdit_Sifre.text()) == 1:
                self.ogretmen_page = Arayuz_Ogretmen(self.ogretmenBilgi(self.ui.lineEdit_ID.text()))
                self.open_ogretmen_page()
                self.ui.label_hata.close()
            else:
                self.ui.label_hata.show()
        elif self.giristuru ==2:
            if self.ogrenciLogin(self.ui.lineEdit_ID.text(), self.ui.lineEdit_Sifre.text()) == 1:
                self.ogrenci_page = Arayuz_Ogrenci(self.ogrenciBilgi(self.ui.lineEdit_ID.text()))
                self.open_ogrenci_page()
                self.ui.label_hata.close()
            else:
                self.ui.label_hata.show()

    def open_yonetici_page(self): # yönetici penceresini açmak için
        self.yonetici_page.show()
    def open_ogretmen_page(self): # öğretmen penceresini açmak için
        self.ogretmen_page.show()
    def open_ogrenci_page(self): # öğrenci pencereyi açmak için
        self.ogrenci_page.show()
    def ogretmenLogin(self, sicil_no, sifre):
        self.c.execute("SELECT * from ogretmenler WHERE sicil_no=? AND sifre=?", (sicil_no, sifre))
        if len(self.c.fetchall()) == 0:
            return 0
        else:
            return 1

    def ogretmenBilgi(self, sicil_no):
        self.c.execute("SELECT * FROM ogretmenler WHERE sicil_no=?", (sicil_no,))
        ogretmenBilgi = self.c.fetchone()
        return ogretmenBilgi

    def ogrenciLogin(self, ogrenci_no, tc_no):
        self.c.execute("SELECT * from ogrenciler WHERE ogrenci_no=? AND tc_no=?", (ogrenci_no, tc_no))
        if (len(self.c.fetchall()) == 0):
            return 0
        else:
            return 1

    def ogrenciBilgi(self, ogrenci_no):
        self.c.execute("SELECT * FROM ogrenciler WHERE ogrenci_no=?", (ogrenci_no,))
        ogrenciBilgi = self.c.fetchone()
        return ogrenciBilgi

uygulama = QApplication([])
pencere = Arayuz()
pencere.show()
uygulama.exec_()
