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






## Upgrade Python3.6 ke Python3.9
- cek versi
```
python3 --version
```
- tambahkan repository
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt-get update

```
- cek apakah versi 3.9 tersedia
```
apt list | grep python3.9
```
- install 3.9
```
sudo apt install python3.9
```
- update alternatives
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2
sudo update-alternatives --config python3

```
**Note :** pilih python versi 3.9 `pada pc saya adalah 0 dengan path /usr/bin/python3.9`, kemungkinan bisa berbeda tetapi tetap pilih versi 3.9
- cek versi
```
python3 -V
```
- python3 sudah terupdate menjadi 3.9



## Install PIP Python3.9
- install distutils
```
sudo apt install python3.9-distutils
```
**Note :** sesuaikan versi python


- install pip
```
sudo apt install python3-pip
```
- upgrade pip
```
pip3 install --upgrade pip
```
- sekalian install virtualenv
```
pip3 install virtualenv
```
- cara penggunaan
```
python3 -m virtualenv <nama_env>
```
- cara aktif dan non aktif virtualenv
```
source <path_activate>
```
```
deactivate
```
