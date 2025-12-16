from pembeli import main as pembeli_main
from penjual import main as penjual_main
from menu import judul



datapenjual = {
            'user1':'pw1', 
            'user2':'pw2',

        }

 
def login():
    while True:
        judul('\t\t       VERIFIKASI')
        print('1. Penjual')
        print('2. Pembeli')
        print()
        validasi = int(input('Siapakah Anda? [1/2] : '))
        if validasi == 1:
            judul('\t\t       LOGIN')
            username = input('Masukan Username : ')
            password = input('Masukan Password : ')

            if username in datapenjual and datapenjual[username] == password:
                print('login kehalaman penjual berhasil')
                print()
                penjual_main()
            
            else:
                print()
                print('password atau username salah')
                print()
        
        elif validasi == 2:
            print('login kehalaman user berhasil')
            print()
            pembeli_main()
        else:
            print('Harap masukkan nomor yang tersedia!!')
            continue
        break



if __name__ =='__main__':
        
        login()
