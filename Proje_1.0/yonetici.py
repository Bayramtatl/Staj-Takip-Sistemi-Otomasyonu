import sqlite3
from ogretmen import Ogretmen
conn = sqlite3.connect("ogrenci_staj_projesi.db")
c = conn.cursor()



class Yonetici:
    """ Yonetici class constructor"""
    def __init__(self, kullanici_adi, sifre):
        self.__kullanici_adi = kullanici_adi
        self.__sifre = sifre
        

    def __str__(self):
        return f""" 
                Kullanici adi: {self.__kullanici_adi}
                Sifre {self.__sifre}
               """

    def __repr__(self):
        return f"Yonetici('{self.__kullanici_adi}','{self.__sifre}')"       


    @property
    def kullanici_adi(self):
        return self.__kullanici_adi


    @kullanici_adi.setter
    def kullanici_adi(self,yeni_kullanici_adi):
        self.__kullanici_adi = yeni_kullanici_adi


    def ogretmenEkle(self, ad, soyad, sicil_no, sifre):
        """add a new teacher"""
        

        yeniOgretmen = Ogretmen(ad, soyad, sicil_no, sifre)
        c.execute("INSERT INTO ogretmenler(ad,soyad,sicil_no,sifre) VALUES(?,?,?,?)",
        (yeniOgretmen.ad, yeniOgretmen.soyad, yeniOgretmen.sicil_no, yeniOgretmen.sifre))
        conn.commit()
        
        

    def ogretmenSil(self, sicil_no):

        """delete a teacher"""
        conn = sqlite3.connect("ogrenci_staj_projesi.db")
        c = conn.cursor()
        c.execute("SELECT * FROM ogretmenler WHERE sicil_no=?",(sicil_no,))

        if (len(c.fetchall())==0):
            conn.close()
            #return 0

        else:
            c.execute("DELETE FROM ogretmenler WHERE sicil_no=?", (sicil_no,))
            conn.commit()
            conn.close()
            return 1



