    # data produk 
produk = {
        "Sabun Mandi": [10000, 50],
        "Shampoo": [25000, 30],
        "Pasta Gigi": [15000, 20]
    }

    # perulangan untuk menampilkan data produk
while True:
        print("\n===== MENU PENGELOLAAN DATA PRODUK =====")
        print("1. Tampilkan Data Produk")
        print("2. Tambah Kategori Produk")
        print("3. Ubah Harga Produk")
        print("4. Hapus Kategori Produk")
        print("5. Keluar")
        print("=========================================")

    # menampilkan data produk
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            print("\n======= Daftar Data Produk =======")
            print(f"{'Nama Produk':<15}{'Harga':<7}{'Stok':<6}")
            for nama, detail in produk.items():
                harga, stok = detail
                print(f"{nama:<15}{harga:<7}{stok:<6}")
            print("=====================================")

    # menambahkan data produk
        elif pilihan == "2":
            nama = input("Masukkan nama produk baru: ")
            try:
                harga = int(input("Masukkan harga: "))
                stok = int(input("Masukkan stok: "))
                produk.update({nama: [harga, stok]})
                print(f"Produk berhasil ditambahkan.")
                
            except ValueError:
                print("Harga dan stok harus berupa angka.")

    # mengubah data produk
        elif pilihan == "3":
            nama = input("Masukkan nama produk yang ingin diubah: ")

            if nama in produk:
                try:
                    harga_baru = int(input("Masukkan harga baru: "))
                    produk[nama][0] = harga_baru
                    print(f"Harga produk '{nama}' berhasil diubah.")

                except ValueError:
                    print("Harga harus berupa angka.")
            else:
                print("Produk tidak ditemukan.")

    # menghapus data produk
        elif pilihan == "4":
            nama = input("masukkan nama produk yang ingin dihapus: ")

            if nama in produk:
                del produk[nama]
                print(f"produk'{nama}' berhasil dihapus.")
            else:
                print("produk tidak ditemukan.")

    # menghentikan program
        elif pilihan == "5":
            print("\n========program telah selesai=========")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-5.")

print("\nData Produk Setelah Perubahan:")
print(produk)