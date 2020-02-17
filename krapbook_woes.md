### Getting Wifi Card Working

Apparently the specific driver for the Wifi/bluetooth combo card I have is not default included in the Arch kernel

# Download from AUR
git clone https://aur.archlinux.org/rtl88x2ce-dkms.git
cd rtl88x2ce-dkms
# Install package
makepkg -si
Reboot

Getting Apple Airbuds to Work
# Install packages from official repositiries
Pacman 

### CIFS to mycology server
```
alias mycology="sudo mount -t cifs -o username=amsesk,domain=UMROOT,vers=1.0 //lsa-research01.m.storage.umich.edu/lsa-research01/tyjames/mycology /mnt/mycology/"
```

### Set network interface to unmanaged by NetworkManager
In file: /etc/udev/rules.d/o-nta1000-net.rules
```
ACTION=="add", SUBSYSTEM=="net", KERNEL=="wlan0", ENV{NM_UNMANAGED}="1"
```

Set wireless interface to unmanaged by NetworkManager via udev
I think that I figured out a solution to this problem, so I figured I'd post it just in case others having the same problem find their way to this thread. I wasn't able to completely remove the duplicated interface, but I was able to set its state with NetworkManager to unmanaged. I haven't had a similar kernel panic or crash since doing that, so I am assuming it is a viable work around, at least for now. I achieved this through creating a file at
/etc/udev/rules.d/wlan0_set_unmanaged.rules
containing...
ACTION=="add", SUBSYSTEM=="net", KERNEL="wlan0", ENV{NM_UNMANAGED}="1"
After rebooting, you can run
nmcli dev
as root to verify that the interface has been set the "unmanaged" for NetworkManager.

### Connection config for UMVPN

### Auto-mount removable media (microSD card in this case) via udev

### Dontkillssh.service (global service)

### Globus-endpoint.service (user service)
```

```

###Setting up conky

```
Sudo apt install conky
Sudo apt install lm-sensors
Sensors-detect
Sensors
```
Put the following in conky.conf to display CPU core temperatures:
```
${color #42AE4A}Core 0 ${color lightgrey}${exec sensors | grep 'Core 0' | grep -o -m 1 -E "[+][0-9]*[.][0-9]*.C" | h
ead -n1}
${color #42AE4A}Core 1 ${color lightgrey}${exec sensors | grep 'Core 1' | grep -o -m 1 -E "[+][0-9]*[.][0-9]*.C" | h
ead -n1}
${color #42AE4A}Core 2 ${color lightgrey}${exec sensors | grep 'Core 2' | grep -o -m 1 -E "[+][0-9]*[.][0-9]*.C" | h
ead -n1}
${color #42AE4A}Core 3 ${color lightgrey}${exec sensors | grep 'Core 3' | grep -o -m 1 -E "[+][0-9]*[.][0-9]*.C" | h
ead -n1}
```

Conky likes to disappear when you click the desktop. Edit the settings like so to prevent that (conky.conf):
```
