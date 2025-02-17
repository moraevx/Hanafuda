# Hanafuda

Proyek ini hanya untuk experimen dan edukasi semata, gunakan dengan bijak. kami tidak bertanggung jawab apabila proyek ini digunakan untuk tujuan yang tidak tepat.
**Gunakan dengan bijak** kami tidak bertanggung jawab apa bila akun yang anda gunakan di tangguhkan sementara atau di blokir secara permanet.
  
i'm Moraevx 

**Terima Kasih**
#Fitur
- Multi Akun
- Auto Draw
- Auto Deposit


## Mengambil AuthToken dan RefreshToken
- Login terlebih dahulu ke https://hanafuda.hana.network/dashboard
- Gunakan kode undangan `**XC2MZ4**` untuk mendapatkan point tambahan
- Gunakan Dev Tool atau (Tekan F12 atau Ctrl + Shift + I di Windows/Linux, atau Cmd + Option + I di macOS )
  
  
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
   sudo apt update && sudo apt upgrade -y
  sudo apt install -y python3 python3-pip python3-aiohttp python3-colorama python3-web3 python3-argparse python3-pyfiglet
   ```
   
## Clone Repo Dan Menjalankan:

1. **Clone repositori ini:**
 
   ```bash
   git clone https://github.com/moraevx/hanafuda.git
   cd hanafuda
   ```
   
2. **Siapkan file `pvkey.txt`:**

   - Ganti file `pvkey.txt` dengan privatkey anda
   - Setaip line mewakili akun yang berbeda

   Contoh isi `pvkey.txt`:

   ```
   {
    "Your_Privatkey_1"
    "Your_Privatkey_1"  
   }
   ```

3. **Siapkan file `token.txt`:**

   - Ganti dengan refreshToken anda
   - Setiap line mewakili akun yang berbeda **[ HARUS SAMA DENGAN URUTAN PRIVATKEY ]**

   ```
    AMf-vB...Your_Token_1
    AMf-vB...Your_Token_2
   ```

3. **Siapkan file `token.json`:**

   - Ganti dengan authToken dan refreshToken anda
   - Setiap line mewakili akun yang berbeda **[ HARUS SAMA DENGAN URUTAN PRIVATKEY ]**

   ```
    [
    {
      "authToken": "Bearer your_initial_auth_token_1",
      "refreshToken": "your_initial_refresh_token_1"
    },
    {
      "authToken": "Bearer your_initial_auth_token_2",
      "refreshToken": "your_initial_refresh_token_2"
    }
    ]
   ```



