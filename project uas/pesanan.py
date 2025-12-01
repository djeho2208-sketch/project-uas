import menu 

def pesan(data):
    menu.judul("Pesan Makanan")
    menu.tampilkan_menu(data)

    banyak_pesan = int(input('Banyak Pesan: '))

    for i in range(banyak_pesan):
        print(f"\nPesanan ke-{i+1}")

        nomor = int(input('Silakan Pilih Nomor Menu (1-5): '))
        daftar = list(data['Menu'].keys())

        if nomor < 1 or nomor > len(daftar):
            print('Nomor Tidak Ada!')
            input('ENTER...')
            continue

        nama = daftar[nomor - 1]
        stok = data['Menu'][nama]['stok']

        if stok <= 0:
            print('Stok Habis!')
            input('ENTER...')
            continue

        print(f'Stok tersedia: {stok}')
        jumlah = int(input('Mau berapa?: '))

        if jumlah <= 0 or jumlah > stok:
            print('Jumlah Tidak Valid!')
            input('ENTER...')
            continue

        if nama in data['keranjang']:
            data['keranjang'][nama] += jumlah
        else:
            data['keranjang'][nama] = jumlah

        print(f'{nama} sebanyak {jumlah} ditambahkan ke keranjang!')
        input('ENTER...')

def lihat_keranjang(data):
    keranjang = data['keranjang']
    if len(keranjang) == 0:
        print('Keranjang kosong')
        return 0

    print('\n' + '='*50)
    print('ISI KERANJANG')
    print('='*50)

    total = 0 

    for nama, jumlah in keranjang.items():
        harga = data['Menu'][nama]['Harga']
        subtotal = harga * jumlah
        total += subtotal
        print(f"{nama:<20} {jumlah} x {menu.format_rupiah(harga):<10} = {menu.format_rupiah(subtotal)}")  

    menu.garis()
    print(f"{'TOTAL':<36} = {menu.format_rupiah(total)}")
    print("=" * 50)

    return total

def hapus_pesanan(data):
    menu.judul('HAPUS PESANAN')

    if len(data['keranjang']) == 0:
        print('Keranjang Kosong')
        input('Enterr....')
        return
    lihat_keranjang(data)
    
    nama = input('Nama Menu Yang Mau DiHapus:')

    if nama in data['keranjang']:
        del data['keranjang'][nama]
        print(f"{nama} Berhasil Dihapus")
    else:
        print('Nama Tidak Ada di Keranjang!')
    input('ENTERR.....')
    