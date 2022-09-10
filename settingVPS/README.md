# VPS
Langkah awal dalam setting VPS adalah
- ping ip vps
```
ping <ip>
```
- login ssh
```
ssh <username>@<ip>
```
**Note :** biasanya username adalah `root` dan gunakan password yang sudah diberikan
- cek user root
```
whoami
pwd

```
- tambah user
```
adduser <user_anda>
```
```
usermod -aG sudo <user_anda>
```
- log out ssh
- login ssh dengan user baru anda
```
ssh <user_anda>@<ip>
```
**Note :** ip sama dengan root tadi