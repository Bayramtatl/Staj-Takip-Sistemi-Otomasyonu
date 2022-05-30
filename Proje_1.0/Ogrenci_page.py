from PyQt5.QtWidgets import*
from Ogrenci_python import Ui_Form_Ogrenci
from ogrenci import Ogrenci
class Arayuz_Ogrenci(QWidget):
    def __init__(self,veri):
        super().__init__()
        self.ui = Ui_Form_Ogrenci()  # classın adını girdik uideki
        self.ui.setupUi(self)
        self.veri = veri
        self.ui.pushButton_OgrBilgileri.clicked.connect(lambda: self.BilgilerimiGoster())
        self.ui.pushButton_OgrtmnBilgileri.clicked.connect(lambda: self.DanismanBilgileriniGoster())
        self.ogrenci1 = Ogrenci(self.veri[1],self.veri[2],self.veri[3],self.veri[4],self.veri[5],self.veri[6],self.veri[7],self.veri[8],self.veri[9],self.veri[10])
        self.listem = []
        self.listem2= []
    def BilgilerimiGoster(self): # Fonksiyonun içi ayarlanacak veri tabanına göre
        self.bilgiler = self.ogrenci1.bilgilerimi_goster(self.ogrenci1.ogrenci_no)
        for i in self.bilgiler:
            for a in i:
                self.listem.append(a)
        self.ui.label_OgrNo.setText("Öğrenci No :")
        self.ui.lineEdit_Ad.setText(str(self.listem[1]))
        self.ui.lineEdit_Soyad.setText(str(self.listem[2]))
        self.ui.lineEdit_OgrNo.setText(str(self.listem[3]))
        self.ui.lineEdit_Fakulte.setText(str(self.listem[5]))
        self.ui.lineEdit_Bolum.setText(str(self.listem[6]))
        self.ui.lineEdit_StajTuru.setText(str(self.listem[7]))
        self.ui.lineEdit_KabulEdlGun.setText(str(self.listem[8]))
        self.ui.lineEdit_KablEdlmynGun.setText(str(self.listem[9]))
    def DanismanBilgileriniGoster(self):
        self.ogrbilgiler = self.ogrenci1.danisman_bilgilerimi_goster(self.ogrenci1.ogrenci_no)
        for i in self.ogrbilgiler:
            for a in i:
                self.listem2.append(a)
        self.ui.label_OgrNo.setText("Sicil No :")
        self.ui.lineEdit_Ad.setText(str(self.listem2[0]))
        self.ui.lineEdit_Soyad.setText(str(self.listem2[1]))
        self.ui.lineEdit_OgrNo.setText(str(self.listem2[2]))
        self.ui.lineEdit_Fakulte.setText(str(self.listem2[3]))
        self.ui.lineEdit_Bolum.setText(str(self.listem2[4]))
        self.ui.lineEdit_StajTuru.clear()
        self.ui.lineEdit_KabulEdlGun.clear()
        self.ui.lineEdit_KablEdlmynGun.clear()
