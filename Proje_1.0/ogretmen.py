
import sqlite3
from ogrenci import Ogrenci
conn = sqlite3.connect("ogrenci_staj_projesi.db")
c = conn.cursor()




class Ogretmen:
    def __init__(self,ad,soyad, sicil_no ,sifre):

        """Ogretmen class constructor"""

        self.__ad = ad
        self.__soyad = soyad
        self.__sicil_no = sicil_no
        self.__sifre = sifre
        self.conn = sqlite3.connect("ogrenci_staj_projesi.db")
        self.c = self.conn.cursor()


    def __str__(self):
        return f""" 
                Ad: {self.__ad}
                Soyad: {self.__soyad}  
                Sicil_no: {self.__sicil_no}
                Sifre {self.__sifre}
               """
    def __repr__(self):
        return f"Ogretmen('{self.__ad}','{self.__soyad}',{self.__sicil_no},{self.__sifre})"   


    @property
    def ad(self):
        return self.__ad

    @ad.setter
    def ad(self, yeniAd):
        self.__ad = yeniAd       

    @property
    def soyad(self):
        return self.__soyad

    @soyad.setter
    def soyad(self,yeniSoyad):
        self.__soyad = yeniSoyad

    @property
    def sifre(self):
        return self.__sifre

    @sifre.setter
    def sifre(self, yeniSifre):
        self.__sifre = yeniSifre

    @property
    def sicil_no(self):
        return self.__sicil_no

    @sicil_no.setter
    def sicil_no(self, yeniSicil_no):
        self.__sicil_no = yeniSicil_no   





    def ogrenci_sorgu(self, ogrenci_no):
        """ get a student by his/her information """

        self.c.execute("""SELECT ogrenciler.ad,
        ogrenciler.soyad,
        ogrenciler.ogrenci_no,
        ogrenciler.tc_no,
        ogrenciler.fakulte,
        ogrenciler.bolum,
        ogrenciler.staj_turu,
        ogrenciler.kabul_edilen_gun,
        ogrenciler.kabul_edilmeyen_gun
        FROM ogretmenler
        JOIN ogrenciler ON ogretmenler.id == ogrenciler.ogretmen_id and ogrenci_no=?""",(ogrenci_no,))

        ogrenciVerisi = self.c.fetchall()

        
        return ogrenciVerisi
        
        

    def ogrenci_ekle(self, ad, soyad, ogrenci_no, tc_no, fakulte, bolum, staj_turu, kabul_edilen_gun,
                     kabul_edilmeyen_gun, ogretmen_id, fonk,label,label2):
        """ add a new student """

        self.c.execute("SELECT * FROM ogrenciler WHERE ogrenci_no=? OR tc_no=?", (ogrenci_no,tc_no))
        if (len(self.c.fetchall()) != 0):
            print("HATA")
            label.show()
            label2.close()


        else:

            yeniOgrenci = Ogrenci(ad, soyad, ogrenci_no, tc_no, fakulte, bolum, staj_turu, kabul_edilen_gun,
                                  kabul_edilmeyen_gun, ogretmen_id)

            self.c.execute("""INSERT INTO ogrenciler(ad,
            soyad,
            ogrenci_no,
            tc_no,
            fakulte,
            bolum,
            staj_turu,
            kabul_edilen_gun,
            kabul_edilmeyen_gun,
            ogretmen_id) VALUES(?,?,?,?,?,?,?,?,?,?)""",
                           (yeniOgrenci.ad,
                            yeniOgrenci.soyad,
                            yeniOgrenci.ogrenci_no,
                            yeniOgrenci.tc_no,
                            yeniOgrenci.fakulte,
                            yeniOgrenci.bolum,
                            yeniOgrenci.staj_turu,
                            yeniOgrenci.kabul_edilen_gun,
                            yeniOgrenci.kabul_edilmeyen_gun,
                            yeniOgrenci.ogretmen_id))

            self.conn.commit()
            label.close()
            label2.show()

            fonk(yeniOgrenci.ogrenci_no)
        

    def ogrenci_duzenle(self, ogrenci_no, guncelAd, guncelSoyad, guncelNo, guncelTC, guncelFakulte, guncelBolum,
                        gunceltaj_turu, guncelKabul, guncelKabulEdilmeyen):
        """ edit the student """
        self.c.execute("""UPDATE ogrenciler
        SET ad=ifnull(?,ad), soyad=ifnull(?,soyad), ogrenci_no=ifnull(?,ogrenci_no), tc_no=ifnull(?,tc_no), fakulte=ifnull(?,fakulte), bolum=ifnull(?,bolum), staj_turu=ifnull(?,staj_turu), kabul_edilen_gun=ifnull(?,kabul_edilen_gun), kabul_edilmeyen_gun=ifnull(?,kabul_edilmeyen_gun)
        WHERE ogrenci_no=?""", (
            guncelAd, guncelSoyad, guncelNo, guncelTC, guncelFakulte, guncelBolum, gunceltaj_turu, guncelKabul,
            guncelKabulEdilmeyen, ogrenci_no))
        self.conn.commit()


    def ogrenci_sil(self,ogrenci_no):
        """ delete the student """
        self.c.execute("DELETE from ogrenciler WHERE ogrenci_no=?",(ogrenci_no,))
        self.conn.commit()


    def butunOgrenciler(self, sicil_no):
        self.c.execute("""SELECT ogrenciler.ogrenci_no
        FROM ogrenciler 
        JOIN ogretmenler ON ogrenciler.ogretmen_id == ogretmenler.id WHERE ogretmenler.sicil_no==?""", (sicil_no,))

        butunOgrenciler = self.c.fetchall()

        return butunOgrenciler


    def sistemdeVarmi(self,ogrenci_no, tc_no):
        self.c.execute("SELECT * from ogrenciler WHERE ogrenci_no=? AND tc_no=?", (ogrenci_no, tc_no))
        if (len(self.c.fetchall()) == 0):
            return 0
        else:
            return 1




