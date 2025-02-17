# Hanafuda

Proyek ini hanya untuk experimen dan edukasi semata, gunakan dengan bijak. kami tidak bertanggung jawab apabila proyek ini digunakan untuk tujuan yang tidak tepat.
**Gunakan dengan bijak** kami tidak bertanggung jawab apa bila akun yang anda gunakan di tangguhkan sementara atau di blokir secara permanet.
##Fitur

  
i'm Moraevx 

**Terima Kasih**
## Instal python

1. **Instal python3:**
   ```bash
   sudo apt install python3
   ```
2. **Instal PIP:**
   ```bash
   sudo apt install python3-pip
   ```
3. **Verifikasi instalasi:**
   ```bash
   python3 --version
   ```
4. **Instal Paket**
   ```bash
   sudo apt update
   sudo apt install python3-requests python3-termcolor python3-colorama python3-pyfiglet
   ```
   
## Clone Repo Dan Menjalankan:

1. **Clone repositori ini:**
 
   ```bash
   git clone https://github.com/moraevx/assister.git
   cd assister
   ```
   
2. **Siapkan file `auth.txt`:**

   - Buat file bernama `auth.txt` di direktori yang sama dengan skrip.
   - Tambahkan token otentikasi Anda, satu token per baris. Setiap token mewakili akun yang berbeda.

   Contoh isi `auth.txt`:

   ```
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ8...
   ```

3. **Jalankan skrip:**

   ```bash
   python3 main.py
   ```

   Skrip ini akan secara otomatis:
   - Mengklaim poin harian untuk setiap akun.

## Mengambil Token Otentikasi

Untuk mengambil `auth` dari cookies di browser:

1. **Buka Developer Tools:**
   - Tekan `F12` atau `Ctrl + Shift + I` di Windows/Linux, atau `Cmd + Option + I` di macOS.
   - Buka tab **Console**.

2. **Jalankan skrip berikut di console:**

   ```javascript
   let cookies = document.cookie.split('; ');
   let refreshToken = cookies.find(cookie => cookie.startsWith('refreshToken=')).split('=')[1];
   prompt('UGD AIRDROP:', refreshToken);
   ```

   - Sebuah prompt akan muncul dengan `auth`. Salin token tersebut dan tempelkan ke file `auth.txt`.

## Catatan:

- Pastikan Anda memperbarui file `auth.txt` dengan token yang valid secara berkala agar otomasi tetap berfungsi.
- Skrip akan berhenti selama 24 jam setelah setiap kali dijalankan, menunggu untuk mengklaim poin harian berikutnya. Jika ingin bekerja selama 24 jam maka jalankan di dalam screen




