def garis():
    print('-'*50)

def judul(teks):
    print()
    print('='*50)
    print('\t\tWARUNG 5 ORANG TAMPAN')
    print('='*50)
    print(teks)
    print('='*50)
    print()

def format_rupiah(angka):
    return f"Rp.{angka:,}".replace(',',',')

def tampilkan_menu(data):
    print('\nDaftar Menu:')
    garis()
    print(f"{'No':<5}{'Nama Menu':20}{'Harga':15}{'stok'}")
    garis()

    nomor = 1
    for nama, item in data['Menu'].items():
        print(f"{nomor:<5}{nama:20}{format_rupiah( item['Harga']):15}{item['stok']} porsi")
        nomor += 1
    garis()
