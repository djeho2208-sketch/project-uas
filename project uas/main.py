from menu import judul,tampilkan_menu
from pesanan import pesan,lihat_keranjang,hapus_pesanan
from pembayaran import data,bayar,tambah_stok
from wexit import welcome_message,exit_program

def options():
    while True: 
        judul('\t\t   MENU UTAMA')
        print('1. Lihat Menu')
        print('2. Pesan')
        print('3. Hapus Pesanan')
        print('4. Lihat Keranjang')
        print('5. Bayar')
        print('6. Tambah Stok')
        print('0. Keluar')
        print()

        pilih = input('pilih: ')

        if pilih == '1':
            tampilkan_menu(data)
            input('ENTERR...')
        elif pilih == '2':
            pesan(data)
        elif pilih == '3':
            hapus_pesanan(data)
        elif pilih == '4':
            lihat_keranjang(data)
            input('ENTERR...')
        elif pilih == '5':
            bayar(data)
        elif pilih == '6':
            tambah_stok(data)
        elif pilih == "0":
            print("Terima kasih!")
            exit_program()
            break

        else:
            print('pilihan salah')
            input('enterr...')

def main():
    welcome_message()
    options()

if __name__ =='__main__':
        main()
        