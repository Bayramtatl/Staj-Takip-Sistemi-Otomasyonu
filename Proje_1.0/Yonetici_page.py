from PyQt5.QtWidgets import*
from Yonetici_python import Ui_Form_Yonetici
from yonetici import Yonetici
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
class Arayuz_Yonetici(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_Yonetici()  # classın adını girdik uideki
        self.ui.setupUi(self)  # uideki setup fonksiyonunu çağırdık
        self.ui.pushButton_Cikis.clicked.connect(self.cikisYap)
        self.ui.pushButton_OgretmenEkle.clicked.connect(lambda: self.ogretmenEklee())
        self.ui.pushButton_OgretmenSil.clicked.connect(lambda: self.ogretmenSill())
        self.ui.lineEdit_SicilNo.setValidator(QIntValidator(0,99999,self))
        self.ui.label_Toolbar_BosAlan.close()
        self.ui.label_Toolbar_Sifre.close()
        self.ui.label_Toolbar_Sil.close()
        self.ui.label_Toolbar_Ekle.close()
        self.ui.label_Toolbar_Sifre_Krktr.close()
        self.ui.label_Toolbar_SilHata.close()
        self.yoneticitest = Yonetici("admin", "admin")
    def ogretmenEklee(self):
        self.bos = ""
        if self.ui.lineEdit_Ogr_Adi.text() == self.bos or self.ui.lineEdit_Ogr_SoyAdi.text() == self.bos:
            QMessageBox.critical(self,"Ekleme Yapılamadı","Ekleme Yaparken Boş Bir Alan Bırakmayınız !")
        elif self.ui.lineEdit_Sifre.text() != self.ui.lineEdit_Sifre_Tekrar.text():
            self.ui.label_Toolbar_Ekle.close()
            self.ui.label_Toolbar_Sil.close()
            self.ui.label_Toolbar_Sifre_Krktr.close()
            self.ui.label_Toolbar_SilHata.close()
            self.ui.label_Toolbar_Sifre.show()
        elif self.ui.lineEdit_Sifre.text() == self.bos or self.ui.lineEdit_Sifre_Tekrar.text() == self.bos:
            self.ui.label_Toolbar_Ekle.close()
            self.ui.label_Toolbar_Sil.close()
            self.ui.label_Toolbar_Sifre.close()
            self.ui.label_Toolbar_SilHata.close()
            self.ui.label_Toolbar_Sifre_Krktr.show()
        else:
            self.ui.label_Toolbar_Sifre.close()
            self.ui.label_Toolbar_Sil.close()
            self.ui.label_Toolbar_Sifre_Krktr.close()
            self.ui.label_Toolbar_SilHata.close()
            self.ui.label_Toolbar_Ekle.show()
            self.yoneticitest.ogretmenEkle(self.ui.lineEdit_Ogr_Adi.text(),self.ui.lineEdit_Ogr_SoyAdi.text()
                                           ,self.ui.lineEdit_SicilNo.text(),self.ui.lineEdit_Sifre.text())
    def ogretmenSill(self):
        bos = ""
        if self.ui.lineEdit_Sifre.text() != self.ui.lineEdit_Sifre_Tekrar.text():# Şifreler uyuşmuyorsa
            self.ui.label_Toolbar_Ekle.close()
            self.ui.label_Toolbar_Sil.close()
            self.ui.label_Toolbar_Sifre_Krktr.close()
            self.ui.label_Toolbar_SilHata.close()
            self.ui.label_Toolbar_Sifre.show()
        elif self.ui.lineEdit_Sifre.text() == bos or self.ui.lineEdit_Sifre_Tekrar.text() == bos:# Şifre null ise
            self.ui.label_Toolbar_Ekle.close()
            self.ui.label_Toolbar_Sil.close()
            self.ui.label_Toolbar_Sifre.close()
            self.ui.label_Toolbar_SilHata.close()
            self.ui.label_Toolbar_Sifre_Krktr.show()
        else: # Sifreler uyumlu ve kayıt silinecek
            self.d=self.yoneticitest.ogretmenSil(self.ui.lineEdit_SicilNo.text())
            if self.d == None:
                self.ui.label_Toolbar_Sifre.close()
                self.ui.label_Toolbar_Ekle.close()
                self.ui.label_Toolbar_Sifre_Krktr.close()
                self.ui.label_Toolbar_Sil.close()
                self.ui.label_Toolbar_SilHata.show()
            else:
                self.ui.label_Toolbar_Sifre.close()
                self.ui.label_Toolbar_Ekle.close()
                self.ui.label_Toolbar_Sifre_Krktr.close()
                self.ui.label_Toolbar_Sil.show()
                self.ui.label_Toolbar_SilHata.close()
    def cikisYap(self):
        self.close()



