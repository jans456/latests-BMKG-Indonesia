
def data():
# Tanggal : 08 November 2023
# Waktu : 14:23:47 WIB
# Magnitudo : 5.1
# Kedalaman : 38 km
# Koordinat : LS = 3.47 LS BT = 129.71 BT
# Lokasi : Pusat gempa berada di laut 85 km Tenggara, Maluku Tengah
# Potensi : Dirasakan (Skala MMI): II Masohi
    data_hasil = dict()
    data_hasil['Tanggal'] = '08 November 2023'
    data_hasil['Waktu'] = 'Magnitudo'
    data_hasil['Magnitudo'] = 5.1
    data_hasil['Kedalaman'] = 38
    data_hasil['Koordinat'] = {'LS' : 3.47, 'BT' : 129.71}
    data_hasil['Lokasi'] = 'Pusat gempa berada di laut 85 km Tenggara, Maluku Tengah'
    data_hasil['Potensi'] = 'Dirasakan (Skala MMI): II Masohi'

    return data_hasil


def tampilkan_data(result):
    print(f"tanggal: {result['Tanggal']}")
    print(f"Waktu : {result['Waktu']}")
    print(f"Magnitudo : {result['Magnitudo']}")
    print(f"Kedalaman :{result['Kedalaman']}")
    print(f"Koordinat : LS= {result['Koordinat']['LS']} BT {result['Koordinat']['BT']}")
    print(f"Lokasi : {result['Lokasi']}")
    print(f"Potensi : {result['Potensi']}")
    



if __name__ == '__main__':
    print("struktur Scraping BMKG")
    result = data()
    tampilkan_data (result)
