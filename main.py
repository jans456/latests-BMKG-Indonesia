#Deteksi Gempa-Dini (scraping BMKG)
# modulrasi aplikasi python
import gempaterkini



if __name__ == '__main__':
    print("aplikasi utama")
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilan_data(result)
