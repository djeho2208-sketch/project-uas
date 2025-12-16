from menu import judul,tampilkan_menu

from pembayaran import data,tambah_stok
from wexit import welcome_message,exit_program




def optionspenjual():
    while True: 
        judul('\t\t   MENU UTAMA PENJUAL')
        print('1. Lihat Menu')
        print('2. Tambah Stok')
        print('0. Keluar')
        print()

        pilih = input('pilih: ')

        if pilih == '1':
            tampilkan_menu(data)
            input('ENTERR...')
        elif pilih == '2':
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
    optionspenjual()
   





        