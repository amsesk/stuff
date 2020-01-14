### Getting Wifi Card Working
Download and install driver from AUR, then build. 
##### Download from AUR
```
git clone https://aur.archlinux.org/rtl88x2ce-dkms.git
cd rtl88x2ce-dkms
# Install package
makepkg -si
reboot
```

Getting Apple Airbuds to Work
-Follow ArchWiki and use Blueman 

###CIFS to mycology server
```
alias mycology="sudo mount -t cifs -o username=amsesk,domain=UMROOT,vers=1.0 //lsa-research01.m.storage.umich.edu/lsa-research01/tyjames/mycology /mnt/mycology/"
```


###Set network interface to unmanaged by NetworkManager
In file: /etc/udev/rules.d/o-nta1000-net.rules
```
ACTION=="add", SUBSYSTEM=="net", KERNEL=="wlan0", ENV{NM_UNMANAGED}="1"
```
