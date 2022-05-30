from PyQt5.QtWidgets import*
from Ogretmen_python import Ui_Form_Ogretmen
from PyQt5.QtGui import QIntValidator
from ogretmen import Ogretmen
import sqlite3
class Arayuz_Ogretmen(QWidget):
    def __init__(self,veri):
        super().__init__()
        self.ui = Ui_Form_Ogretmen()  # classın adını girdik uideki
        self.ui.setupUi(self)  # uideki setup fonksiyonunu çağırdık
        self.conn = sqlite3.connect("ogrenci_staj_projesi.db")
        self.c = self.conn.cursor()
        self.veri = veri
        self.ui.lineEdit_OgrNo.setValidator(QIntValidator(0,99999,self))
        self.ui.lineEdit_Tcno.setValidator(QIntValidator(0,99999999999,self))
        self.ui.lineEdit_Kabul_Edl_Gun.setValidator(QIntValidator(0,120,self))
        self.ui.lineEdit_Kabul_Edilm_Gun.setValidator(QIntValidator(0,120,self))
        self.ui.comboBox_Fakulte.addItem("Seciniz",-1)
        self.ui.comboBox_Fakulte.addItem("Muhendislik Fakultesi",0)
        self.ui.comboBox_Fakulte.addItem("Egitim Fakultesi", 1)
        self.ui.comboBox_Fakulte.setCurrentIndex(0)
        self.fakulteSecimi = self.ui.comboBox_Fakulte.currentData()
        self.ui.comboBox_Fakulte.currentIndexChanged.connect(self.comboAyarla)
        self.ui.pushButton_Kaydet.clicked.connect(lambda: self.OgrEkle())
        self.ui.pushButton_Duzenle.clicked.connect(lambda: self.OgrDuzenle())
        self.ui.pushButton_Sil.clicked.connect(lambda: self.OgrSil())
        self.ui.comboBox_Sorgu.currentTextChanged.connect(lambda: self.SorguGuncelle())
        self.ui.label_Ogr_BosAlan.close()
        self.ui.label_EklemeBasarili.close()
        self.ui.label_SilmeBasarili.close()
        self.ui.label_Ogr_NoBos.close()
        self.ui.label_FakulteSecin.close()
        self.ui.label_Kayitli.close()
        self.ogrid = ""
        self.liste = []
        self.bos = ""
        self.ogretmenid =""
        self.ogretmen1 = Ogretmen(self.veri[1],self.veri[2],self.veri[3],self.veri[4])
        self.listem = []
        self.liste = self.ogretmen1.butunOgrenciler(self.ogretmen1.sicil_no)
        self.ui.comboBox_Sorgu.addItem("Seciniz")
        for i in self.liste:
            for a in i:
                self.ui.comboBox_Sorgu.addItem(str(a))
    def SorguGuncelle(self): ## Line editlere sorgu yapılan öğrenci bilgilerini yerleştirir.
        if self.ui.comboBox_Sorgu.currentText() != "":# Silme işleminden sonra sorgu yapmaması için
            if self.ui.comboBox_Sorgu.currentText() != "Seciniz":
                self.ogretmen1 = Ogretmen(self.veri[1],self.veri[2],self.veri[3],self.veri[4])
                self.listem.clear()
                self.bilgiList = self.ogretmen1.ogrenci_sorgu(self.ui.comboBox_Sorgu.currentText())
                for i in self.bilgiList:
                    for a in i:
                        self.listem.append(a)
                self.ui.lineEdit_Adi.setText(str(self.listem[0]))
                self.ui.lineEdit_Soyadi.setText(str(self.listem[1]))
                self.ui.lineEdit_OgrNo.setText(str(self.listem[2]))
                self.ui.lineEdit_Tcno.setText(str(self.listem[3]))
                self.ui.comboBox_Fakulte.setCurrentText(str(self.listem[4]))
                self.ui.comboBox_Bolum.setCurrentText(str(self.listem[5]))
                self.ui.comboBox_StajTuru.setCurrentText(str(self.listem[6]))
                self.ui.lineEdit_Kabul_Edl_Gun.setText(str(self.listem[7]))
                self.ui.lineEdit_Kabul_Edilm_Gun.setText(str(self.listem[8]))

    def comboAyarla(self): # Fakulte secimine göre bölümlerin güncellenmesini sağlar
        self.fakulteSecimi = self.ui.comboBox_Fakulte.currentData()
        self.ui.comboBox_Bolum.showPopup()
        if self.fakulteSecimi == 0:
            self.ui.comboBox_Bolum.clear()
            self.ui.comboBox_Bolum.addItems(
                ["Bilgisayar Mühendisliği", "Makine Mühendisliği", "İnşaat Mühendisliği", "Tekstil Mühendisliği"])
        elif self.fakulteSecimi == 1:
            self.ui.comboBox_Bolum.clear()
            self.ui.comboBox_Bolum.addItems(
                ["Türkçe Öğretmenliği", "Matematik Öğretmenliği", "Okul-Öncesi Öğretmenliği", "Sınıf Öğretmenliği"])

    def OgrEkle(self):
        if self.ui.lineEdit_Adi.text()==self.bos or self.ui.lineEdit_Soyadi.text()==self.bos or self.ui.lineEdit_OgrNo.text()==self.bos or self.ui.lineEdit_Tcno.text()==self.bos or self.ui.lineEdit_Kabul_Edl_Gun.text()==self.bos or self.ui.lineEdit_Kabul_Edilm_Gun.text() ==self.bos:
            self.ui.label_Ogr_BosAlan.show()
            self.ui.label_EklemeBasarili.close()
            self.ui.label_FakulteSecin.close()
        elif self.ui.comboBox_Fakulte.currentText() == "Seciniz":
            self.ui.label_FakulteSecin.show()

        else:
            self.ogretmen1.ogrenci_ekle(self.ui.lineEdit_Adi.text(),self.ui.lineEdit_Soyadi.text(),
                                        self.ui.lineEdit_OgrNo.text(),self.ui.lineEdit_Tcno.text(),
                                        self.ui.comboBox_Fakulte.currentText(),self.ui.comboBox_Bolum.currentText(),
                                        self.ui.comboBox_StajTuru.currentText(),self.ui.lineEdit_Kabul_Edl_Gun.text(),
                                        self.ui.lineEdit_Kabul_Edilm_Gun.text(),self.veri [0],self.ui.comboBox_Sorgu.addItem,self.ui.label_Kayitli,self.ui.label_EklemeBasarili)
            self.ui.label_Ogr_BosAlan.close()
            self.ui.label_FakulteSecin.close()

    def OgrDuzenle(self):
        self.ui.label_Kayitli.close()
        self.ui.label_EklemeBasarili.close()
        self.ogretmen1.ogrenci_duzenle(self.ui.comboBox_Sorgu.currentText(),self.ui.lineEdit_Adi.text(),
                                       self.ui.lineEdit_Soyadi.text(),
                                       self.ui.lineEdit_OgrNo.text(),self.ui.lineEdit_Tcno.text(),
                                       self.ui.comboBox_Fakulte.currentText(),self.ui.comboBox_Bolum.currentText(),
                                       self.ui.comboBox_StajTuru.currentText(),
                                       self.ui.lineEdit_Kabul_Edl_Gun.text(),self.ui.lineEdit_Kabul_Edilm_Gun.text())
        self.ui.comboBox_Sorgu.clear()
        self.liste = self.ogretmen1.butunOgrenciler(self.ogretmen1.sicil_no)
        self.ui.comboBox_Sorgu.addItem("Seciniz")
        for i in self.liste:
            for a in i:
                self.ui.comboBox_Sorgu.addItem(str(a))

    def OgrSil(self):
        self.ui.label_Kayitli.close()
        if self.ui.lineEdit_OgrNo.text() == self.bos:
            self.ui.label_Ogr_NoBos.show()
            self.ui.label_SilmeBasarili.close()
            self.ui.label_EklemeBasarili.close()
        else:
            self.ui.label_Ogr_NoBos.close()
            self.ui.label_SilmeBasarili.show()
            self.ui.label_EklemeBasarili.close()
            self.ogretmen1.ogrenci_sil(self.ui.lineEdit_OgrNo.text())
            # Silme işleminden sonra combobox'ın güncellenmesi için
            self.ui.comboBox_Sorgu.clear()
            self.liste = self.ogretmen1.butunOgrenciler(self.ogretmen1.sicil_no)
            self.ui.comboBox_Sorgu.addItem("Seciniz")
            for i in self.liste:
                for a in i:
                    self.ui.comboBox_Sorgu.addItem(str(a))