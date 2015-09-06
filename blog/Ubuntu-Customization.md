---
layout:      post
title:       Ubuntu Customization
date:        2015-09-06
update_date: 
summary:     
categories:  blog
permalink:   /blog/Ubuntu-Customization/
---

Here are some of my favorite Ubuntu customizations.

* Aliases

> `sudo gedit ~/.bash_aliases`, add:

	alias agi = 'sudo apt-get install'
	alias agr = 'sudo apt-get remove'
	alias agu = 'sudo apt-get update; sudo apt-get upgrade; sudo apt-get dist-upgrade; sudo apt-get autoremove'
	alias aar = 'sudo apt-add-repository'

	alias e = 'exit'
	alias s = 'sudo'
	alias shutdown = 'sudo shutdown -h now'
	alias restart = 'sudo shutdown -r now'

* atom
```
sudo add-apt-repository ppa:webupd8team/atom; sudo apt-get update; sudo apt-get install atom
```

* firefox aurora

```
aar ppa:ubuntu-mozilla-daily/firefox-aurora; agu
```

* proxy

shadowsocks-qt5

```
sudo add-apt-repository ppa:hzwhuang/ss-qt5; sudo apt-get update; sudo apt-get install shadowsocks-qt5
```

lantern
```
wget https://s3.amazonaws.com/lantern/lantern-installer-beta-64-bit.deb; sudo dpkg -i lantern-installer-beta-64-bit.deb; rm lantern-installer-beta-64-bit.deb
```


* git

```
agi git
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR EMAIL ADDRESS"
git config credential.helper store
```
via proxy:
```
git config --global http.proxy http://127.0.0.1:8787; git config --global https.proxy https://127.0.0.1:8787
```
to unset:
```
git config --global --unset http.proxy; git config --global --unset https.proxy
```
* Glances

```
agi python-pip
sudo pip install Glances
sudo pip install PySensors
```

* Brackets

```
aar ppa:webupd8team/brackets; agi brackets
```

* thefuck

```
wget -O - https://raw.githubusercontent.com/nvbn/thefuck/master/install.sh | sh - && $0
```
