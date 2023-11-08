# Tanggal : 07 November 2023
# Waktu : 12:36:38 WIB
# Magnitudo :5.0
# Kedalaman :10
# Lokasi : LS=10.24  BT = 118.07
# Keterangan :124 km BaratDaya KODI-SUMBABARATDAYA-NTT
# Potensi : tidak berpotensi TSUNAMI
from bs4 import BeautifulSoup
import requests



def ekstraksi_data():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    
    if content.status_code == 200:   
        soup = BeautifulSoup(content.text, 'html.parser')

        result =soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        Waktu = result[1]
        Tanggal= result[0]

        result = soup.find('div', {'class', 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        
        i = 0
        Magnitudo = None
        ls = None
        bt = None
        Lokasi = None
        Potensi = None
        for res in result:
            # print(i ,res)
            if i == 1:
                Magnitudo = res.text
            elif i == 2:
                Kedalaman = res.text
            elif i == 3:
                Koordinat = res.text.split(' - ')
                ls = Koordinat[0]
                bt = Koordinat[1]
            elif i == 4:
                Lokasi= res.text
            elif i == 5:
                Potensi = res.text
            i = i + 1


        # print(title.string)

        hasil = dict()
        hasil['Tanggal']= Tanggal #'07 November 2023'
        hasil['Waktu']= Waktu  #'12:36:38 WIB'
        hasil['Magnitudo']= Magnitudo #5.0
        hasil['Kedalaman']= Kedalaman  #10
        hasil['Koordinat']= {'ls' : ls,'bt' : bt}
        # hasil['Lokasi']= {'ls' : ls,'bt' : bt}   # {'ls' : 10.24,'bt' : 118.07}
        hasil['Lokasi']=  Lokasi #'124 km BaratDaya KODI-SUMBABARATDAYA-NTT'
        hasil['Potensi']= Potensi #'tidak berpotensi TSUNAMI'

        return hasil
    else:
        return None



def tampilan_data(result):
    if result is None:
        print("tidak bisa menemukan data gempa terkini")
        return
    
    print(f"Tanggal : {result['Tanggal']}")
    print(f"Waktu : {result['Waktu']}")
    print(f"Magnitudo : {result['Magnitudo']}")
    print(f"Kedalaman : {result['Kedalaman']}")
    print(f"Koordinat : LS = {result['Koordinat']['ls']} BT = {result['Koordinat']['bt']}")
    print(f"Lokasi : {result['Lokasi']}")
    print(f"Potensi : {result['Potensi']}")

if __name__ == '__main__':
    print("aplikasi utama")
    
