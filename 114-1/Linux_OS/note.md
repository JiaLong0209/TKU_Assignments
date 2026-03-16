
## week 2 
### install VMware in arch linux 

https://medium.com/@r3t2skull/install-vmware-workstation-on-arch-linux-febe66259838

```bash
sudo pacman -S fuse2 gtkmm linux-headers pcsclite libcanberra

```


###  VMware workstation pro
check WHD


## Week 3

```bash
echo $SHELL

sudo grep -e .*=.* /etc/os-release

```

## week5 - VIM

```bash
# Install vim
sudo apt install vim -y

```

### homework

```bash
cd 
mkdir exercise1

cd ~/exercise1
```

```bash
cd 
mkdir exercise1

cd ~/exercise1
```


### Shell

```bash
chmod u+x *.sh 
```

## Week8 - file permission and net tool


### file permission
```bash

ls -l /etc | head 

```
total 1480
-rw-r--r-- 1 root    root        44  6月 25 07:28 adjtime
drwxr-xr-x 1 root    root        12  3月  8  2025 alsa
drwxr-xr-x 1 root    root       318 10月 21 09:55 apparmor.d
-rw-r--r-- 1 root    root         1 10月 13 00:21 arch-release
drwxr-xr-x 1 root    root       180 10月 21 09:55 ardour8
drwxr-xr-x 1 root    root        28  6月 25 08:12 arp-scan
-rw-r--r-- 1 root    root         0  3月 23  2025 arptables.conf
drwxr-xr-x 1 root    root         0  1月 12  2025 audisp
drwxr-xr-x 1 root    root       188  6月 25 07:51 audit

Breakdown:
Part	Example	Meaning
1. File type & permissions	-rw-r--r--	Describes what kind of file it is and who can access it.
2. Hard link count	1	How many hard links (directory entries) point to this file.
3. Owner (user)	root	The user who owns this file.
4. Group	root	The group that owns this file.
5. File size (bytes)	44	Size of the file in bytes.
6~8. Last modified date	6月 25 07:28	Month, day, and time the file was last modified (in your system locale).
9. File name	adjtime	The name of the file or directory.

---

Type | U (user)| G (group) | O (others)


e.g.1 將 file 權限變更為 -rwxr-x--x → 
chmod u=rwx,g=rx,o=x file

chmod u+x a.txt


### net tools

```bash

sudo apt install net-tools -y
sudo apt install iputils-ping -y
sudo apt install dnsutils -y


ifconfig

# 追蹤當前裝置連線至 google public DNS 需經過哪些節點。
sudo traceroute -I 8.8.8.8 

# traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
#  1  _gateway (192.168.182.244)  7.165 ms  7.252 ms  7.368 ms
#  2  10.156.65.128 (10.156.65.128)  206.677 ms  206.676 ms  206.675 ms
#  3  10.156.65.5 (10.156.65.5)  35.741 ms  35.740 ms  35.740 ms
#  4  10.156.67.150 (10.156.67.150)  35.635 ms  35.634 ms  35.633 ms
#  5  10.156.67.178 (10.156.67.178)  36.463 ms  38.841 ms  38.839 ms
#  6  210-65-126-98.tpdb-3312.hinet.net (210.65.126.98)  36.407 ms  28.581 ms  28.57
# 0 ms
#  7  * * *
#  8  * * *
#  9  220-128-13-161.pcpd-3332.hinet.net (220.128.13.161)  39.993 ms  39.284 ms  39.
# 270 ms
# 10  72.14.202.162 (72.14.202.162)  39.265 ms  39.392 ms  38.418 ms
# 11  142.250.224.97 (142.250.224.97)  37.030 ms  21.530 ms  30.197 ms
# 12  108.170.225.177 (108.170.225.177)  31.843 ms  31.842 ms  31.836 ms
# 13  dns.google (8.8.8.8)  31.650 ms  30.239 ms  28.797 ms

ping 8.8.8.8

ping -c 4 -t 11 8.8.8.8

host www.tku.edu.tw 
# www.tku.edu.tw has address 203.145.221.108

host 203.145.221.108   
# 108.221.145.203.in-addr.arpa domain name pointer 203-145-221-108.twcc.ai.

nslookup www.tku.edu.tw 
# Server:         192.168.182.244
# Address:        192.168.182.244#53
# 
# Non-authoritative answer:
# Name:   www.tku.edu.tw
# Address: 203.145.221.108

nslookup 203.145.221.108

# 108.221.145.203.in-addr.arpa    name = 203-145-221-108.twcc.ai.
# Authoritative answers can be found from:


```

### Cron table

```bash
# Debian / Ubuntu:

sudo apt install cron
sudo systemctl enable --now cron


# Arch Linux:

sudo pacman -S cronie
sudo systemctl enable --now cronie

```

### file system

#### Arch Linux

```bash

sudo blkid | grep btrfs

# /dev/nvme0n1p8: LABEL="home" UUID="43301041-aae7-4b23-ac69-1ddd3dc5fb3f" UUID_SUB="4b2dff2d-993d-4e28-a51f-5abe08758b24" BLOCK_SIZE="4096" TYPE="btrfs" PARTUUID="37e243ac-3346-4c8c-8d58-aa558f8b7796"
# /dev/nvme0n1p6: LABEL="root" UUID="88179240-3396-432a-8a85-5e20b20d0526" UUID_SUB="1f394bd3-a3cc-449d-a99b-0172a0cf0f7a" BLOCK_SIZE="4096" TYPE="btrfs" PARTUUID="f81869e0-7df6-48c2-8e99-e7ed59bb7597"

sudo btrfs inspect-internal dump-super -f /dev/nvme0n1p6

```

## week10 - firewall

### Firewall tool

```bash

sudo iptables -L -v

# Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
#  pkts bytes target     prot opt in     out     source               destination         
# 
# Chain FORWARD (policy DROP 0 packets, 0 bytes)
#  pkts bytes target     prot opt in     out     source               destination         
#     0     0 DOCKER-USER  all  --  any    any     anywhere             anywhere            
#     0     0 DOCKER-FORWARD  all  --  any    any     anywhere             anywhere            
# 
# Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
#  pkts bytes target     prot opt in     out     source               destination         
# 
# Chain DOCKER (1 references)
#  pkts bytes target     prot opt in     out     source               destination         
#     0     0 DROP       all  --  !docker0 docker0  anywhere             anywhere            
# 
# Chain DOCKER-BRIDGE (1 references)
#  pkts bytes target     prot opt in     out     source               destination         
#     0     0 DOCKER     all  --  any    docker0  anywhere             anywhere            
# 
# Chain DOCKER-CT (1 references)
#  pkts bytes target     prot opt in     out     source               destination         
#     0     0 ACCEPT     all  --  any    docker0  anywhere             anywhere             ctstate RELATED,ESTABLISHED
# 
# Chain DOCKER-FORWARD (1 references)
#  pkts bytes target     prot opt in     out     source               destination         
#     0     0 DOCKER-CT  all  --  any    any     anywhere             anywhere            
#     0     0 DOCKER-ISOLATION-STAGE-1  all  --  any    any     anywhere             anywhere            
#     0     0 DOCKER-BRIDGE  all  --  any    any     anywhere             anywhere            
#     0     0 ACCEPT     all  --  docker0 any     anywhere             anywhere            
# 
# Chain DOCKER-ISOLATION-STAGE-1 (1 references)
#  pkts bytes target     prot opt in     out     source               destination         
#     0     0 DOCKER-ISOLATION-STAGE-2  all  --  docker0 !docker0  anywhere             anywhere            
# 
# Chain DOCKER-ISOLATION-STAGE-2 (1 references)
#  pkts bytes target     prot opt in     out     source               destination         
#     0     0 DROP       all  --  any    docker0  anywhere             anywhere            
# 
# Chain DOCKER-USER (1 references)
#  pkts bytes target     prot opt in     out     source               destination         


#------------------
# public key: encript
# private key:  decode

```
### SSH

```bash

# install
sudo apt install ssh -y


# check
ip a

ssh debian@ip

sudo systemctl status sshd

```

### Web server


```bash

```


## Week 13 (minecraft server)

```bash

# 1
sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft

# 2
sudo -u minecraft mkdir /opt/minecraft/server
cd /opt/minecraft/server
sudo -u minecraft wget https://launcher.mojang.com/v1/objects/.../server.jar -O server.jar

# 3 Accept EULA
echo "eula=true" | sudo -u minecraft tee /opt/minecraft/server/eula.txt

# 4

sudo -u minecraft nano /opt/minecraft/server/start.sh

# start.sh
#!/bin/bash 
# java -Xms2G -Xmx4G -jar server.jar nogui #

sudo chmod +x /opt/minecraft/server/start.sh


# 5
sudo vim /etc/systemd/system/minecraft.service

# [Unit]
# Description=Minecraft Server
# After=network.target
# 
# [Service]
# User=minecraft
# Group=minecraft
# WorkingDirectory=/opt/minecraft/server
# ExecStart=/bin/bash /opt/minecraft/server/start.sh
# Restart=on-failure
# RestartSec=10
# StandardOutput=append:/opt/minecraft/server/server.log
# StandardError=append:/opt/minecraft/server/server.log
# 
# [Install]
# WantedBy=multi-user.target

# 6 
sudo systemctl daemon-reload
sudo systemctl start minecraft
sudo systemctl enable minecraft

# check

sudo systemctl status minecraft
journalctl -u minecraft -f


```












