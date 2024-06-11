#Deneme,bu bir çok amaçlı yazılımdır.

#Canım Ailem ve kuzenim Nida Ablama teşekkür ediyorum
#Canım babama ve kuzenlerime ayrı ayrı teşekkür ederim

#Bu aralar bir gariplik sezdim.

import os #os kütüphanesini içeri aktardım.
import py_compile #Derleme için derleme kütüphanesi.
import marshal
import struct
while True:
    print("Ota60 Çevirme aracına hoşgeldiniz lütfen seçenek seçin.")

    print()
    print()
    print()
    
    print("1.Dosyanızı ikiliye çevirin.")
    print("2.Dosyayı exe yapın.")
    print("3.Dosyayı derleyin.")
    print("4.Çıkış yapın.")

    com = input("Lütfen seçeneği girin > ")

    if com == "1" :
        def derle_python_dosyasi(kaynak_dosya):
            try:
                # Derleme işlemi
                py_compile.compile(kaynak_dosya, cfile=kaynak_dosya + 'c')
                print(f"{kaynak_dosya} başarıyla {kaynak_dosya + 'c'} olarak derlendi.")
            except Exception as e:
                print(f"Derleme başarısız oldu: {e}")

        def binary():
            pyc_file_path = 'ota.pyc'
            bin_file_path = 'ota.bin'

            # .pyc dosyasını açın ve bayt kodunu okuyun
            with open(pyc_file_path, 'rb') as pyc_file:
                header_size = 16  # İlk 16 baytı (header) atlayacağız
                pyc_file.read(header_size)  # Header'ı atla
                bytecode = pyc_file.read()  # Geri kalan bayt kodunu oku

            # Bayt kodunu .bin dosyasına yazın
            with open(bin_file_path, 'wb') as bin_file:
                bin_file.write(bytecode)

            print(f"Bayt kodu dönüştürüldü ve yazıldı {bin_file_path}")

        def main():
            kaynak_dosya = input("Lütfen derlenecek Python dosyasının adını (ve .py uzantısını) girin: ")
            derle_python_dosyasi(kaynak_dosya)
    
            if not os.path.exists(kaynak_dosya):
                print(f"{kaynak_dosya} adlı dosya mevcut değil.")
                exit()

        binary()

        if __name__ == "__main__":
            main()

    if com == "3" :
        def derle_python_dosyasi(kaynak_dosya):
            try:
                # Derleme işlemi
                py_compile.compile(kaynak_dosya, cfile=kaynak_dosya + 'c')
                print(f"{kaynak_dosya} başarıyla {kaynak_dosya + 'c'} olarak derlendi.")
            except Exception as e:
                print(f"Derleme başarısız oldu: {e}")

        def main():
            kaynak_dosya = input("Lütfen derlenecek Python dosyasının adını (ve .py uzantısını) girin: ")
            derle_python_dosyasi(kaynak_dosya)
    
            if not os.path.exists(kaynak_dosya):
                print(f"{kaynak_dosya} adlı dosya mevcut değil.")
                exit()

        if __name__ == "__main__":
            main()
    if com == "2" :
        def dönüştür_ve_ad_değiştir(py_dosya_adı, exe_dosya_adı):
            try:
                os.system(f'pyinstaller --onefile {py_dosya_adı}')
                exe_adı = os.path.join('dist', os.path.splitext(py_dosya_adı)[0], 'dosya_adı.exe')
                os.rename(os.path.join('dist', 'dosya_adı.exe'), exe_dosya_adı)
                print(f"{py_dosya_adı} dosyası başarıyla {exe_dosya_adı} adıyla dönüştürüldü ve adı değiştirildi.")
            except Exception as e:
                print(f"Dönüştürme ve ad değiştirme işlemi başarısız oldu: {e}")

        def main():
            global py_dosya_adi
            global exe_dosya_adi

            py_dosya_adı = input("Lütfen dönüştürülecek Python dosyasının adını (ve .py uzantısını) girin: ")
            exe_dosya_adı = input("Lütfen oluşturulacak .exe dosyasının adını (ve .exe uzantısını) girin: ")
            dönüştür_ve_ad_değiştir(py_dosya_adı, exe_dosya_adı)

        if __name__ == "__main__":
            main()
    if com == "4" :
        print("Görüşürüz ...")
        exit()
