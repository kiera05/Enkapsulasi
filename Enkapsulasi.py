class Mahasiswa:
    def __init__(self, nama, nim):
        self._nama = nama
        self._nim = nim
        self._nilai_matakuliah = {}

    # --- PROPERTY (READ ONLY) ---
    @property
    def nama(self):
        return self._nama

    @property
    def nim(self):
        return self._nim

    # --- TAMBAH NILAI ---
    def tambah_nilai(self, matkul, nilai):
        if 0 <= nilai <= 100:
            self._nilai_matakuliah[matkul] = nilai
            print("[+] Nilai berhasil ditambahkan")
        else:
            print("[!] Nilai harus antara 0 - 100")

    # --- TAMPILKAN NILAI ---
    def tampilkan_nilai(self):
        if not self._nilai_matakuliah:
            print("[!] Belum ada nilai")
            return
        for mk, n in self._nilai_matakuliah.items():
            print(f"- {mk}: {n}")

    # --- RATA-RATA ---
    @property
    def nilai_rata_rata(self):
        if not self._nilai_matakuliah:
            return 0
        total = sum(self._nilai_matakuliah.values())
        return total / len(self._nilai_matakuliah)


# --- FUNGSI TAMPILKAN DAFTAR ---
def tampilkan_daftar(data):
    if not data:
        print("[!] Data kosong")
        return False
    print("\n=== DAFTAR MAHASISWA ===")
    for i, m in enumerate(data, 1):
        print(f"{i}. {m.nama} (NIM: {m.nim})")
    return True


# --- MAIN PROGRAM ---
def main():
    daftar_mahasiswa = []

    while True:
        print("\n" + "="*35)
        print("      SISTEM DATA MAHASISWA")
        print("="*35)
        print("1. Tambah Mahasiswa")
        print("2. Tambah Nilai")
        print("3. Lihat Data")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        # --- TAMBAH MAHASISWA ---
        if pilihan == '1':
            nama = input("Nama: ")
            nim = input("NIM: ")
            m = Mahasiswa(nama, nim)
            daftar_mahasiswa.append(m)
            print("[+] Mahasiswa berhasil ditambahkan")

        # --- TAMBAH NILAI ---
        elif pilihan == '2':
            if tampilkan_daftar(daftar_mahasiswa):
                try:
                    idx = int(input("Pilih nomor: ")) - 1
                    matkul = input("Mata kuliah: ")
                    nilai = int(input("Nilai: "))
                    daftar_mahasiswa[idx].tambah_nilai(matkul, nilai)
                except (ValueError, IndexError):
                    print("[!] Input salah")

        # --- LIHAT DATA ---
        elif pilihan == '3':
            if tampilkan_daftar(daftar_mahasiswa):
                for m in daftar_mahasiswa:
                    print("\n------------------")
                    print(f"Nama : {m.nama}")
                    print(f"NIM  : {m.nim}")
                    print("Nilai:")
                    m.tampilkan_nilai()
                    print(f"Rata-rata: {m.nilai_rata_rata:.2f}")

        # --- KELUAR ---
        elif pilihan == '4':
            print("Program selesai")
            break

        else:
            print("[!] Pilihan tidak valid")


# --- JALANKAN PROGRAM ---
if __name__ == "__main__":
    main()