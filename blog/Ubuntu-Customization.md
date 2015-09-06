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

### Aliases

`sudo gedit ~/.bash_aliases`, add:

	alias agi='sudo apt-get install'
	alias agr='sudo apt-get remove'
	alias agu='sudo apt-get update; sudo apt-get upgrade; sudo apt-get dist-upgrade; sudo apt-get autoremove'
	alias aar='sudo apt-add-repository'

	alias e='exit'
	alias s='sudo'
	alias ..='cd ..'
	alias shutdown='sudo shutdown -h now'
	alias restart='sudo shutdown -r now'

	alias ppi='sudo pip install'
	alias zouni='sudo git add .; sudo git commit -a -m rev; sudo git push'

	alias sba='sudo subl ~/.bash_aliases'

	alias proxy_on='export http_proxy=http://127.0.0.1:8787; export https_proxy=$http_proxy; echo proxy_on'
	alias proxy_off='unset http_proxy; unset https_proxy; echo proxy_off'
	alias my_ip='curl -s icanhazip.com'

### Text Editor

* sublime_text 3:

	`aar ppa:webup8team/sublime-text-3; agu; agi sublime-text-installer`

	to launch: `subl`   

### Git

	agi git
	s git config --global user.name "YOUR NAME"
	s git config --global user.email "YOUR EMAIL ADDRESS"
	s git config credential.helper store

### Web Browser

* Firefox aurora:

	`aar ppa:ubuntu-mozilla-daily/firefox-aurora; agu`

* Vimperator.xpi:

	`s git clone https://github.com/vimperator/vimperator-labs; cd vimperator-labs; s make xpi; s mv downloads/vimperator*.xpi ~/Vimperator.xpi; cd ..; s rm -r vimperator-labs; firefox ~/Vimperator.xpi`

### Proxies

* [shadowsocks-qt5](https://github.com/librehat/shadowsocks-qt5)

	`aar ppa:hzwhuang/ss-qt5; agu; agi shadowsocks-qt5`

* [lantern](https://getlantern.org/)

	`wget https://s3.amazonaws.com/lantern/lantern-installer-beta-64-bit.deb; sudo dpkg -i lantern-installer-beta-64-bit.deb; rm lantern-installer-beta-64-bit.deb`

### Other Packages
	
* [glances](https://github.com/nicolargo/glances)

	`agi python-pip; agi python-dev; ppi glances`

* [htop](https://github.com/hishamhm/htop)
	
	`agi htop`

* [thefuck](https://github.com/nvbn/thefuck)

	`wget -O - https://raw.githubusercontent.com/nvbn/thefuck/master/install.sh | sh - && $0`

