# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Bayram/Desktop/Proje_1.0/Ogrenci.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Ogrenci(object):
    def setupUi(self, Form_Ogrenci):
        Form_Ogrenci.setObjectName("Form_Ogrenci")
        Form_Ogrenci.resize(490, 490)
        Form_Ogrenci.setMinimumSize(QtCore.QSize(490, 490))
        Form_Ogrenci.setMaximumSize(QtCore.QSize(490, 490))
        Form_Ogrenci.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label = QtWidgets.QLabel(Form_Ogrenci)
        self.label.setGeometry(QtCore.QRect(40, 80, 150, 30))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.label.setObjectName("label")
        self.label_OgrNo = QtWidgets.QLabel(Form_Ogrenci)
        self.label_OgrNo.setGeometry(QtCore.QRect(40, 180, 150, 30))
        self.label_OgrNo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.label_OgrNo.setObjectName("label_OgrNo")
        self.label_4 = QtWidgets.QLabel(Form_Ogrenci)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 150, 30))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form_Ogrenci)
        self.label_5.setGeometry(QtCore.QRect(40, 280, 150, 30))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form_Ogrenci)
        self.label_6.setGeometry(QtCore.QRect(40, 330, 150, 30))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form_Ogrenci)
        self.label_7.setGeometry(QtCore.QRect(40, 380, 150, 30))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form_Ogrenci)
        self.label_8.setGeometry(QtCore.QRect(40, 430, 150, 30))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_Ad = QtWidgets.QLineEdit(Form_Ogrenci)
        self.lineEdit_Ad.setEnabled(False)
        self.lineEdit_Ad.setGeometry(QtCore.QRect(250, 80, 150, 30))
        self.lineEdit_Ad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.lineEdit_Ad.setObjectName("lineEdit_Ad")
        self.lineEdit_OgrNo = QtWidgets.QLineEdit(Form_Ogrenci)
        self.lineEdit_OgrNo.setEnabled(False)
        self.lineEdit_OgrNo.setGeometry(QtCore.QRect(250, 180, 150, 30))
        self.lineEdit_OgrNo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.lineEdit_OgrNo.setObjectName("lineEdit_OgrNo")
        self.lineEdit_Fakulte = QtWidgets.QLineEdit(Form_Ogrenci)
        self.lineEdit_Fakulte.setEnabled(False)
        self.lineEdit_Fakulte.setGeometry(QtCore.QRect(250, 230, 150, 30))
        self.lineEdit_Fakulte.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.lineEdit_Fakulte.setObjectName("lineEdit_Fakulte")
        self.lineEdit_StajTuru = QtWidgets.QLineEdit(Form_Ogrenci)
        self.lineEdit_StajTuru.setEnabled(False)
        self.lineEdit_StajTuru.setGeometry(QtCore.QRect(250, 330, 150, 30))
        self.lineEdit_StajTuru.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.lineEdit_StajTuru.setObjectName("lineEdit_StajTuru")
        self.lineEdit_KabulEdlGun = QtWidgets.QLineEdit(Form_Ogrenci)
        self.lineEdit_KabulEdlGun.setEnabled(False)
        self.lineEdit_KabulEdlGun.setGeometry(QtCore.QRect(250, 380, 150, 30))
        self.lineEdit_KabulEdlGun.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.lineEdit_KabulEdlGun.setObjectName("lineEdit_KabulEdlGun")
        self.lineEdit_KablEdlmynGun = QtWidgets.QLineEdit(Form_Ogrenci)
        self.lineEdit_KablEdlmynGun.setEnabled(False)
        self.lineEdit_KablEdlmynGun.setGeometry(QtCore.QRect(250, 430, 150, 30))
        self.lineEdit_KablEdlmynGun.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.lineEdit_KablEdlmynGun.setObjectName("lineEdit_KablEdlmynGun")
        self.lineEdit_Bolum = QtWidgets.QLineEdit(Form_Ogrenci)
        self.lineEdit_Bolum.setEnabled(False)
        self.lineEdit_Bolum.setGeometry(QtCore.QRect(250, 280, 150, 30))
        self.lineEdit_Bolum.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.lineEdit_Bolum.setObjectName("lineEdit_Bolum")
        self.horizontalFrame = QtWidgets.QFrame(Form_Ogrenci)
        self.horizontalFrame.setGeometry(QtCore.QRect(0, 0, 491, 61))
        self.horizontalFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_OgrBilgileri = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_OgrBilgileri.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_OgrBilgileri.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton_OgrBilgileri.setObjectName("pushButton_OgrBilgileri")
        self.horizontalLayout.addWidget(self.pushButton_OgrBilgileri)
        self.pushButton_OgrtmnBilgileri = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_OgrtmnBilgileri.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_OgrtmnBilgileri.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton_OgrtmnBilgileri.setObjectName("pushButton_OgrtmnBilgileri")
        self.horizontalLayout.addWidget(self.pushButton_OgrtmnBilgileri)
        self.label_3 = QtWidgets.QLabel(Form_Ogrenci)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 150, 30))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_Soyad = QtWidgets.QLineEdit(Form_Ogrenci)
        self.lineEdit_Soyad.setEnabled(False)
        self.lineEdit_Soyad.setGeometry(QtCore.QRect(250, 130, 150, 30))
        self.lineEdit_Soyad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.lineEdit_Soyad.setObjectName("lineEdit_Soyad")

        self.retranslateUi(Form_Ogrenci)
        QtCore.QMetaObject.connectSlotsByName(Form_Ogrenci)

    def retranslateUi(self, Form_Ogrenci):
        _translate = QtCore.QCoreApplication.translate
        Form_Ogrenci.setWindowTitle(_translate("Form_Ogrenci", "Form"))
        self.label.setText(_translate("Form_Ogrenci", "Adı  :"))
        self.label_OgrNo.setText(_translate("Form_Ogrenci", "Öğrenci No : "))
        self.label_4.setText(_translate("Form_Ogrenci", "Fakülte :"))
        self.label_5.setText(_translate("Form_Ogrenci", "Bölüm :"))
        self.label_6.setText(_translate("Form_Ogrenci", "Staj Türü"))
        self.label_7.setText(_translate("Form_Ogrenci", "Kabul Edilen Günler :"))
        self.label_8.setText(_translate("Form_Ogrenci", "Kabul Edilmeyen Günler :"))
        self.pushButton_OgrBilgileri.setText(_translate("Form_Ogrenci", "Öğrenci Bilgileri"))
        self.pushButton_OgrtmnBilgileri.setText(_translate("Form_Ogrenci", "Danışman Öğretmen Bilgileri"))
        self.label_3.setText(_translate("Form_Ogrenci", "Soyadı : "))

