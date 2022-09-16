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


## Menambahkan Repository Kali Linux
- install keyring .deb
```
wget http://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2022.1_all.deb
sudo dpkg -i kali-archive-keyring_2022.1_all.deb
sudo apt update
sudo apt-get update

```
- tambahkan repository
```
sudo nano /etc/apt/sources.list
```
```
#kali linux
deb http://http.kali.org/kali kali-rolling main contrib non-free
deb-src http://http.kali.org/kali kali-rolling main contrib non-free
deb http://http.kali.org/kali kali-last-snapshot main contrib non-free
deb http://http.kali.org/kali kali-experimental main contrib non-free
```
- tambahkan pada baris paling bawah, dan save
- update repository
```
sudo apt update
sudo apt-get update
sudo apt upgrade
sudo apt-get upgrade

```




## Install JAVA 18 (terbaru)
- download java 18
```
wget https://download.oracle.com/java/18/latest/jdk-18_linux-x64_bin.deb
```
- install
```
sudo dpkg -i jdk-18_linux-x64_bin.deb
```
**Note :** jika terjadi error seperti dibawah
```
dpkg: dependency problems prevent configuration of jdk-18:
 jdk-18 depends on libc6-i386; however:
  Package libc6-i386 is not installed.
 jdk-18 depends on libc6-x32; however:
  Package libc6-x32 is not installed.

dpkg: error processing package jdk-18 (--install):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 jdk-18
``` 
- perbaikan error (jika tidak terjadi error skip langkah ini)
```
sudo apt --fix-broken install
```
- setelah memperbaiki error lakukan **langkah install** kembali
- jadikan java 18 sebagai default
```
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-18/bin/java 1
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-18/bin/javac 1

```
- cek versi java
```
java --version

```
**Note :** jika sebelumnya sudah terinstall java, maka ikuti langkah berikut

- pindah prioritas java
```
sudo update-alternatives --config java
```
- pilih java 18
```
There are 2 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                            Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      auto mode
  1            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      manual mode
  2            /usr/lib/jvm/jdk-18/bin/java                     1         manual mode

Press <enter> to keep the current choice[*], or type selection number: 2
update-alternatives: using /usr/lib/jvm/jdk-18/bin/java to provide /usr/bin/java (java) in manual mode
```
**Note :** pada komputer saya, memilih no 2 karena java 18 ada di opsi 2

- lakukan cek versi java kembali





## Install Android Studio 2021.2
- pastikan java sudah terinstall
```
java --version
```
- pada pc saya menggunakan java 18
```
java 18.0.2.1 2022-08-18
Java(TM) SE Runtime Environment (build 18.0.2.1+1-1)
Java HotSpot(TM) 64-Bit Server VM (build 18.0.2.1+1-1, mixed mode, sharing)
```
- cari android studio di **snap**
```
snap find "android-studio"
```
- sesuai dengan versi terbaru
```
Name                   Version      Publisher     Notes    Summary
android-studio         2021.2.1.15  snapcrafters  classic  The IDE for Android
android-studio-canary  2022.1.1.7   snapcrafters  classic  The IDE for Android (Canary build)
```
- install android studio
```
sudo snap install android-studio --classic
```

#### Lanjutan Install Android Studio
- buka aplikasi 
- pada pop up pertama pilih `Do not import settings`
- pada pop up kedua pilih `Don't send`
- Welcome : `next`
- Install Type : `Standard` > `next`
- Select UI Theme : `bebaaasss (Darcula-gelap, Light-terang)` > `next`
- Verify Settings : `next`
- Emulator Settings : `finish`
- Downloading Components : `finish`
- masuk pembuatan project baru 