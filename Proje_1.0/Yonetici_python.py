# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Bayram/Desktop/Proje_1.0/Yonetici.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Yonetici(object):
    def setupUi(self, Form_Yonetici):
        Form_Yonetici.setObjectName("Form_Yonetici")
        Form_Yonetici.setEnabled(True)
        Form_Yonetici.resize(540, 420)
        Form_Yonetici.setMinimumSize(QtCore.QSize(540, 420))
        Form_Yonetici.setMaximumSize(QtCore.QSize(540, 420))
        Form_Yonetici.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form_Yonetici.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_iki = QtWidgets.QLabel(Form_Yonetici)
        self.label_iki.setGeometry(QtCore.QRect(140, 0, 201, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_iki.setFont(font)
        self.label_iki.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(140, 140, 140);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_iki.setObjectName("label_iki")
        self.pushButton_OgretmenEkle = QtWidgets.QPushButton(Form_Yonetici)
        self.pushButton_OgretmenEkle.setEnabled(True)
        self.pushButton_OgretmenEkle.setGeometry(QtCore.QRect(200, 350, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_OgretmenEkle.setFont(font)
        self.pushButton_OgretmenEkle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_OgretmenEkle.setStyleSheet("selection-color: rgb(255, 255, 127);\n"
"background-color: rgb(0, 170, 255);\n"
"")
        self.pushButton_OgretmenEkle.setObjectName("pushButton_OgretmenEkle")
        self.pushButton_OgretmenSil = QtWidgets.QPushButton(Form_Yonetici)
        self.pushButton_OgretmenSil.setGeometry(QtCore.QRect(300, 350, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_OgretmenSil.setFont(font)
        self.pushButton_OgretmenSil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_OgretmenSil.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_OgretmenSil.setObjectName("pushButton_OgretmenSil")
        self.pushButton_Cikis = QtWidgets.QPushButton(Form_Yonetici)
        self.pushButton_Cikis.setGeometry(QtCore.QRect(400, 350, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Cikis.setFont(font)
        self.pushButton_Cikis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Cikis.setObjectName("pushButton_Cikis")
        self.label_Id = QtWidgets.QLabel(Form_Yonetici)
        self.label_Id.setGeometry(QtCore.QRect(20, 180, 145, 35))
        self.label_Id.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(140, 140, 140);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_Id.setObjectName("label_Id")
        self.label_Sifre = QtWidgets.QLabel(Form_Yonetici)
        self.label_Sifre.setGeometry(QtCore.QRect(20, 230, 145, 35))
        self.label_Sifre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(140, 140, 140);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_Sifre.setObjectName("label_Sifre")
        self.label_SifreTekrar = QtWidgets.QLabel(Form_Yonetici)
        self.label_SifreTekrar.setGeometry(QtCore.QRect(20, 280, 145, 35))
        self.label_SifreTekrar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(140, 140, 140);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_SifreTekrar.setObjectName("label_SifreTekrar")
        self.lineEdit_SicilNo = QtWidgets.QLineEdit(Form_Yonetici)
        self.lineEdit_SicilNo.setGeometry(QtCore.QRect(230, 180, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_SicilNo.setFont(font)
        self.lineEdit_SicilNo.setStyleSheet("border-color: rgb(144, 144, 144);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_SicilNo.setObjectName("lineEdit_SicilNo")
        self.lineEdit_Sifre = QtWidgets.QLineEdit(Form_Yonetici)
        self.lineEdit_Sifre.setGeometry(QtCore.QRect(230, 230, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Sifre.setFont(font)
        self.lineEdit_Sifre.setStyleSheet("border-color: rgb(144, 144, 144);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_Sifre.setObjectName("lineEdit_Sifre")
        self.lineEdit_Sifre_Tekrar = QtWidgets.QLineEdit(Form_Yonetici)
        self.lineEdit_Sifre_Tekrar.setGeometry(QtCore.QRect(230, 280, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Sifre_Tekrar.setFont(font)
        self.lineEdit_Sifre_Tekrar.setStyleSheet("border-color: rgb(144, 144, 144);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_Sifre_Tekrar.setObjectName("lineEdit_Sifre_Tekrar")
        self.label_Toolbar_Sifre = QtWidgets.QLabel(Form_Yonetici)
        self.label_Toolbar_Sifre.setGeometry(QtCore.QRect(380, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Toolbar_Sifre.setFont(font)
        self.label_Toolbar_Sifre.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_Toolbar_Sifre.setObjectName("label_Toolbar_Sifre")
        self.label_Toolbar_Ekle = QtWidgets.QLabel(Form_Yonetici)
        self.label_Toolbar_Ekle.setGeometry(QtCore.QRect(160, 390, 141, 31))
        self.label_Toolbar_Ekle.setObjectName("label_Toolbar_Ekle")
        self.label_Toolbar_Sil = QtWidgets.QLabel(Form_Yonetici)
        self.label_Toolbar_Sil.setEnabled(True)
        self.label_Toolbar_Sil.setGeometry(QtCore.QRect(280, 390, 141, 31))
        self.label_Toolbar_Sil.setObjectName("label_Toolbar_Sil")
        self.label_Toolbar_Sifre_Krktr = QtWidgets.QLabel(Form_Yonetici)
        self.label_Toolbar_Sifre_Krktr.setGeometry(QtCore.QRect(380, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Toolbar_Sifre_Krktr.setFont(font)
        self.label_Toolbar_Sifre_Krktr.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_Toolbar_Sifre_Krktr.setObjectName("label_Toolbar_Sifre_Krktr")
        self.lineEdit_Ogr_Adi = QtWidgets.QLineEdit(Form_Yonetici)
        self.lineEdit_Ogr_Adi.setGeometry(QtCore.QRect(230, 80, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Ogr_Adi.setFont(font)
        self.lineEdit_Ogr_Adi.setStyleSheet("border-color: rgb(144, 144, 144);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_Ogr_Adi.setObjectName("lineEdit_Ogr_Adi")
        self.lineEdit_Ogr_SoyAdi = QtWidgets.QLineEdit(Form_Yonetici)
        self.lineEdit_Ogr_SoyAdi.setGeometry(QtCore.QRect(230, 130, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Ogr_SoyAdi.setFont(font)
        self.lineEdit_Ogr_SoyAdi.setStyleSheet("border-color: rgb(144, 144, 144);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_Ogr_SoyAdi.setObjectName("lineEdit_Ogr_SoyAdi")
        self.label_Id_2 = QtWidgets.QLabel(Form_Yonetici)
        self.label_Id_2.setGeometry(QtCore.QRect(20, 80, 145, 35))
        self.label_Id_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(140, 140, 140);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_Id_2.setObjectName("label_Id_2")
        self.label_Id_3 = QtWidgets.QLabel(Form_Yonetici)
        self.label_Id_3.setGeometry(QtCore.QRect(20, 130, 145, 35))
        self.label_Id_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(140, 140, 140);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_Id_3.setObjectName("label_Id_3")
        self.label_Toolbar_SilHata = QtWidgets.QLabel(Form_Yonetici)
        self.label_Toolbar_SilHata.setGeometry(QtCore.QRect(190, 320, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Toolbar_SilHata.setFont(font)
        self.label_Toolbar_SilHata.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_Toolbar_SilHata.setObjectName("label_Toolbar_SilHata")
        self.label_Toolbar_BosAlan = QtWidgets.QLabel(Form_Yonetici)
        self.label_Toolbar_BosAlan.setGeometry(QtCore.QRect(190, 320, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Toolbar_BosAlan.setFont(font)
        self.label_Toolbar_BosAlan.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_Toolbar_BosAlan.setObjectName("label_Toolbar_BosAlan")

        self.retranslateUi(Form_Yonetici)
        QtCore.QMetaObject.connectSlotsByName(Form_Yonetici)

    def retranslateUi(self, Form_Yonetici):
        _translate = QtCore.QCoreApplication.translate
        Form_Yonetici.setWindowTitle(_translate("Form_Yonetici", "Yönetici Paneli"))
        self.label_iki.setText(_translate("Form_Yonetici", "    Yönetici Paneli"))
        self.pushButton_OgretmenEkle.setText(_translate("Form_Yonetici", "Öğretmen Ekle"))
        self.pushButton_OgretmenSil.setText(_translate("Form_Yonetici", "Öğretmen Sil"))
        self.pushButton_Cikis.setText(_translate("Form_Yonetici", "Çıkış Yap"))
        self.label_Id.setText(_translate("Form_Yonetici", "Sicil No : "))
        self.label_Sifre.setText(_translate("Form_Yonetici", "Şifre : "))
        self.label_SifreTekrar.setText(_translate("Form_Yonetici", "Şifre Tekrar : "))
        self.lineEdit_Sifre.setPlaceholderText(_translate("Form_Yonetici", "Şifreler aynı olmalı"))
        self.lineEdit_Sifre_Tekrar.setPlaceholderText(_translate("Form_Yonetici", "Şifreler aynı olmalı"))
        self.label_Toolbar_Sifre.setText(_translate("Form_Yonetici", "Girdiğiniz şifreler uyuşmuyor !"))
        self.label_Toolbar_Ekle.setText(_translate("Form_Yonetici", "Öğretmen Başarıyla eklendi"))
        self.label_Toolbar_Sil.setText(_translate("Form_Yonetici", "Öğretmen Başarıyla Silindi"))
        self.label_Toolbar_Sifre_Krktr.setText(_translate("Form_Yonetici", "Şifre  ekranı boş kalamaz !"))
        self.label_Id_2.setText(_translate("Form_Yonetici", "Öğr. Adı : "))
        self.label_Id_3.setText(_translate("Form_Yonetici", "Öğr. Soyadı : "))
        self.label_Toolbar_SilHata.setText(_translate("Form_Yonetici", "Girdiğiniz Sicil No\'da bir öğretmen bulunmamaktadır !"))
        self.label_Toolbar_BosAlan.setText(_translate("Form_Yonetici", "Ekleme Yapılamadı. Lütfen boş bir alan bırakmayınız !"))

