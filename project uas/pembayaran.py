from menu import garis,judul,format_rupiah,tampilkan_menu
from pesanan import lihat_keranjang

def bayar(data):
    judul('PEMBAYARAN')
    if len(data['keranjang']) == 0:
        print('keranjang kosong')
        input('ENTERR......')
        return
    
    total = lihat_keranjang(data)
    
    print("\n Pilih Metode Pembayaran:[1.Tunai/2.Qris]")
    metode = input('Pilih:')
    
    if metode == "2":
        print('Silakan Scan QRIS')
        input('Sudah Bayar? ENTERR....')
        bayar = total
        kembalian = 0
    else: 
        print(f'TOTAL: {format_rupiah(total)}')
        bayar = int(input('Bayar: Rp'))
        if bayar < total:
            print('Uang Kurang!')
            input('ENTERR.....')
            return
        kembalian = bayar - total
    
    for nama, jumlah in data ['keranjang'].items():
        data['Menu'][nama]['stok']-= jumlah
    
    data['pendapatan'] += total

    print('\n' + '='*50)
    print('STRUK PEMBAYARAN')
    garis()
    for nama,jumlah in data['keranjang'].items():
        harga =data['Menu'][nama]["Harga"]
        subtotal = harga * jumlah
        print(f"{nama:<20} {jumlah}x {format_rupiah(harga)} = {format_rupiah(subtotal)}")
    garis()
    print(f"Total = {format_rupiah(total)}")
    print(f"Bayar = {format_rupiah(bayar)}")
    print(f"Kembali = {format_rupiah(kembalian)}")
    print("=" * 50)  
    data["keranjang"] = {}

    input("ENTER...")

def tambah_stok(data):
    judul('TAMBAH STOK')
    tampilkan_menu(data)

    nomor = int(input('Nomor Menu: '))
    Daftar = list(data['Menu'].keys())

    if nomor < 0 or nomor > len(Daftar):
        print('Menu Tidak Ada!')
        input('ENTER...')
        return
    nama = Daftar [nomor -1]
    tambah = int(input('Tambah Berapa: '))

    if tambah <= 0:
        print('jumlah valid!')
        input('enterr...')
        return
    data["Menu"][nama]["stok"] += tambah
    print(f"Stok {nama} sekarang: {data['Menu'][nama]['stok']}")

    input("ENTER...")
    

data = {
    'Menu':{
        'Nasi Goreng': {'Harga': 15000, 'stok': 100},
        'Kwetiau': {'Harga': 14000, 'stok': 100},
        'Capcay' : {'Harga' : 13000, 'stok' : 100},
        'Lemon Tea' : {'Harga' : 6000, 'stok' : 100},
        'Teh Manis': {'Harga': 5000, 'stok': 100},
    },
    'keranjang': {},
    'pendapatan': 0
}
