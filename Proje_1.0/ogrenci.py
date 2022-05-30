import sqlite3

conn = sqlite3.connect("ogrenci_staj_projesi.db")
c = conn.cursor()

class Ogrenci:

    def __init__(self, ad, soyad , ogrenci_no ,tc_no , fakulte, bolum, staj_turu, kabul_edilen_gun, kabul_edilmeyen_gun, ogretmen_id):

        """Ogrenci class constructor"""

        self.__ad = ad
        self.__soyad = soyad
        self.__ogrenci_no = ogrenci_no
        self.__tc_no = tc_no
        self.__fakulte = fakulte
        self.__bolum = bolum
        self.__staj_turu = staj_turu
        self.__kabul_edilen_gun = kabul_edilen_gun
        self.__kabul_edilmeyen_gun = kabul_edilmeyen_gun
        self.__ogretmen_id = ogretmen_id
        self.conn = sqlite3.connect("ogrenci_staj_projesi.db")
        self.c = self.conn.cursor()


    def __str__(self):
        return f""" 
                Ad: {self.__ad}
                Soyad: {self.__soyad}  
                Öğrenci_no: {self.__ogrenci_no}
                TC_no: {self.__tc_no}
                Fakülte: {self.__fakulte}
                Bölüm: {self.__bolum}
                Kabul edilen gün: {self.__kabul_edilen_gun}
                Kabul edilmeyen gün: {self.__kabul_edilmeyen_gun}

               """
    def __repr__(self):
        return f"Ogrenci('{self.__ad}','{self.__soyad}',{self.__ogrenci_no},{self.__tc_no},'{self.__fakulte}','{self.bolum}',{self.__kabul_edilen_gun},{self.__kabul_edilmeyen_gun})"    


    #variable ad getter setter

    @property
    def ad(self):

        return self.__ad

    @ad.setter
    def ad(self, yeniAd):

        self.__ad = yeniAd 

    
    #variable soyad getter setter

    @property
    def soyad(self):

        return self.__soyad


    @soyad.setter
    def soyad(self, yeniSoyad):

        self.__soyad = yeniSoyad 
  

    #variable ogrenci_no getter setter

    @property
    def ogrenci_no(self):

        return self.__ogrenci_no


    @ogrenci_no.setter
    def ogrenci_no(self, yeniNo):

        self.__ogrenci_no = yeniNo 


    #variable tc_no getter setter


    @property
    def tc_no(self):

        return self.__tc_no


    @tc_no.setter
    def tc_no(self, yeniTc):

        self.__tc_no = yeniTc


    #variable fakulte getter setter

    @property
    def fakulte(self):

        return self.__fakulte


    @fakulte.setter
    def fakulte(self, yeniFakulte):

        self.__fakulte = yeniFakulte


    #variable fakulte getter setter

    @property
    def bolum(self):

        return self.__bolum


    @bolum.setter
    def bolum(self, yeniBolum):

        self.__bolum = yeniBolum


     #variable staj_turu getter setter

    @property
    def staj_turu(self):
        return self.__staj_turu


    @staj_turu.setter
    def staj_turu(self, yeni_staj_turu):
        self.__staj_turu = yeni_staj_turu


    #variable kabul_edilen_gun getter setter

    @property
    def kabul_edilen_gun(self):

        return self.__kabul_edilen_gun


    @kabul_edilen_gun.setter
    def kabul_edilen_gun(self, yeni_kabul_gun):

        self.__kabul_edilen_gun = yeni_kabul_gun 


     #variable kabul_edilmeyen_gun getter setter

    @property
    def kabul_edilmeyen_gun(self):

        return self.__kabul_edilmeyen_gun


    @kabul_edilmeyen_gun.setter
    def kabul_edilmeyen_gun(self, yeni_kabul_edilmeyen_gun):
        self.__kabul_edilmeyen_gun = yeni_kabul_edilmeyen_gun


    @property
    def ogretmen_id(self):

        return self.__ogretmen_id


    @ogretmen_id.setter
    def ogretmen_id(self, yeni_ogretmen_id):
        self.__ogretmen_id = yeni_ogretmen_id


    
    def bilgilerimi_goster(self, ogrenci_no):
        """ get the student's information """
        self.conn = sqlite3.connect("ogrenci_staj_projesi.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM ogrenciler WHERE ogrenci_no=?",(ogrenci_no,))

        ogrenciVerisi = self.c.fetchall()


        return ogrenciVerisi
        
        

    def danisman_bilgilerimi_goster(self,ogrenci_no):
        """ get the teacher's information """

        self.c.execute("""SELECT ogretmenler.ad,
        ogretmenler.soyad,
        ogretmenler.sicil_no,
        ogrenciler.fakulte,
        ogrenciler.bolum
        FROM ogrenciler JOIN ogretmenler ON ogrenciler.ogretmen_id == ogretmenler.id
        where ogrenci_no=?""",(ogrenci_no,))

        danismanVeri = self.c.fetchall()

        return danismanVeri  




